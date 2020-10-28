---
layout: single
title:  "벤치마크를 믿지 마라! 를 읽고"
date:   2020-10-28 11:10:03 +0900
categories: [python3, benchmark, gunicorn, flask, sanic, bottle]
--- 

## 블로그 글
https://blog.miguelgrinberg.com/post/ignore-all-web-performance-benchmarks-including-this-one


## 단상
파이썬이 가지고 있는 가장 큰 컴플렉스중 하나는 "느려" 인 것 같다.

![image-center]({{ site.baseurl }}/assets/images/2020-10-28-osoi.jpg){: .align-center}


근데 실제로 백엔드 개발 할 때 느리고 빠르다는 어떻게 알까?
직접 테스트 해보지 않고 어떤 서버 + 어플리케이션 조합이 빠를지 어떻게 알 수 있을까?
이런 고민을 해결하려고 한창 파이썬 프레임워크들의 벤치마크를 찾아서 돌아다니던 시절이 있었다.

우연히 어디선가 cherrypy 가 nginx 보다 빠르다는 글을 읽고 cherrypy 를 적용했던 적이 있다.
결과는? 사실 성능이 다가 아니라는 걸 알게 됬다. 전에 nginx, uwsgi 등등을 썼던 때에는 이런 일이 한
번도 없었는데, cherrypy 를 쓰니까 갑자기 알 수 없는 이유로 서버가 뻗는 경우가 가끔 있었다.

위 글을 읽고 다시 한 번 "벤치마크가 다가 아니구나" 를 깨닫게 되었다. 그리고 한 가지 더,
"결국 성능은 자기 앱으로 측정해 보아야 한다." 라는 교훈을 얻었다.



 
