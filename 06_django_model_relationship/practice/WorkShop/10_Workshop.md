# 10_Workshop

## 1. Model 댓글 작성을 위한 테이블을 정의한다. 

**models.py**

```python
class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    content = models.CharField(max_length=150)
```

**forms.py**

```python
class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        # fields = '__all__'
        exclude = ('article',)
```



## 2. Comment Create
/articles//comments/ 댓글 작성 기능을 구현한다.

**views.py**

```python
@require_POST
def create_comment(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.article = article
        comment.save()
        return redirect('articles:detail', article.pk)
    context = {
        'comment_form': comment_form,
        'article': article,
        'comments': article.comment_set.all(),
    }
    return render(request, 'articles/detail.html', context)
```

**detail.html**

```html
<form action="{% url 'articles:create_comment' article.pk %}" method="POST">
    {% csrf_token %}
    {{ comment_form }}
    <input type="submit" value="댓글달기">
  </form>
  {% if comments %}
    {{ comments|length }}개의 댓글이 있습니다.
  {% endif %}
```



## 3. Comment Read 
댓글 읽기 기능을 구현한다. 상세 페이지 하단에 댓글 목록을 출력한다. 

**detail.html**

```html
  <ul>
    {% for comment in comments %}
      <li>{{ comment.content }}</li>
    {% empty %}
      <li>아직 댓글이 없습니다.</li>
    {% endfor %}
  </ul>
```



## 4. Comment Delete 
/articles//comments//delete/ 댓글 삭제 기능을 구현한다.

**detail.html**

```html
<form action="{% url 'articles:delete_comment' article.pk comment.pk %}" method="POST">
    {% csrf_token %}
    <input type="submit" value="DELETE">
</form>
```

