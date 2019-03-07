---
title:  "async 와 await"
date:   2019-03-05 20:21:03 +0900
---

**주의:** 본 수업은 파이썬 3.7 버전 이상을 필요로 합니다.
{: .notice--info}


## async 맞보기

파이썬 쓰레드를 잠시 중단시키기 위해 time.sleep() 을 사용해 본 경험이 있을 것이다.

{% highlight python %}
import time

def print_now():
    print(f"{time.strftime('%X')}")

print_now() # 16:12:18
time.sleep(1)
print_now() # 16:12:19 , 1초 지났다.

{% endhighlight %}

지금 다시 time.sleep() 에 대한 이야기를 하려는 것은 아니다.
우리에게 친숙한 time.sleep() 과 같은 역할을 하는 asyncio.sleep() 을 시작으로 
파이썬 3.7부터 도입된 새로운 비동기 시스템에 대해서 소개하고자 한다.

다음 코드에서 `await asyncio.sleep(1)` 도 `time.sleep(1)` 같은 역할을 한다.

{% highlight python %}
import asyncio
import time


def print_now():
    print(f"{time.strftime('%X')}")


async def main():
    print_now() # 16:12:18
    await asyncio.sleep(1)
    print_now() # 16:12:19

asyncio.run(main())
{% endhighlight %}

모르는 키워드가 2개 나왔다. async 과 await 이다. 이번 수업의 주제이다.
async 와 await 의 자세한 작동방식을 파악하기 전에, 위 코드를 읽고 추측할 수 있는 내용 먼저
정리하도록 하자.

우선 `async def` 는 다음과 같은 의미이다.

"이 함수는 비동기로 실행되는 함수 입니다" 
{: .text-center}
 
yield 가 포함된 제너레이터 함수가 함수의 호출 당시에 실행되지 않는다는 것을 알고 있을 것이다.
(모른다면 <a href="{{ site.baseurl }}/series/principles_of_python/generator/" target="_blank">
generator</a> 부터 공부하고 오도록 하자.)

async 함수도 이와 마찬가지로, async 함수를 호출하면 함수가 바로 실행되는 것이 아니라,
함수로부터 "코루틴 객체(coroutine object)"을 넘겨받게 된다.

{% highlight python %}
>>> main()
<coroutine object main at 0x1053bb7c8>
{% endhighlight %}

코루틴 객체를 리턴하는 함수 (async 키워드가 달려있는 함수) 를 코루틴(coroutine) 이라고 부른다.

지금은 함수 하나만 실행하고 있기 때문에 비동기인지 아닌지 알 수 없지만 
실제 비동기로 처리하는 건 이따가 해 보도록 하자.  

`await` 은 async 함수 내부에서 사용하는 키워드 이며 (async 함수 바깥에서 사용하면 에러가 난다.)
해당 함수 내부에서 비동기로 실행해야 할 부분을 의미한다.

제너레이터 함수에서 `yield` 구문을 만나면 함수 작동은 중지되고 함수 바깥으로 yield 값을 
가지고 빠져나가는 것을 기억하는가? `await` 이 코루틴 내부에서 `yield` 와 같은 기능을 한다.
코루틴을 실행 도중 await 구문을 만나면 await 구문을 실행 한 뒤, 다른 쓰레드로 실행 권한을 넘긴다.
 
따라서 `await asyncio.sleep()` 으로 한 쓰레드가 잠들어 있는 동안, 파이썬은 다른 함수를 실행할 수 있게 된다.


## async 와 await 으로 동시에 2개의 함수 실행하기 

이제는 직접 함수를 2번 실행해서, 진짜 두 함수가 비동기로 동시에 시작하는지를 테스트 해보도록 하자.
아래 예제는 파이썬 3 공식 문서에서 가져왔다. **참고** 란에 링크를 걸어 두었다.

먼저 비동기가 아니라 **순차적으로** 실행되는 예제를 살펴보자.

{% highlight python %}
import asyncio
import time

async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)

async def main():
    print(f"started at {time.strftime('%X')}")

    await say_after(1, 'hello')
    await say_after(2, 'world')

    print(f"finished at {time.strftime('%X')}")

asyncio.run(main())
{% endhighlight %}

위 함수의 실행결과이다.
```
started at 17:05:24
hello
world
finished at 17:05:27
```
파이썬이 실행된 후 1초 후에 hello 가 출력되고, 2초 후에 world 가 실행되었다.
즉, 다음과 같이 실행 된 것이다.

