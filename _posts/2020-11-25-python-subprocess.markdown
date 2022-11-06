---
layout: single
title:  "python 디렉터리 안의 모든 영상 길이 sum 하기"
date:   2020-11-25 11:10:03 +0900
categories: [Python, Aws]
--- 


## 목적

하나의 디렉터리 안에 수 많은 폴더들이 있고
그 안에 .mov 파일들이 들어 있습니다.
이 영상들의 총 길이를 알아내고 싶다면 어떻게 해야 할까요?


## Environment
* macOS Catalina
* python 3.8
* brew 가 깔려 있는 상태


## 사전 준비

```
brew install ffmpeg
```

## ffmpeg 의 사용법
<a href="https://stackoverflow.com/questions/6239350/how-to-extract-duration-time-from-ffmpeg-output" target="_blank">
https://stackoverflow.com/questions/6239350/how-to-extract-duration-time-from-ffmpeg-output</a>

```
ffmpeg -i file.mp4 2>&1 | grep Duration | awk '{print $2}' | tr -d ,
```

file.mp4 의 자리에 원하는 파일의 경로를 넣으면 파일의 재생시간이 깔끔하게 출력됩니다.


## 전체 코드

바로 복사해서 쓰시면 됩니다.

```python
import glob
import subprocess
from datetime import timedelta, datetime

lengths = []


def get_length(filename):
    ffmpeg = subprocess.Popen(
        ['ffmpeg', '-i', filename],
        stderr=subprocess.PIPE
    )
    grep = subprocess.Popen(
        ['grep', 'Duration'],
        stdin=ffmpeg.stderr,
        stdout=subprocess.PIPE
    )
    awk = subprocess.Popen(
        ['awk', "{print $2}"],
        stdin=grep.stdout,
        stdout=subprocess.PIPE
    )
    trim = subprocess.Popen(
        ['tr', '-d', ','],
        stdin=awk.stdout,
        stdout=subprocess.PIPE
    )
    for line in trim.stdout:
        # 딱 첫 번째 줄만 출력.
        return line.decode('utf-8')

# root_dir needs a trailing slash (i.e. /root/dir/)
for filename in glob.iglob('/영상이 들어있는 폴더 경로/' + '**/*.mov', recursive=True):
     lengths.append(get_length(filename))


# 시간 parse
deltas = []
for elem in lengths:
    datetime = datetime.strptime(elem[:-4], '%H:%M:%S')
    delta = timedelta(hours=datetime.hour, minutes=datetime.minute, seconds=datetime.second)
    deltas.append(delta)

# sum
print(sum(deltas, timedelta(0)))

```

`ffmpeg -i` 를 실행하면 딱 "재생시간" 만 나오면 정말 좋겠지만, 당장 필요없는 정보도 많이 나옵니다.
심지어 stdout 이 아니라 stderr 로 출력을 하죠... (황당)
그래서 딱 "재생시간"만 뽑아내기 위해 후처리를 합니다. 

```
ffmpeg -i file.mp4 2>&1 | grep Duration | awk '{print $2}' | tr -d ,
```

