# 15_Workshop

![result](README.md.assets/result.PNG)

**views.py**

```python
def profile(request, username):
    User = get_user_model()
    person = get_object_or_404(User, username=username)
    context = {
        'person': person,
    }
    return render(request, 'accounts/profile.html', context)

@require_POST
def follow(request, user_pk):
    if request.user.is_authenticated:
        User = get_user_model()
        you = get_object_or_404(User, pk=user_pk)
        me = request.user
        if you != me:
            if you.followers.filter(pk=me.pk).exists():
                you.followers.remove(me)
            else:
                you.followers.add(me)
        return redirect('accounts:profile', you.username)
    return redirect('accounts:login')

```



**models.py**

```python
class User(AbstractUser):
    followings = models.ManyToManyField('self', symmetrical=False, related_name="followers")

```



**profile.html**

```html
{% extends 'base.html' %}

{% block content %}
  <h1>{{ person.username }} 님의 프로필</h1>
  {% with followings=person.followings.all followers=person.followers.all %}
    <p>follow : {{ followings|length }}</p>
    <p>follower : {{ followers|length }}</p>
    <form action="{% url 'accounts:follow' person.pk %}" method='POST'>
      {% csrf_token %}
      {% if request.user.pk != person.pk %}
        {% if request.user in person.followers.all %}
          <button class='btn btn-danger'><i class="fas fa-user-times"></i></button>
        {% else %}
          <button class='btn btn-primary'><i class="fas fa-user-plus"></i></button>
        {% endif %}
      {% endif %}
    </form>
  {% endwith %}

  <h1>{{ person.username }} 님의 게시글</h1>
  {% for article in person.article_set.all %}
    <div>{{ article.title }}</div>
  {% endfor %}
  <hr>

  <h1>{{ person.username }} 님의 댓글</h1>
  {% for comment in person.comment_set.all %}
    <div>{{ comment.content }}</div>
  {% endfor %}
  <hr>

  <h1>{{ person.username }} 's likes</h1>
    <ul>
    {% for article in person.like_articles.all %}
        <li>{{ article.title }}</li>
    {% endfor %}
    </ul>
  <hr>
  <a href="{% url 'articles:index' %}">목록</a>
{% endblock content %}

```

