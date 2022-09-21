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

```SQL
create user reboot with password 'reboot';
alter role reboot set client_encoding to 'utf-8';
alter role reboot set timezone to 'Asia/Seoul';
drop database reboot;
create database reboot;
grant all privileges on database reboot to reboot;
```

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

잘 안될 경우 `drop databese reboot` 로 db 삭제 후 다시 만들어서 시도해보자.

```bash
# POST using JSON
http --json POST http://127.0.0.1:8000/apart/ name="빛가람코오롱"
## https://www.django-rest-framework.org/tutorial/2-requests-and-responses/
```

## Views

django-rest-framework 의 가장 최적화된 코드는 다음과 같다.

```python
# views.py
from rest_framework import generics

from rec.models import *
from rec.serializers import *

# (중요) queryset, serializer_class 로 변수명을 고정시켜야 한다. 내부적으로 저 변수명을 호출하는 듯 하다
class ApartmentsList(generics.ListCreateAPIView):
    queryset = Apartments.objects.all()
    serializer_class  = ApartmentsSerializer

class ApartmentstDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Apartments.objects.all()
    serializer_class  = ApartmentsSerializer
```


## scheduler 만들기

```python
pip install schedule

# scheduler.py

import schedule
import time

def job():
    print("I'm working...")

schedule.every(10).seconds.do(job)
schedule.every(10).minutes.do(job)
schedule.every().hour.do(job)
schedule.every().day.at("10:30").do(job)
schedule.every(5).to(10).minutes.do(job)
schedule.every().monday.do(job)
schedule.every().wednesday.at("13:15").do(job)
schedule.every().minute.at(":17").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
```

## 매매가 저장

```python
from rec.models import *
from rec.serializers import *

# params
apart_id = 1
price = 1300

# 매매가 저장
apart = Apartments.objects.get(id=apart_id)
price = PriceInfo(apart=apart, price=price)
price.save()

# 데이터 확인
serializer = PriceInfoSerializer(price)
serializer.data
```

저널리스트 - 기사(아티클)
1 : N
