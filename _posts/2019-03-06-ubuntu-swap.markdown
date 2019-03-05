---
layout: single
title:  "mysqld.sock 에 연결이 되지 않는 문제"
date:   2019-03-06 00:10:03 +0900
categories: [linux, ubuntu, mysql]
--- 

## 발단

어느날 qa 서버 관리자 페이지가 마비 됬다.
관리자 페이지 html 및 로그인 까지는 잘 되는데 
db 연산이 필요한 부분만 들어가면 뻗어 버리는 것을 발견.


## 조사 1
최근에 관리자 페이지 api 를 손댄 적도 없는데 왜 그럴까?
pycharm 의 database tool 로 qa서버의 mysql에 접속해 보았다.

읭? database tool 에서도 접속이 되지 않는다.(Java IO Error 발생) 슬슬 사태의 심각성을 깨닫게 된다.

정확한 원인파악을 위해 이번엔 ssh 터미널로 들어가 직접 mysql 클라이언트를 실행해보기로 한다.

 

```
$ mysql -p -u root
error: 'Can't connect to local MySQL server through socket '/var/run/mysqld/mysqld.sock'
```

![image-center]({{ site.baseurl }}/assets/images/2019-03-06-wtf.jpg){: .align-center}

**일 났다.**
{: .text-center}

일단 이게 운영서버가 아니라서 참 다행이라는 생각을 했다. 대체 뭐가 문제일까 궁리해 보기 시작한다.
일단 저 .sock 파일. .sock 파일이 socket 파일이라는 건 알고 있는데, mysql 서버가 켜질때, 그리고 port 를 listen 할 때
필요한 파일이라는 것 말고는 구체적으로 어떻게 동작하는지도 몰랐다.

아니 애초에 멀쩡하던 파일이 왜 없어진 걸까

최근에 mysql 설정 관련해서 공부하면서 설정파일들을 이리저리 만져보던 것이 기억이 났다.
문득, "설마 내가 테스트용 서버에 있던 mysql 설정 파일을 덮어 써 버린게 아닐까?" 하는 생각이
뇌리를 스쳤다.

부리나케 해당 서버에 접속해서 my.cnf 파일을 대조해 보았다.
결과는? 내가 그런 황당한 실수를 했었더라면 이 글을 적고 있지도 않았을 것이다.
문제는 다른 곳에 있었다.


## 조사 2

디지털 오션에서 다음 커맨드를 입력해 보라는 글을 찾았다.

```bash
$ tail -30 /var/log/mysql/error.log 
```
tail 커맨드를 사용해서 mysql 의 에러로그 마지막 30줄을 보게 되는데

```
[Note] InnoDB: Initializing buffer pool, total size = 128M, instances = 1, chunk size = 128M
[ERROR] InnoDB: mmap(137428992 bytes) failed; errno 12
[ERROR] InnoDB: Cannot allocate memory for the buffer pool
[ERROR] InnoDB: Plugin initialization aborted with error Generic error
```

그 중 위와 같은 문구가 포함되어 있었다. 본문의 질문자와 증상이 똑같았다.
요는 서버의 **메모리 부족** 이 원인이라는 것이다.

![image-center]({{ site.baseurl }}/assets/images/2019-03-06-out-of-memory.jpg){: .align-center}

어디서 메모리 누수가 일어나는건지... 알아내려면 상당히 많은 시간이 걸릴 것 같았다.

일단 메모리가 문제라는 것은 알았으니 swap 을 사용해서 메모리를 늘리면 되었다.

<a target="_blank" href="{{ site.baseurl }}/linux/ubuntu/ubuntu-swap2/">SWAP 사용하기</a>

## 정리

* mysqld.sock 파일은 mysql 서버가 시작함과 동시에 생성되며, 꺼지면 mysqld 디렉터리 째로 없어진다.




## 참고

다음 링크들이 도움이 많이 되었다.

https://www.digitalocean.com/community/questions/mysql-stopped-and-it-can-t-be-restart

https://stackoverflow.com/questions/11990708/error-cant-connect-to-local-mysql-server-through-socket-var-run-mysqld-mysq

https://www.digitalocean.com/community/tutorials/how-to-add-swap-on-ubuntu-14-04










