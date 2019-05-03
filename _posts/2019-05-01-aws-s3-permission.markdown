---
layout: single
title:  "원숭이도 따라한다! 쉽게 aws s3 퍼블릭 버킷 만들기"
date:   2019-05-01 11:10:03 +0900
categories: [aws, s3]
--- 

## 사전 준비
S3? 쉽고 빠르게 시작해 봅시다. 

AWS S3 를 사용하려면 당연히 AWS 계정이 필요해요. 먼저 계정을 생성하신 후
계속해 주시길 바랍니다.

이번 글에서는 버킷을 만든 후에 public 접근을 열어놓는 것 까지를 다루겠습니다.
write 접근은 막고, 퍼블릭 read 접근만 허용해서 이미지 서버, 스태틱 서버 등으로
S3 를 활용할 수 있게 세팅합니다.

## s3 버킷 생성
S3 에서 데이터를 저장하는 공간을 버킷이라고 합니다. 

AWS 콘솔 홈에서 S3 를 검색해서 들어가면 처음에 아래와 같은 화면이 뜹니다.
아직 S3 버킷이 하나도 없다는 뜻입니다.
![image-center]({{ site.baseurl }}/assets/images/2019-05-02-s3-2.jpg){: .align-center}

이제부터 순서대로 따라해 주세요.

![image-center]({{ site.baseurl }}/assets/images/2019-05-02-s3-3.jpg){: .align-center}
Create bucket 을 클릭!
{: .text-center }

![image-center]({{ site.baseurl }}/assets/images/2019-05-02-s3-4.jpg){: .align-center}
Bucket name 에 원하는 이름을 적습니다.
{: .text-center }

메이플 이름을 만들때 처럼 버킷 이름은 겹치면 안됩니다. s3 버킷을 생성하면
버킷에 URL 이 할당되게 되는데, 전 세계 어디에서도 인터넷만 되면 이 URL 을 통해
버킷에 접근할 수 있습니다. 따라서 버킷이름은 전 세계에서 고유한 값이어야 합니다.

이름을 지었다면 하단의 Next 를 눌러 다음으로 넘어갑니다.

![image-center]({{ site.baseurl }}/assets/images/2019-05-02-s3-5.jpg){: .align-center}
Versioning : Keep all versions of an object in the same bucket 만 체크하고
다음으로 넘어갑니다.
{: .text-center }

버킷에 데이터를 저장할 때에는 파일 그대로를 저장하는 것이 아니라 객체(Object)의 형태로
저장합니다. S3에서 말하는 "객체(Object)"의 개념은 다음과 같습니다.

객체는 키, 객체 데이터, 메타 데이터로 구성됩니다.

키: 파일 이름과도 같습니다. 나중에 "버킷 URL + 키" 로 파일을 다운로드 받을 수 있습니다.

객체 데이터: 여러분이 업로드한 파일(이미지, 스크립트 등등) 혹은 데이터 입니다.

메타 데이터: 객체에 대한 설명입니다. key:value 형태로 저장됩니다. (마지막으로 수정한 시각 등등)

위 이미지의 각 옵션의 의미는 다음과 같습니다.
본 실습을 따라하는데 꼭 알아야 하는 내용은 아니므로
이해가 안 되면 나중에 와서 다시 보아도 됩니다.

**Keep all versions of an object in the same bucket:** 객체의 버전을 같은 버킷에 저장합니다.
객체를 실수로 삭제하거나, 덮어 썼을 경우에도 이전 버전이 유지되기 때문에 복원이 가능합니다.

**Log requests for access to your bucket:** 로깅용 옵션 입니다.
이 옵션을 켜면 버킷에 접근한 모든 내역이
로그가 남고, 로그가 일정량 모일 때 마다 버킷이 로그 파일을 생성해 버킷 안에 저장합니다.
현재 생성하는 버킷에 해당 로그파일들을 저장할 수도 있고, 로그를 저장할 로그용 버킷을
따로 만들어 그곳에 저장할 수도 있습니다.

**Tags:** 아마존 Resouce(EC2, S3 등등등) 에 붙일 수 있는 태그입니다. 자세한 설명은
본 실습의 범주를 벗어나므로 생략합니다.

**Record object-level API activity using AWS CloudTrail for an additional cost:**
CloudTrail 을 사용해서 오브젝트 레벨 API 활동을 기록할지 여부를 설정합니다.
만약 사용한다면 추가 요금이 부과됩니다. 체크하지 않습니다.

**Automatically encrypt objects when they are stored in S3:**
S3 객체를 자동으로 암호화할지 여부입니다. 퍼블릭 버킷을 만들 것이기 때문에
체크하지 않습니다.

![image-center]({{ site.baseurl }}/assets/images/2019-05-02-s3-6.jpg){: .align-center}
전부 해제한 후 next
{: .text-center }

permission 설정입니다. (recommended) 권장사항이라고 적혀 있지만 일단 모두 해제한 후
다음으로 넘어갑니다. 위 permission 옵션이 모두 체크 되어있다면 버킷을 '공개'(public)로
만들 수가 없습니다. 걱정하지 마세요, 적절한 설정 이후에 필요한 설정은 다시 체크할 것입니다.