<svg xmlns="http://www.w3.org/2000/svg" style="background-color: unset; width:100%;" xmlns:xlink="http://www.w3.org/1999/xlink" version="1.1" width="671px" height="61px" viewBox="-0.5 -0.5 671 61" content="&lt;mxfile modified=&quot;2019-03-05T08:18:57.651Z&quot; host=&quot;www.draw.io&quot; agent=&quot;Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:65.0) Gecko/20100101 Firefox/65.0&quot; etag=&quot;O91O7wUj55LtDvSb-79d&quot; version=&quot;10.3.2&quot; type=&quot;device&quot;&gt;&lt;diagram id=&quot;foitgb0iSrcng9kuBp8v&quot; name=&quot;Page-1&quot;&gt;5Vddb9sgFP01SNvDphhsx350HHd7mVYpmtbtZUI2sb0Rk2Hy1V8/MBB/JUrXVV3UWpHCPVwu3HuOAQMUr/YfOF4Xn1hGKICTbA/QHEDoTFwo/xRy0IjnhxrIeZkZpxZYlPfEjjTopsxI3XMUjFFRrvtgyqqKpKKHYc7Zru+2ZLQ/6xrnZAQsUkzH6NcyE4VGAzht8Y+kzAs7s2PzW2HrbDKpC5yxXQdCCUAxZ0zo1mofE6qKZ+uix92c6T0ujJNKPGRA+DP7XrvR4fOXhN3mBdzfLzbvAh1li+nGJAygT2W82ZLJsKqulPGmx/+9UUudAYhumqcL+Xnzn8xBEKtfEoNwDmauagRzEMUyVNOegchVbqEPgtDOJRetpzNhdL3EwZLA2abKiMrDkd27ohRkscap6t1J2UmsECtqupclpfFx1ciBUTTzJF4Lzn4R21Oxihyn2hIuyP5sXZ0jW1LmhK2I4AfpYgdMDcFG4TA09q7Vi2NFUHS04hsMG4nmx9Ati7JhiPwLUsMRqTU+/MBLQfgbmYvmAoJgAsKgkPGYtcK3T1r6JPB8+f6fKb1ivOO8bJ6noQR56MoosdvZSU7ggJMd43KXemGceO61vSaO88SbXwwiyZkHErnJIbULvoTtbQqvjjd4grdBSUmVRer0l1ZKcV2Xab+KZF+Ku077m2xP3nvGmqvcJ9Y4WKOSq7/rGp1RymyHNZYdpxdHstFFY0CBTIBteEouH9cC85yISyfAmNIOZd4JxizGCcWi3PaXe4pGM8MtK5vX5cyB6MKBEnSaZlT3xjIIBAfSQ9NBIF2HUaBGVce0/0Fo7qsVWvhAoTkT8B+V5oYDgaBHKm10OAXPrDTv1SrN3owuS+3MOfU8UvMHV0rkhI+Tmj/Q7OicfLTUpNl+TWr39pscJX8A&lt;/diagram&gt;&lt;/mxfile&gt;"><defs/><g><rect x="0" y="0" width="120" height="60" rx="9" ry="9" fill="#12aab5" stroke="none" pointer-events="none"/><g transform="translate(28.5,21.5)"><switch><foreignObject style="overflow:visible;" pointer-events="all" width="63" height="12" requiredFeatures="http://www.w3.org/TR/SVG11/feature#Extensibility"><div xmlns="http://www.w3.org/1999/xhtml" style="display: inline-block; font-size: 12px; font-family: Helvetica; color: rgb(0, 0, 0); line-height: 1.2; vertical-align: top; width: 64px; white-space: nowrap; overflow-wrap: normal; text-align: center;"><div xmlns="http://www.w3.org/1999/xhtml" style="display:inline-block;text-align:inherit;text-decoration:inherit;"><font color="#FFFFFF">파이썬 실행</font></div></div></foreignObject><text x="32" y="12" fill="#000000" text-anchor="middle" font-size="12px" font-family="Helvetica">[Not supported by viewer]</text></switch></g><rect x="183" y="0" width="120" height="60" rx="9" ry="9" fill="#e85642" stroke="none" pointer-events="none"/><g transform="translate(193.5,21.5)"><switch><foreignObject style="overflow:visible;" pointer-events="all" width="98" height="12" requiredFeatures="http://www.w3.org/TR/SVG11/feature#Extensibility"><div xmlns="http://www.w3.org/1999/xhtml" style="display: inline-block; font-size: 12px; font-family: Helvetica; color: rgb(255, 255, 255); line-height: 1.2; vertical-align: top; width: 99px; white-space: nowrap; overflow-wrap: normal; text-align: center;"><div xmlns="http://www.w3.org/1999/xhtml" style="display:inline-block;text-align:inherit;text-decoration:inherit;">say_after(1, ‘hello’)</div></div></foreignObject><text x="49" y="12" fill="#ffffff" text-anchor="middle" font-size="12px" font-family="Helvetica">say_after(1, ‘hello’)</text></switch></g><rect x="370" y="0" width="120" height="60" rx="9" ry="9" fill="#e85642" stroke="none" pointer-events="none"/><g transform="translate(378.5,21.5)"><switch><foreignObject style="overflow:visible;" pointer-events="all" width="102" height="12" requiredFeatures="http://www.w3.org/TR/SVG11/feature#Extensibility"><div xmlns="http://www.w3.org/1999/xhtml" style="display: inline-block; font-size: 12px; font-family: Helvetica; color: rgb(255, 255, 255); line-height: 1.2; vertical-align: top; width: 103px; white-space: nowrap; overflow-wrap: normal; text-align: center;"><div xmlns="http://www.w3.org/1999/xhtml" style="display:inline-block;text-align:inherit;text-decoration:inherit;">say_after(2, ‘world’)</div></div></foreignObject><text x="51" y="12" fill="#ffffff" text-anchor="middle" font-size="12px" font-family="Helvetica">say_after(2, ‘world’)</text></switch></g><rect x="550" y="0" width="120" height="60" rx="9" ry="9" fill="#12aab5" stroke="none" pointer-events="none"/><g transform="translate(597.5,21.5)"><switch><foreignObject style="overflow:visible;" pointer-events="all" width="24" height="12" requiredFeatures="http://www.w3.org/TR/SVG11/feature#Extensibility"><div xmlns="http://www.w3.org/1999/xhtml" style="display: inline-block; font-size: 12px; font-family: Helvetica; color: rgb(0, 0, 0); line-height: 1.2; vertical-align: top; width: 25px; white-space: nowrap; overflow-wrap: normal; text-align: center;"><div xmlns="http://www.w3.org/1999/xhtml" style="display:inline-block;text-align:inherit;text-decoration:inherit;"><font color="#FFFFFF">종료</font></div></div></foreignObject><text x="12" y="12" fill="#000000" text-anchor="middle" font-size="12px" font-family="Helvetica">[Not supported by viewer]</text></switch></g><path d="M 120 30 L 176.63 30" fill="none" stroke="#000000" stroke-miterlimit="10" pointer-events="none"/><path d="M 181.88 30 L 174.88 33.5 L 176.63 30 L 174.88 26.5 Z" fill="#000000" stroke="#000000" stroke-miterlimit="10" pointer-events="none"/><path d="M 303 30 L 363.63 30" fill="none" stroke="#000000" stroke-miterlimit="10" pointer-events="none"/><path d="M 368.88 30 L 361.88 33.5 L 363.63 30 L 361.88 26.5 Z" fill="#000000" stroke="#000000" stroke-miterlimit="10" pointer-events="none"/><path d="M 490 30 L 543.63 30" fill="none" stroke="#000000" stroke-miterlimit="10" pointer-events="none"/><path d="M 548.88 30 L 541.88 33.5 L 543.63 30 L 541.88 26.5 Z" fill="#000000" stroke="#000000" stroke-miterlimit="10" pointer-events="none"/></g></svg>

