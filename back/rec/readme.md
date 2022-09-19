# 부동산 가격 알림봇

## venv

```bash
# from git bash
source ./back/venv/Scripts/activate
```

## 확인 방법

`python manage.py shell`

```bash

from rec.models import *        
from rec.serializers import *       
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

apart = Apartments(name="부영 1차")
apart.save()

serializer = ApartmentsSerializer(apart)   
serializer.data
# {'id': 2, 'name': '부영 1차'}

# 파이썬 네이티브 데이터 모델로 변환(serialization)
content = JSONRenderer().render(serializer.data) 
content
# b'{"id":2,"name":"\xeb\xb6\x80\xec\x98\x81 1\xec\xb0\xa8"}'

# Deserialization 
import io
stream = io.BytesIO(content)
data = JSONParser().parse(stream)
data
# {'id': 2, 'name': '부영 1차'}

serializer = ApartmentsSerializer(data=data)
serializer.is_valid()
serializer.validated_data
serializer.save()

# 저장된 전체 데이터 확인
serializer = ApartmentsSerializer(Apartments.objects.all(), many=True)
serializer.data
```

## db 생성

create database rec;

## postgresql 계정 생성 및 권한 설정

create user reboot with password 'reboot';
alter role reboot set client_encoding to 'utf-8';
alter role reboot set timezone to 'Asia/Seoul';
grant all privileges on database rec to reboot;

## migrate

python manage.py makemigrations
python manage.py migrate

성공 시 아래와 같이 뜬다.

```bash
$ python manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, rec, sessions, snippets
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying auth.0012_alter_user_first_name_max_length... OK
  Applying rec.0001_initial... OK
  Applying rec.0002_apartlist_priceinfo_delete_rec... OK
  Applying rec.0003_priceinfo_price... OK
  Applying rec.0004_rename_apartlist_apartments... OK
  Applying sessions.0001_initial... OK
  Applying snippets.0001_initial... OK
  Applying snippets.0002_alter_snippet_language... OK
  Applying snippets.0003_alter_snippet_language_alter_snippet_style... OK
(venv) 
```

잘 안될 경우 `drop databese rec` 로 db 삭제 후 다시 만들어서 시도해보자.
