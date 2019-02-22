---
title:  "Let's start Flask!" 
date:   2019-01-26 20:21:03 +0900
---


## flask 의 설치

가상환경에서 pip 를 사용해 flask 를 설치한다.
터미널에 다음 커맨드를 입력하자.
```markdown
pip install flask
```

## minimal flask application

{% highlight python %}

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()

from flask import Flask

{% endhighlight %}



















