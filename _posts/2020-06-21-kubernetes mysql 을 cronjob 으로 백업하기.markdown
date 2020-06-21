---
layout: single
title:  "kubernetes mysql 을 cronjob 으로 백업하기"
date:   2020-06-21 11:10:03 +0900
categories: [kubernetes, mysql, cronjob]
---


## 환경
* GKE
* Mysql (StatefulSet 으로 배포)

## 할 일
1. dump 파일을 저장할 bucket 생성 (설명 생략)
2. 서비스 어카운트와 key 가져오기
3. gsutil과 mysqldump가 설치된 docker image 준비하기
4. github action 스크립트로 docker build
5. docker image 를 cronjob 으로 배포


## 서비스 어카운트와 key 가져오기

GCP 콘솔 > IAM 에서 (저는 Editor 권한을 갖고 있는 default 계정을 사용했습니다.) > service account 선택 > email 복사.
(github action 페이지에서 GKE_EMAIL 로 사용) 

선택한 service account > Keys > Key 하나 새로 발급 > json 선택 (프로젝트 내부에서, 그리고 github action 페이지에서 GKE_KEY 로 사용)


## 도커 이미지 준비

```dockerfile
FROM google/cloud-sdk:alpine

# mysqldump 설치
RUN apk --update add mysql-client

# timezone 설정
RUN apk add tzdata
RUN cp /usr/share/zoneinfo/Asia/Seoul /etc/localtime
RUN echo "Asia/Seoul" > /etc/timezone
RUN date

# 아까 다운로드 받은 파일을 service-account.json 이라는 이름으로 프로젝트에 넣었습니다.
# 프로젝트에 넣은 파일을 docker 이미지 내부에 복사해서 넣습니다.
COPY service-account.json /root/service_key.json
# backup 을 담당하는 스크립트 backup.sh
COPY backup.sh /root/backup.sh

RUN gcloud config set project soyeon-275107 && \
    gcloud auth activate-service-account --key-file /root/service_key.json && \
    gsutil ls gs://soyeonlab-mysql-backup/
RUN chmod +x /root/backup.sh

ENTRYPOINT ["/root/backup.sh"]
```
베이스 이미지는 cloud-sdk:alpine 을 사용합니다. gcloud 와 gsutil이 자동으로 깔려 있어요!
alpine 리눅스 기반이기 때문에 패키지 매니저로 apk 를 사용합니다. timezone 을 세팅해요.(생략 가능)

```shell script
# backup.sh
# 오늘-날짜.sql 파일을 mysqldump을 사용해서 만듭니다. 이후 gsutil을 사용해서 bucket에 복사! 
echo "dumping ... $DB_HOST, $DB_USER, $DB_PASS, $DB_NAME to $GS_BUCKET 디버깅용"
mysqldump --user="${DB_USER}" --password="${DB_PASS}" --host ${DB_HOST} ${DB_NAME} > /root/$(date +\%Y-\%m-\%d).sql
gsutil cp /root/$(date +\%Y-\%m-\%d).sql ${GS_BUCKET}
```
위와 같이 backup.sh 를 만들고, 나중에 cronjob 을 정의할 때 환경변수를 넣어주면 됩니다.

## github action 스크립트

```yaml
name: GCP publish production

on:
  push:
    branches: [ master ]
  pull_request:
    branches: [ master ]

# Environment variables available to all jobs and steps in this workflow
env:
  GKE_PROJECT: ${{ secrets.GKE_PROJECT }}
  GKE_EMAIL: ${{ secrets.GKE_EMAIL }}
  GITHUB_SHA: ${{ github.sha }}
  GKE_ZONE: asia-northeast3-a
  IMAGE: sy-mysql-backup
  REGISTRY_HOSTNAME: gcr.io

jobs:
  setup-build-publish-deploy:
    name: Setup, Build, Publish, and Deploy
    runs-on: ubuntu-latest
    steps:

    - name: Checkout
      uses: actions/checkout@v2

    # Setup gcloud CLI
    - uses: GoogleCloudPlatform/github-actions/setup-gcloud@master
      with:
        version: '270.0.0'
        service_account_email: ${{ secrets.GKE_EMAIL }}
        service_account_key: ${{ secrets.GKE_KEY }}

    # Configure docker to use the gcloud command-line tool as a credential helper
    - run: |
        # Set up docker to authenticate
        # via gcloud command-line tool.
        gcloud auth configure-docker
    # Build the Docker image
    - name: Build
      run: |
        docker build -t "$REGISTRY_HOSTNAME"/"$GKE_PROJECT"/"$IMAGE":"$GITHUB_SHA" \
          --build-arg GITHUB_SHA="$GITHUB_SHA" \
          --build-arg GITHUB_REF="$GITHUB_REF" .
    # Push the Docker image to Google Container Registry
    - name: Publish
      run: |
        docker push $REGISTRY_HOSTNAME/$GKE_PROJECT/$IMAGE:$GITHUB_SHA
```

아까 저장해 두었던 GKE_EMAIL 과 GKE_KEY 를 
깃허브 > 리포지토리 > 설정 > secrets 안에 넣습니다.

여기까지 하고 마스터에 푸쉬하면 docker image 를 빌드해 cloud registry 안에 저장합니다.

## docker image 를 cronjob 으로 배포

```yaml
apiVersion: batch/v1beta1
kind: CronJob
metadata:
  name: mysql-backup
spec:
  schedule: "49 12 * * *"
  jobTemplate:
    spec:
      template:
        spec:
          restartPolicy: OnFailure
          containers:
            - name: mysql-backup
              image: gcr.io/<프로젝트ID>/sy-mysql-backup:<깃 해쉬(이미지 태그)>
              env:
                - name: GOOGLE_PROJECT
                  value: <프로젝트ID>
                - name: GOOGLE_EMAIL
                  value: <앞서 저장한 service account의 email>
                - name: DB_HOST
                  value: <kubernetes mysql 서비스의 IP>
                - name: DB_USER
                  value: <root 혹은 사용하고 있는 mysql 계정>
                - name: DB_PASS
                  valueFrom:
                    secretKeyRef:
                      name: <secret 이름>
                      key: <mysql 비밀번호가 들어있는 key>
                - name: DB_NAME
                  value: <백업할 mysql database>
                - name: GS_BUCKET
                  value: gs://<백업을 저장할 버킷 이름>
```

## 한계
cronjob 은 kube-controller-manager 의 시간대에 의존합니다.
그런데 gke 의 kube-controller-manager 는 가려져 있기 때문에 (control plane 전체가 GCP에 의해 가려짐.)
시간대를 한국 시간대로 바꿀 수가 없어요! ㅠㅠ

특정 주기에 의해 돌아가는 cron 을 만들거나
외국 시간대에 맞추는 것 밖에 할 수 없습니다.
단! 위처럼 이미지 내부의 시간대는 조절할 수 있습니다. (cron 이 실행되는 시간대는 조절할 수 없지만)


## 끝!

궁금하신 점은 댓글 주세요

## 참고

https://www.serverlab.ca/tutorials/containers/kubernetes/using-kubernetes-cronjob-to-backup-mysql-on-gke/



