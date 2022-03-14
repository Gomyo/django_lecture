# Workshop

![0311_result](./0311_result.PNG)

## CRUD 구현

CRUD를 구현했다.

교수님과 앞부분을 진행했는데,

```python
if request.method == 'POST':
```

위 코드를 create에 적용하여 new 함수와 edit 함수를 만들 필요 없이, 한 함수 내에서 redirect와 render를 if문 분기하여 실행하게 하였다.

뒤의 update만 해서 올리라고 하셔서 update는 프로젝트의 명세에 맞게 edit 함수와 edit.html을 따로 만들어서 구현해 보았다.

## 코드

### python

- urls.py
```python
from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('', views.index, name='index'),
    path('new/', views.new, name='new'),
    path('create/', views.create, name='create'),
    path('<int:post_pk>/', views.detail, name='detail'),
    path('<int:post_pk>/delete/', views.delete, name='delete'),
]

```

- views.py
```python
from django.shortcuts import render, redirect, get_object_or_404
from .models import Article

# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)


```

- models.py
```python
from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

```

### html

3월 10일과 명세가 같길래 그냥 다른 방식으로 구현해 보았다.

### 1) READ

- index.html
```html
{% extends 'base.html' %}

{% block content %}
  <h1>INDEX PAGE</h1>
  <hr>
  <a href="{% url 'articles:create' %}">[글쓰기]</a>
  <ul>
    {% for article in articles %}
      <li>
        <a href="{% url 'articles:detail' article.pk %}">
          {{ article.pk }} 번 글 | {{ article.title }}
        </a>
      </li>
    {% empty %}
      <p>아직 글이 없습니다.</p>
    {% endfor %}
  </ul>
{% endblock content %}

```

### 2) CREATE

views.py

```python

def create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')

        article = Article(title=title, content=content)
        article.save()
        return redirect('articles:detail', article.pk)
    else:
        return render(request, 'articles/create.html')
```



- create.html

**form을 비워두면 현재 URL로 정보를 날린다.**

**이것을 이용해 new를 만들지 않고도 create.html에서 render, redirect을 모두 할 수 있게 한다.**

```html
{% extends 'base.html' %}

{% block content %}
  <h1>NEW</h1>
  <hr>
  <!-- form을 비워두면 현재 URL로 정보를 날린다. -->
  <form action="" method="POST">
    {% csrf_token %}
    <label for="title">TITLE | </label>
    <input type="text" id="title" name="title">

    <label for="content">CONTENT | </label>
    <textarea name="content" id="content" cols="30" rows="10"></textarea>

    <input type="submit">
  </form>
  <a href="{% url 'articles:index' %}">[BACK]</a>
{% endblock content %}

```

### 3) DETAIL

view.py

```python


def detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)

    context = {
        'article': article,
    }
    return render(request, 'articles/detail.html', context)

```



- detail.html (read)

humanize를 적용해 한국인에게 보다 친숙한 페이지 UX를 주었다.

**edit, delete 모두 DB에 접속하는 중요한 부분이기 때문에 POST form으로 넘겨주고, views.py에서도 method를 체크하는 부분을 추가했다.**

```html
{% extends 'base.html' %}
{% load humanize %}

{% block content %}
  <h1>DETAIL PAGE</h1>
  <hr>
  <p> {{ article.pk }}</p>
  <p> {{ article.title }}</p>
  <p> {{ article.content }}</p>
  <p>작성일: {{ article.created_at|naturalday }}</p>
  <p>수정일: {{ article.updated_at|naturaltime }}</p>
  <hr>
  <form action="{% url 'articles:edit' article.pk %}" method='POST'>
    {% csrf_token %}
    <input type="submit" value="EDIT">
  </form>
  <form action="{% url 'articles:delete' article.pk %}" method='POST'>
    {% csrf_token %}
    <input type="submit" value="DELETE">
  </form>
  <hr>
  <a href="{% url 'articles:index' %}">[BACK]</a>
{% endblock content %}

```



### 4) UPDATE

views.py

```python

def edit(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    # create의 else와 다르게 context로 넘겨주어야 한다.
    context = {
        'article': article,
    }
    return render(request, 'articles:detail', context)

def edit(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if request.method == 'POST':
        # create의 else와 다르게 context로 넘겨주어야 한다.
        context = {
            'article': article,
        }
        return render(request, 'articles/edit.html', context)
    else:
        return redirect('articles:detail', article.pk)

```

edit.html

input, textarea에 값이 채워져 있어야 함을 명심한다.

```html
{% extends 'base.html' %}

{% block content %}
  <h1>EDIT</h1>
  <hr>
  <form action="{% url 'articles:update' article.pk %}" method="POST">
    {% csrf_token %}
    <label for="title">TITLE | </label>
    <input type="text" id="title" name="title" value="{{ article.title }}">

    <label for="content">CONTENT | </label>
    <textarea name="content" id="content" cols="30" rows="10">{{ article.content }}</textarea>

    <input type="submit">
  </form>
  <a href="{% url 'articles:detail' article.pk %}">[BACK]</a>
{% endblock content %}

```



### 5) DELETE

views.py

```python
def delete(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if request.method == 'POST':
        article.delete()
        return redirect('articles:index')
    return redirect('articles:detail', article.pk)
```

