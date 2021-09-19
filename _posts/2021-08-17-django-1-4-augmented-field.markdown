---
layout: single
title:  "S3에 바로 올라가는 ORM 파일 필드 만들기"
date:   2021-08-07 11:10:03 +0900
categories: [Postgresql, MVCC]
--- 


## Environment
python 2.7.14
Django 1.4 (고대 쟝고)
South 1.0.2
기존 코드를 


## 쟝고에 FileField 는 있는데 왜 S3FileField 는 없을까!!

기존 코드에서는 FileField 를 사용한 뒤, Form 의 save_new() 함수에서 s3 업로드를 진행한 뒤,
S3 경로의 FileField 의 url 을 바꿔치기 하는 방식을 사용하고 있었습니다.

이 방식을 사용했을 때

* 필드가 해야 할 일을 form 이 대신한다.
* column 만 봤을 때는 파일이 s3 에 올라가는지, 로컬(그럴리 없지만)에 저장되는지 알 수 없다.

라는 문제점이 남게 됩니다.

```python
# coding=utf-8
from datetime import datetime

from django.forms.models import BaseInlineFormSet
from util import upload_image_to_s3 # s3 에 파일을 업로드 하는 util 함수
from const import UPLOAD_DIRS # S3 버킷 안의 폴더

class ImageInlineFormset(BaseInlineFormSet):

    def save_new(self, form, commit=True):
        # 기타 여러가지 form set 이 하는 작업들 ...
        
        # + S3 업로드 작업
        obj = super(ImageInlineFormset, self).save_new(form, commit=False)
        image = form.files.get(u'{}-image_url'.format(form.prefix))

        if image:
            filename = u'{:%Y%m%d%H%M%S%f}_{}'.format(
                datetime.now(),
                image.name,
            )
            s3_path = upload_image_to_s3(UPLOAD_DIRS, image, filename)
            obj.image_url = s3_path

        if commit:
            obj.save()

        return obj
```


## S3FileField
그래서 S3FileField 를 만들었습니다~

```python
from datetime import datetime

from django.db.models import FileField
from south.modelsinspector import add_introspection_rules

from utils import upload_image_to_s3


class S3FileField(FileField):

    def __init__(self, *args, **kwargs):
        super(S3FileField, self).__init__(*args, **kwargs)

    def _upload_to_s3(self, image):
        filename = u'{:%Y%m%d%H%M%S%f}_{}'.format(
            datetime.now(),
            image.name,
        )
        return upload_image_to_s3(self.upload_to, image, filename)

    def pre_save(self, model_instance, add):
        file = super(FileField, self).pre_save(model_instance, add)
        if file and not file._committed:
            file.name = self._upload_to_s3(file)
        return file


add_introspection_rules([], ["^dowant\.promotion\.fields\.S3FileField"])

```

* pre_save() 를 override 합니다. 여기서 s3 에 업로드 합니다.
* add_introspection_rules 를 추가해야 마이그레이션 파일이 만들어집니다.


## 사용
필드를 만든 후에는 일반 FileField 처럼 사용하면 됩니다.
```python
    image = S3FileField(
        max_length=300,
        upload_to='s3-버킷-안의-폴더/',
        storage=FileSystemStorage(location='', base_url='https://s3-bucket-경로'),
    )
```




