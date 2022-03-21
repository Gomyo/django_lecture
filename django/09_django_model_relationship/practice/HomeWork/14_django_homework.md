# 14_HomeWork

### 1. M:N True or False 

- 각 문항을 읽고 맞으면 T, 틀리면 F를 작성하고 틀렸다면 그 이유도 함께 작성하시오. 

  1) Django에서 1:N 관계는 ForeignKeyField를 사용하고 M:N 관계는 ManyToManyField를 사용한다. 

  - T

  2) ManyToManyField를 설정하고 만들어지는 테이블 이름은 “앱이름_클래스이름_지정한 필드이름”의 형태로 만들어진다. 
  
  - T
  
  3) ManyToManyField의 첫번째 인자는 참조할 모델, 두번째 인자는 related_name이 작성 되는데 두 가지 모두 필수적으로 들어가야 한다.
  
  - F. related_name은 필수 사항은 아니다. 다만 여러 개의 MtoM Field를 쓴다면 매니저가 겹칠 수 있기 때문에 필수가 된다.

### 2. Like in templates

- 아래 빈 칸 (a)와 (b)에 들어갈 코드를 각각 작성하시오.

  ```python
  class Article(models.Model):
      ...
      user = models.ForeighKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
      like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_articles')
  ```

  ```django
  <!-- articles/index.html -->
  
  {% for articlr in articles %}
    ...
    <p>{{ article.title }}</p>
    <a href="{% url 'articles:like' article.pk %}">
  	{% if __(a)__ in __(b)__ %}
        <i class="fas fa-heart fa-lg" style-"color:crimson"></i>
      {% else %}
        <i class="fas fa-heart fa-lg" style-"color:black"></i>
      {% endif %}
    </a>
    <span>{{ __(b)__|length }}명이 이 글을 좋아합니다.</span>
  {% endfor %}
  ```

- a : request.user
- b : article.like_users.all

### 3. Follow in views 

- 모델 정보가 다음과 같을 때 빈칸 (a)와 (b)에 들어갈 코드를 각각 작성하시오.

  ```python
  from django.db import models
  from django.conf import settings
  from django.contrib.auth.models import AbstractUser
  
  class User(AbstractUser):
      followings = modles.ManyToManyField('self', symmetrical=False, related_name='followers')
  ```

  ```python
  app_name = "accounts"
  urlpatterns = [
      ...
      path('<int:user_pk>/follow/', views.follow, name="follow")
  ]
  ```

  ```python
  from django.contrib.auth import get_user_model
  
  
  User = get_user_model()
  
  @require_POST
  def follow(request, __(a)__):
      person = get_object_or_404(User, pk=__(a)__)
      user = request.user
      
      if user != person:
          if person.__(b)__.__(c)__(pk=user.pk).exists():
              person.__(b)__.__(d)__(user)
          else:
              person.__(b)__.__(e)__(user)
      return redirect('accounts:profile', person.username)
  ```

  - a : user_pk
  - b : followers
  - c : filter
  - d : remove
  - e : add



### 4. User AttributeError 

- 아래와 같은 에러 메시지가 발생하는 이유와 이를 해결하기 위한 방법과 코드를 작성하 시오. 

  ![image-20210401081345027](14_HomeWork.assets/image-20210401081345027.png)

- User 클래스를 accounts 어플리케이션에서 처리하라고 넘겨 놓고, 장고 기본 클래스인 auth.User를 사용하는 Form을 사용했을 경우 발생하는 에러이다. auth.User를 사용하는 관련 코드를 모두 커스텀해서 accounts.User를 사용하도록 해야 한다. `settings.AUTH_USER_MODEL` 사용

### 5. related_name 

- 아래의 경우 related_name을 필수적으로 설정해야 한다. 그 이유를 설명하시오. 

  ```python
  class Article(models.Model):
  	user = models.ForeighKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
      like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_articles')
  ```

  - related_name을 설정하지 않으면 users, like_users 둘다 역참조 매니저가 article_set이 되어버린다. 따라서 user 칼럼은 article_set, like_users 칼럼은 User.like_articles로 조회할 수 있도록 분리해 줘야 한다.

### 6. follow templates person 

- 변수에는 view함수에서 넘어온 유저 정보가 담겨 있고, 모델 정보가 아래와 같을 때 빈칸 a, b, c, d, e에 들어갈 알맞은 코드를 각각 작성하시오

  ```python
  app_name = 'accounts'
  urlpatterns = [
      ...
      path('<username>/follow/', views.follow, name="follow")
  ]
  ```

  ```python
  from django.db import models
  from django.contrib.auth.models import AbstractUser
  
  class User(AbstractUser):
      followers = modles.ManyToManyField('self', symmetrical=False, related_name='followings')
  ```

  ```django
  <h1>작성자 : {{ person.username }}</h1>
  
  <div>팔로잉 : {{ __(a)__|length }}</div>
  <div>팔로워 : {{ __(b)__|length }}</div>
  
  <div>    
    {% if __(c)__ != __(d)__ %}
      {% if __(c)__ != __(b)__ %}
        <a href="{% url 'accounts:follow' __(e)__ %}">Unfollow</a>
      {% else %}
        <a href="{% url 'accounts:follow' __(e)__ %}">follow</a>
      {% endif %}
    {% endif %}
  </div>
  
  ```

  - a : person.folloings.all
  - b : person.followers.all
  - c : request.user
  - d : person
  - e : person.username



















