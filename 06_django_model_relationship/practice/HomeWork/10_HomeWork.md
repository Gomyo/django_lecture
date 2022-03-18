# 10_HomeWork

### 1. Lookup

- 지문의 코드에서 ‘__gt’ 부분을 lookup이라고 한다. 링크를 참고하여 Django에서 사용 가능 한 lookup 세가지와 그 의미를 작성하시오. 

  https://docs.djangoproject.com/en/3.1/ref/models/querysets/#field-lookups

  ```python
  Entry.objects.filter(pk__gt=4)
  ```

```
gt : 초과
gte : 이상
lt : 미만
lte : 이하
```



### 2. 1:N 관계 설정

- 지문은 1:N 관계 설정을 하기 위하여 정의된 모델이다. 링크를 참고하여 빈 칸에 들어갈 수 있는 값 세가지를 선택 후 그 의미를 작성하시오. 

  https://docs.djangoproject.com/en/3.1/ref/models/fields/#arguments

  ```python
  class Comment(models.Model):
      content = models.CharField(max_length=100)
      article = models.ForeignKey(Article, on_delete=__(a)__)
  ```

  ```
  CASCADE : 부모 객체가 삭제되면 부모 객체를 참조하는 객체도 함께 삭제되는 옵션
  PROTECT : 참조되어 있는 경우 오류 발생
  SET_NULL : 부모객체가 삭제됐을 때 모든 값을 NULL로 치환. (NOT NULL 조건시 불가능)
  SET_DEFAULT : 모든 값을 DEFAULT로  치환 (Default 설정 있어야 함ㅁ. DB에서는 보통 default 없으면 null로 잡기도 하지만 장고는 그렇지 안ㄶ다.)
  SET : 특정 함수 호출
  DO_NOTHING : 아무것도 하지 않음. 다만 sql에 ON DELETE 직접 설정
  ```
  
  

### 3. comment create view 

- 지문은 댓글 기능을 작성하기 위한 코드이다. 빈 칸에 들어갈 코드와 의미를 작성하시오.

  ```python
  def comment_create(request, pk):
      Article = Article.objects.get(pk=pk)
      if request.method == 'POST':
          form = CommentForm(request.POST)
          if form.is_valid():
              comment = form.save(__(a)__)
              comment.article = article
              comment.save()
             	return redirect('atciels:index')
  ```

  ```
  a: commit=False
  객체 조작을 위해 인스턴스를 생성하지만 저장하지는 않음
  ```
  
  

### 4. 1:N DB API 

- 게시물 아래에 댓글을 출력하려고 한다. Article과 Comment 모델이 1:N으로 관계설정 이 되어 있다고 가정 할 때 아래의 빈칸에 적절한 코드를 작성하시오.

  ```html
  <h1>{{ article.title }}</h1>
  {% for comment in __(a)__ %}
    <p>{{ comment.content }}</p>
  {% empty %}
    <p>댓글이 없습니다.</p>
  {% endfor %}
  ```

  ```
  a : article.comment_set.all
  DTL이니 ()는 넣지 않는다.
  ```
  
  