---
layout: single
title:  "swap 을 사용해서 메모리 용량 늘리기"
date:   2019-03-06 00:10:03 +0900
categories: [linux, ubuntu]
--- 

<a target="_blank" href="{{ site.baseurl }}/linux/ubuntu/ubuntu-swap/">mysqld.sock 에 연결이 안되는 문제</a>
에서 이어집니다.

## SWAP ?

swap 은 쉽게 말해서 윈도우의 가상 메모리랑 똑같습니다. 
그걸 리눅스에서는 swap 이라고 부릅니다.

메모리 용량이 항상 쪼들리는 micro 인스턴스를 쓰고 있노라면
가끔씩 mysql 이 어디론가 사라져 버리곤 합니다.
운영체제가 메모리를 확보하기 위해 백그라운드 프로세스를 임의로 꺼버리는데
운 나쁘게 mysql 이 당첨된 경우입니다.

서버는 살아 있는데 db는 꺼져 버렸으니 500 에러가 터지게 됩니다.
당장 메모리를 늘리는 방법이 있지만 (그리고 메모리를 늘리는 것을 권장합니다만)
당장 비용이 부담스럽다면 swap 을 사용하는 방법이 있습니다.

단순한 웹 서버라면 속도 차이도 별로 체감이 안됩니다.

## SWAP 만들기
ubuntu 18을 기준으로 하겠습니다. 본인의 우분투 서버에 SSH로 접속합니다.


`free -h` 명령어를 사용해 현재 swap 이 사용중인지 검사합니다.
```
$ free -h
              total        used        free      shared  buff/cache   available
Mem:           3.6G        2.2G        483M         18M        984M        1.2G
Swap:            0B          0B          0B
```
현재는 swap 을 안 쓰고 있으니 total 0 입니다!


다음은 `df -h` 명령어를 사용해 디스크에 공간이 충분한지 볼까요?
```
# df -h
Filesystem      Size  Used Avail Use% Mounted on
udev            1.8G     0  1.8G   0% /dev
tmpfs           369M   19M  351M   5% /run
/dev/sda1        97G   14G   83G  15% /
tmpfs           1.9G     0  1.9G   0% /dev/shm
tmpfs           5.0M     0  5.0M   0% /run/lock
tmpfs           1.9G     0  1.9G   0% /sys/fs/cgroup
/dev/sda15      105M  3.6M  101M   4% /boot/efi
tmpfs           369M     0  369M   0% /run/user/1002
tmpfs           369M     0  369M   0% /run/user/1001
```
/dev/sda1 에 공간이 충분하다는 것을 확인했습니다~
 

그럼 다음 명령어로 swap 을 만듭니다.
```
$ sudo fallocate -l 1G /swapfile 
```

다음 명령어로 정상적으로 만들어졌는지 확인합니다.
```
$ ls -lh /swapfile
-rw-r--r-- 1 root root 1.0G Oct 24 03:18 /swapfile
```
위처럼 나왔다면 성공!


그럼 만든 swap 파일을 사용해 보겠습니다. 먼저 루트가 사용하도록 swap 파일의 권한을 바꿀게요.
```
$ sudo chmod 600 /swapfile
$ ls -lh /swapfile
-rw------- 1 root root 1.0G Oct 24 03:18 /swapfile
```

그 다음에, marking 과정을 거칩니다. swap 을 사용할 수 있도록 준비한다고 생각하시면 되요. 
```
$ sudo mkswap /swapfile
Setting up swapspace version 1, size = 1024 MiB (1073737728 bytes)
no label, UUID=702b83a7-d6f8-48ca-9e0f-30e6086dea0b
```

실제로 swap 을 사용설정 합니다.
```
$ sudo swapon /swapfile
$ sudo swapon --show
NAME      TYPE  SIZE USED PRIO
/swapfile file 1024M   0B   -2

```


마지막으로 free -h 로 확인해 볼게요~
```
$ free -h
              total        used        free      shared  buff/cache   available
Mem:           3.6G        2.2G        137M         18M        1.3G        1.2G
Swap:          1.0G          0B        1.0G
```

여기까지 따라했다면 완료! 참 쉽죠!





