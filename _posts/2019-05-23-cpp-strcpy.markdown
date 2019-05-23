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

