---
layout: single
title:  "초간단! c++ string 입력을 char 배열로 바꾸기"
date:   2019-05-23 20:10:03 +0900
categories: [c++]
--- 

## Input 받기
까먹을 까봐 적어 놓습니다.

{% highlight c++ %}

        //주의!  temp 의 길이가 10이라는 걸 알고 있을 때만 사용!
        char board[10];
        string temp;
        cin>>temp;
        strcpy(board, temp.c_str());
{% endhighlight %}

## 이중 배열 인자로 넘기기
한글로 검색해 보면 장황한 글 말고는 검색이 쉽지 않네요.
그래서 한 번에 이해되는 명료한 
<a href="https://stackoverflow.com/questions/8767166/passing-a-2d-array-to-a-c-function" target="_blank">
스택 오버플로</a> 글을 가져왔습니다. 