![image-center]({{ site.baseurl }}/assets/images/2019-05-02-s3-7.jpg){: .align-center}
리뷰 화면입니다. 하단의 Create bucket 버튼을 눌러서 버킷 생성을 완료합니다.
{: .text-center }

![image-center]({{ site.baseurl }}/assets/images/2019-05-02-s3-7.jpg){: .align-center}
버킷 생성 완료! 
{: .text-center }
이제 버킷의 권한 설정을 할 차례입니다. 목록에서 버킷 이름을 클릭합니다.
![image-center]({{ site.baseurl }}/assets/images/2019-05-02-s3-8.jpg){: .align-center}

## permission 세팅

버킷 이름을 클릭했다면 아래와 같은 화면이 보입니다.

![image-center]({{ site.baseurl }}/assets/images/2019-05-02-s3-9.jpg){: .align-center}
Permissions 클릭 
{: .text-center }

쉽게 설명하자면, S3 Permission 에는 ACL 과 Policy, 2가지의 권한 설정이 존재합니다.
(엄밀히 말하면 User Policy, Resource-based Policy 등등 다양하게 나눌 수 있는데
여기서는 간단하게만 설명하겠습니다.)

ACL: Access Control List 의 약자로, 버켓 주인과 오브젝트 주인이 다를 경우의 권한 설정,
log 저장용 버킷에 대한 권한 설정 등등에 사용하는 것이 권장사항입니다.

Policy: 우리가 사용할 권한 설정입니다. 모든 아마존 S3 권한을 policy 를 통해서 설정할 수 있습니다.


![image-center]({{ site.baseurl }}/assets/images/2019-05-02-s3-10.jpg){: .align-center}
Policy 클릭
{: .text-center }

다음 Json을 붙여넣습니다.
```json
 {
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "AddPerm",
            "Effect": "Allow",
            "Principal": "*",
            "Action": "s3:GetObject",
            "Resource": "arn:aws:s3:::버킷 이름/*"
        }
    ]
}
```
Version 은 policy 양식의 버전을 나타내며, 오늘 날짜 값이 아니니 2012-10-17 그대로 사용합니다.
Action 은 s3 에 대해 수행할 동작을 나타내며 `GetObject` 를 허용했으므로 '읽기'를 허용한 셈입니다.
Principal 은 권한을 얻게 되는 주체를 나타내는데, *(와일드카드) 를 사용했으므로 '모든 이'를 의미합니다.

다 입력했다면 우측의 Save 를 누르고 빠져나옵니다.

![image-center]({{ site.baseurl }}/assets/images/2019-05-02-s3-12.jpg){: .align-center}
버킷 public access 에 대한 경고문이 나왔다면 정상입니다. public 마크가 붙은 것이 보입니다.
{: .text-center}


이제 Public access setting 으로 돌아갑니다.
![image-center]({{ site.baseurl }}/assets/images/2019-05-02-s3-13.jpg){: .align-center}
맨 아래의 체크박스를 제외하고 모두 체크한 후 확인을 누릅니다. confirm 을 요구하는
팝업이 뜨면 손으로 confirm 을 직접 입력하고 확인을 누릅니다.
{: .text-center}

## 테스트

설정은 끝났습니다! 실제로 public access 가 되는지 확인해 봅시다.
아무 이미지나 bucket 에 올려보겠습니다.

![image-center]({{ site.baseurl }}/assets/images/2019-05-02-s3-14.jpg){: .align-center}
upload 버튼을 누르고
{: .text-center}

![image-center]({{ site.baseurl }}/assets/images/2019-05-02-s3-15.jpg){: .align-center}
전 귀여운 강아지 사진인 뭉뭉.jpg 를 올려 보겠습니다. 파일을 업로드 하고 왼쪽 하단의 upload 버튼을 클릭합니다.
{: .text-center}

![image-center]({{ site.baseurl }}/assets/images/2019-05-02-s3-16.jpg){: .align-center}
업로드가 완료되었다면 파일 이름을 클릭하고
{: .text-center}

![image-center]({{ site.baseurl }}/assets/images/2019-05-02-s3-17.jpg){: .align-center}
맨 아래의 Object URL 링크를 복사 한 뒤, 시크릿 탭을 열어서 (AWS 에 로그인 되지 않은 아무 브라우저나
여서도 됩니다.) 링크에 접속하면!
{: .text-center}
 
![image-center]({{ site.baseurl }}/assets/images/2019-05-02-s3-18.jpg){: .align-center}
누구나 이미지를 다운로드 받을 수 있음을 확인할 수 있습니다!
{: .text-center}
 

수고하셨습니다!
다음 글에서는 루트 계정이 아닌 IAM 계정을 사용해서 버킷에 접근하는 방법을 설명하고 
그 다음에는 파이썬 boto3 라이브러리를 사용해 이미지 파일을 업로드 해 보겠습니다.


