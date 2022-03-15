# 09_HomeWork

### 1. User Model BooleanField

- django에서 기본적으로 사용하는 User 모델은 AbstractUser 모델을 상속받아 정의된다. 

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

  1) 아래의 models.py를 참고하여 User 모델에서 사용할 수 있는 칼럼 중 BooleanField 로 정의 된 칼럼을 모두 작성하시오.

   https://github.com/django/django/blob/master/django/contrib/auth/models.py

```
if_staff : admin site에 login 할 수 있는지
is_active : active한 상태인지. 계정 삭제 대신에 이것을 비활성화한다.
is_superuser
	In PermissionsMixin class
```



### 2. username max length

-  django에 기본적으로 사용하는 User 모델의 username 컬럼이 저장할 수 있는 최대 길 이를 작성하시오.

```
150
```



### 3. login validation 

- 단순히 사용자가 로그인 된 사용자인지만을 확인하기 위하여 User 모델 내부에 정의된 속성의 이름을 작성하시오.

```
is_authenticated
```



### 4. Login 기능 구현

- 다음은 로그인 기능을 구현한 코드이다. 빈 칸에 들어갈 코드를 작성하시오

  ```python
  from django.contrib.auth.forms import __(a)__
  from django.contrib.auth import __(b)__ as auth_login
  
  
  def login(request):
      if request.method == 'POST':
          form = __(a)__(request, request.POST)
          if form.is_valid():
              auth_login(request, __(c)__)
             	return redirect('accounts:index')
  	else:
          form = __(a)__()
      context = {
          'form': form
      }
      return render(request, 'accounts/login.html', context)
  ```

  ```
  a : AuthenticationForm
  b : login
  ```
  
  

### 5.  who are you?

- 로그인을 하지 않았을 경우 template에서 user 변수를 출력했을 때 나오는 클래스의 이름을 작성하시오.

```
AnonymousUser
```



### 6. 암호화 알고리즘

- Django에서 기본적으로 User 객체의 password 저장에 사용하는 알고리즘, 그리고 함께 사용된 해시 함수를 작성하시오.

```python
1. password 저장에 사용하는 알고리즘은 기본적으로 SHA256 해시를 사용하는 PBKDF2 알고리즘을 사용한다. (NIST 권장사항) 저장되는 포맷은 <algorithm>$<iterations>$<salt>$<hash> 이다.

2. 사용되는 해시 함수는 아래와 같다.
def get_hasher(algorithm='default')
algorithm이 default이면 hasher도 default를 리턴한다.
```

PBKDF2 이외에도 2015년 Password Hashing Competition의 우승자 Argon2와 bcrypt도 지원한다.(PBKDF2SHA1)

- `PBKDF2`
  - Hash container algorithm
  - 입력한 암호 기반으로 salt를 정해진 횟수(iterations)만큼 hash 함수 수행

- `SHA256`

  - 특정 입력값에 대해 항상 같은 값을 리턴

  **취약점**

  1. 레인보우 어택 취약
  2. 무차별 대입공격 취약

  **보완점**

  1. salting(레인보우 어택 방어)
     - 임의의 문자열을 추가하여 다이제스트 생성
     - 같은 패승워드라도 각각 다른 salt가 들어가 다이제스트가 다르게 만들어짐
  2. key stretching (무차별 대입공격 방어)
     - 해시 함수를 여러번 반복
     - 즉, 생성된 다이제스트를 입력값으로 다시 다이제스트를 생성. 이를 반복

### 7. Logout 기능 구현

- 로그아웃 기능을 구현하기 위하여 다음과 같이 코드를 작성하였다. 로그아웃 기능을 실행 시 문제가 발생한다고 할 때 그 이유와 해결 방법을 작성하시오

  ```python
  def logout(request):
      logout(request)
      return redirect('accounts:login')
  ```

  - 4번 문제에서 login 메소드를 auth_login으로 바꿔서 사용한 이유와 같다. logout을 그대로 사용하면 재귀함수가 되어 버리기 때문에, 함수명은 그대로 두고 logout을 auth_logout 과 같이 변경해서 작성해야 한다.

