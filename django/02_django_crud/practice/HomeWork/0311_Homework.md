# 0311_Homework

## ❖ Django Model 

posts 앱 안의 models.py 파일에 다음과 같은 코드를 작성하였다.

```python
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
```

1) models.py를 작성한 후 마이그레이션 작업을 위해 터미널에 작성해야 하는 두 개의 명령어를 작성하시오.

```shell
$ python manage.py makemigrations
$ python manage.py migrate
```

2) 다음 중 새로운 Post를 저장하기 위하여 작성한 코드 중 옳지 않은 것을 고르시오.

```python
# 1
post = Post()
post.title = 'a'
post.content = 'b'
post.save

# 2
post = Post(title='a' content='b')
post.save()

# 3
post = Post('title', 'content')
post.save()

#4
Post.objects.create(title='a', content='b')
```

```
3번이 안된다.
```

3) Post가 10개 저장되어 있고 id의 값이 1부터 10까지라고 가정할 때 가장 첫 번째 Post를 가져오려고 한다. 다음 중 옳지 않은 코드를 고르시오.

```python
#1
post1 = Post.objects.all()[0]
#2
post2 = Post.objects.all()[-10]
#3
post3 = Post.objects.all().first()
#4
post4 = Post.objects.all().get(id=1)
```

```shell
2번이 안된다. 리스트처럼 보이지만 all()의 리턴값은 querySet이기 때문이다.
리스트의 negative index 접근은 안된다.

추가)
order_by('-pk')가 되는 것은 order_by의 파라미터로 str형이 쓰이기 때문이다.
```

4) my_post 변수에 Post 객체 하나가 저장되어 있다. title을 “안녕하세요” content를 “반갑습니다” 로 수정하기 위한 코드를 작성하시오.

```python
my_post.title = '안녕하세요'
my_post.content = '반갑습니다'
my_post.save()
```



5) 만들어진 모든 Post 객체를 QuerySet형태로 반환 해주기 위해 빈칸에 들어갈 코드를 작성하시오.

```python
posts = Post.__(a)__.__(b)__()
```

```
a : objects
b : all
```

