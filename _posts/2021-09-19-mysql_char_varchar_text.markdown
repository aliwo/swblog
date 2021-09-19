---
layout: single
title:  "Mysql  Char vs Varchar vs TEXT 언제 쓰는게 좋을까?"
date:   2021-09-19 11:10:03 +0900
categories: [Mysql]
--- 

# Char vs Varchar vs TEXT
언제 쓰는게 좋을까? 직접 테스트 해봤습니다.

# TL; DR

* (mysql8, utfmb4 에서...) 16000자 이하: varchar < 65535자 이하: TEXT (CHAR 는 왜 쓰는지 모르겠음) 
* char 가 varchar 보다 성능이 좋다는 얘기가 있는데, 테스트 해봤을 때 유의미한 차이는 없었습니다.
* varchar 는 저장 공간이 가변이라 disk 낭비가 적으며, index도 됩니다.
* TEXT 는 index 도 안되고 default 값도 안 됩니다만 (^__^) varchar 보다 많이 저장할 수 있습니다. 


# Char
* 고정 길이
* 0~255 까지의 길이를 지정할 수 있습니다. (byte 가 아니라 길이)
* 고정 길이 만큼의 disk space 를 차지합니다. 
* CHAR(10) 에 'abcd' 를 저장하면, 'abcd' 와 함께 빈 6자리를 채우기 위해 6개의 space (padding) 가 뒤에 채워집니다.
* 채워진 스페이스는 해당 row 를 가져올 때 빼고 가져옵니다.
* PAD_CHAR_TO_FULL_LENGTH 설정이 켜져 있다면 빼지 않고 스페이스도 가져옵니다.
* index 가능

# Varchar
* 저장된 문자열 만큼의 disk space 만 차지합니다.
* Char 와 다르게 prefix byte 를 사용합니다. (1~2 byte 남짓을 추가적으로 사용)
* 최대 65535 byte 를 저장합니다. (길이가 아니라 byte) 어떤 character set 을 사용하느냐에 따라 max 길이가 달라집니다.
* 테스트 해보니 (약)16000자가 최대였습니다. (mysql 8.0.25에서 utfmb4 charset 사용)
* index 가능

# Text
* varchar 보다 더 큰 값을 가질 수 있습니다.
* index 불가
* default 값을 가질 수 없습니다. (눈물)
* 테스트 해보니 65535 자를 (길이) 저장할 수 있었습니다. (mysql 8.0.25에서 utfmb4 charset 사용)
* stack overflow 에서 65535 byte 를 저장한다는 글을 많이 볼 수 있었는데, 사실은 byte 가 아니라 글자 수가 65535자 입니다.


# VARCHAR 와 Text 길이 테스트
* python 으로 고정 길이의 문자열을 만듭니다. `'a' * 16125`
* utf8mb4 에서 어떨 때는 16125 보다 긴 컬럼으로 ALTER 할 때 에러 발생, 어떨 때는 16179 보다 길 때 에러 발생... 정확한 기준을 모르겠습니다.
* varchar(16125) 의 경우 정말 `'a' * 16125` 는 할당되지만 `'a' * 16126` 는 할당 안 됬습니다.


# CHAR VS VARCHAR 테스트
애초에 CHAR 의 최대 길이가 255 입니다. 이렇게 작은 값을 read 해 올 때 성능 비교는 의미가 없는 것 같습니다.
500 row 이상을 한 번에 불러오는 경우도 생각해 볼 수 있겠으나... 이건 성능의 문제보다는 pagination 을 안해서
생기는 문제라고 생각합니다.
* CHAR(200) 과 VARCHAR(200) 을 컬럼을 만듭니다.
```
create table string_table
(
  my_char    char(200)      null,
  my_varchar varchar(16179) null,
  my_text    text           null,
  id         int auto_increment
  primary key
);
```
* my_char 에 'a' 200 개로 이루어진 문자열을 저장한 컬럼 250개 생성
* my_carchar 에도 'a' 200 개로 이루어진 문자열을 저장한 컬럼 250개 생성
* 두 쿼리의 성능 비교 
  * `SELECT my_char FROM string_table WHERE my_char IS NOT NULL;`
  * `SELECT my_varchar FROM string_table WHERE my_varchar IS NOT NULL;`

```
> SELECT my_char FROM string_table WHERE my_char IS NOT NULL
[2021-09-18 23:07:11] 250 rows retrieved starting from 1 in 48 ms (execution: 8 ms, fetching: 40 ms)
> SELECT my_char FROM string_table WHERE my_char IS NOT NULL
[2021-09-18 23:07:36] 250 rows retrieved starting from 1 in 77 ms (execution: 8 ms, fetching: 69 ms)
> SELECT my_char FROM string_table WHERE my_char IS NOT NULL
[2021-09-18 23:07:37] 250 rows retrieved starting from 1 in 70 ms (execution: 9 ms, fetching: 61 ms)
> SELECT my_char FROM string_table WHERE my_char IS NOT NULL
[2021-09-18 23:07:38] 250 rows retrieved starting from 1 in 59 ms (execution: 9 ms, fetching: 50 ms)
> SELECT my_varchar FROM string_table WHERE my_varchar IS NOT NULL
[2021-09-18 23:07:51] 252 rows retrieved starting from 1 in 57 ms (execution: 10 ms, fetching: 47 ms)
> SELECT my_varchar FROM string_table WHERE my_varchar IS NOT NULL
[2021-09-18 23:07:52] 252 rows retrieved starting from 1 in 60 ms (execution: 8 ms, fetching: 52 ms)
> SELECT my_varchar FROM string_table WHERE my_varchar IS NOT NULL
[2021-09-18 23:07:53] 252 rows retrieved starting from 1 in 51 ms (execution: 9 ms, fetching: 42 ms)
> SELECT my_varchar FROM string_table WHERE my_varchar IS NOT NULL
[2021-09-18 23:07:54] 252 rows retrieved starting from 1 in 53 ms (execution: 9 ms, fetching: 44 ms)
> SELECT my_varchar FROM string_table WHERE my_varchar IS NOT NULL
[2021-09-18 23:07:54] 252 rows retrieved starting from 1 in 63 ms (execution: 9 ms, fetching: 54 ms)
```

결론: `또이또이`

# Reference

https://stackoverflow.com/questions/25300821/difference-between-varchar-and-text-in-mysql/25301046#25301046

https://dev.mysql.com/doc/refman/8.0/en/char.html







