---
layout: single
title:  "windows 에서 mysql 설정 파일을 찾아 떠나는 여행"
date:   2019-03-03 16:10:03 +0900
categories: [mysql]
--- 

## 도움이 된 글

https://stackoverflow.com/questions/14597884/mysql-my-ini-location

즉, msi 인스톨러를 통해 mysql 을 설치했다면 programdata 폴더 안에 설정파일이 있는 것!


## 현재 server 의 default char set 알아내기
간단하다.
```mysql
SHOW VARIABLES;
```



## windows 에서 mysql 재실행
설정 파일을 바꾸었다면 mysql 을 재실행 해야 바뀐 설정이 적용된다.
![image-center]({{ site.baseurl }}/assets/images/2019-03-04--mysql01.jpg){: .align-center}














