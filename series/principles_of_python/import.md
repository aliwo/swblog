---
title:  "니 것도 내꺼 내 것도 내꺼"
date:   2019-01-18 20:21:03 +0900
---

<h2>Wifi 가져 오기</h2>
때는 2011년. 여러분은 새로 출시된 따끈따끈한 갤럭시 s2를 사 들고 
즐거운 마음으로 집에 돌아왔다. 이제 막 핸드폰만 사 들고 온지라 여러분의 갤럭시는 아직 개통이 되지 않은 상태다.
핸드폰 가게의 말 대로라면 내일은 되야 개통이 된다늠 오양이다.
따라서 현재 셀룰러 데이터는 사용할 수 없다. 그러나 실망하기에는 이르다.
여러분의 최신형 스마트폰 갤럭시 s2는 wifi로 인터넷에 연결할 수 있다. 
그런데 아뿔싸. 여러분의 집엔 무선 공유기가 없다는 것을 깨닫고 만다.
```python
# my_home.py
class GalaxyS2:
    
    def connect(self, wifi):
        if not wifi:
            raise ConnectionError
        print('인터넷이 연결 되었습니다.') 

my_galaxy = GalaxyS2()
my_galaxy.connect() # 우리집엔 Wifi가 없다!
```

<br>

다급해진 여러분은 급한대로 없는 와이파이라도 연결해 보려고 한다.
아래 코드를 실행해보자.
```python
# my_home.py
class GalaxyS2:
    
    def connect(self, wifi):
        if not wifi:
            raise ConnectionError
        print('인터넷이 연결 되었습니다.') 

my_galaxy = GalaxyS2()
my_galaxy.connect(wifi) # Name Error 발생!! 
```

새로 산 galaxy s2 를 가지고 놀지 못한다는 사실에 망연자실해 있던 여러분에게 한가지 생각이 뇌리에 스친다.
옆 집에서 wifi를 가져다 쓰는 것이다.
```python
# neighbor_home.py
class Wifi:
    pass

wifi = Wifi()
```

우리 집 (my_home.py) 에서 옆 집(neighbor_home.py) 를 실행 하려면 import 키워드를 사용한다.
여기서는 neighbor_home.py 가 가지고 있는 wifi 를 가져오고 싶으므로 from neighbor_home import wifi
라고 입력하면 된다.
```python
# my_home.py
from neighbor_home import wifi

class GalaxyS2:
    
    def connect(self, wifi):
        if not wifi:
            raise ConnectionError
        # 인터넷 연결 ... 

my_galaxy = GalaxyS2()
my_galaxy.connect(wifi)
```