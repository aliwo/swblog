---
layout: single
title:  "kubeadm token 조회와 사용하기"
date:   2020-08-07 12:10:03 +0900
categories: [kubernetes]
---

## token을 다시 조회하는 방법
처음에 `kubeadm init` 을 성공하면 해당 클러스터에 join 할 수 있는
토큰을 얻을 수 있다.
```
kubeadm join 192.168.56.2:6443 --token z7md1g.7bxgzhnwsiacs43e \
    --discovery-token-ca-cert-hash sha256:6db8bffc719fa7978ced52217596a3a9bd4de0ffb80517cc4dd0689cc907054d
```

이 토큰을 다시 조회하려면...
```
kubeadm token list
``` 
 
`discovery-token-ca-cert-hash` 를 다시 조회하려면...
```
openssl x509 -pubkey -in /etc/kubernetes/pki/ca.crt | openssl rsa -pubin -outform der 2>/dev/null | openssl dgst -sha256 -hex | sed 's/^.* //'
```