이제부터 main() 함수 내부를 바꿔서 비동기 동시 실행으로 바꿔 보자.

{% highlight python %}
async def main():
    task1 = asyncio.create_task(
        say_after(1, 'hello'))

    task2 = asyncio.create_task(
        say_after(2, 'world'))

    print(f"started at {time.strftime('%X')}")

    # Wait until both tasks are completed (should take
    # around 2 seconds.)
    await task1
    await task2

    print(f"finished at {time.strftime('%X')}")
{% endhighlight %}

`asyncio.create_task()` 는 코루틴 객체를 인자로 받아서 task 객체로 감싸주는 역할을 한다.
코루틴을 await 했을 시 함수가 종료되기 까지 기다렸지만
task 를 await 했을 시에는 함수의 종료를 기다리지 않고 넘어간다.


## return 받기

say_after 를 조금 수정해서
return_after 로 바꿔서 실험해 보자.

{% highlight python %}
import asyncio
import time

async def return_after(delay, what):
    await asyncio.sleep(delay)
    return what

async def main():
    print(f"started at {time.strftime('%X')}")

    print(await return_after(1, 'hello'))
    print(await return_after(2, 'world')) 

    print(f"finished at {time.strftime('%X')}")

asyncio.run(main())
{% endhighlight %}

결과값:
```
started at 10:51:16
hello
world
finished at 10:51:19
```

일반 함수를 실행한 것 처럼 바로 결과값을 받아볼 수 있었다. task 도 
비슷하게 사용한다.
{% highlight python %}
async def main():

    task1 = asyncio.create_task(
        return_after(1, 'hello'))

    task2 = asyncio.create_task(
        return_after(2, 'world'))

    print(f"started at {time.strftime('%X')}")

    print(await task1)
    print(await task2)

    print(f"finished at {time.strftime('%X')}")
{% endhighlight %}

결과값:
```
started at 10:56:39
hello
world
finished at 10:56:41
```


## awaitable
코루틴과 테스트 그리고 조금 있다 배우게 될 퓨처, 이 세 가지를 모두 `awaitable` 이라고 한다.
해당 객체에 await 키워드를 사용할 수 있다는 뜻이다.



## 정리

* 코루틴 객체를 리턴하는 함수 (async 키워드가 달려있는 함수) 를 코루틴(coroutine) 이라고 부른다.

## 참고

https://docs.python.org/ko/3/library/asyncio-task.html












