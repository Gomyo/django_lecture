# 08_Homework

## 1. Django User Model 
django에서 기본적으로 사용하는 User 모델은 아래의 경로에서 찾아볼 수 있다.

```python
from django.contrib.auth.models import User
```

1) 아래의 Django 공식 저장소에서 User 모델이 정의된 코드를 찾아 작성하시오. https://github.com/django/django

```python
class User(AbstractUser):
    """
    Users within the Django authentication system are represented by this
    model.
    Username and password are required. Other fields are optional.
    """
    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'
```

User는 AbstractUser를 상속받아 사용한다.

AbstractUser 클래스에는 first_name, last_name, email 등의 model field가 있으며 forms.py에서 get_user_model() 메소드로 활성화된 User를 가져올 때, 원하는 model field를 선택하여 커스터마이징한다.

## 2. Create user by ModelForm 

기본 User 모델의 정보를 생성하기 위하여 Django 내부에 정의된 ModelForm을
불러오는 import 구문을 작성하시오.

```python
from django.contrib.auth.forms import UserCreationForm
```



## 3. Django view decorators
views.py에 정의된 함수를 post 요청에 대해서만 실행하게 하기 위하여 추가하는
require_POST 함수를 불러오는 import 구문을 작성하시오.

```python
from django.views.decorators.http import require_POST
```