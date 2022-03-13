# 0316_Homework

아래 작성된 views.py의 코드 일부를 보고 문제에 알맞은 답을 서술 하시오.

```python
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm()
    context = {
        'form': form,
    }
    return render(request, 'articles/create.html', context)
```

### 1. 왜 변수 context는 if else 구문과 동일한 레벨에 작성 되어있는가?

- if POST인 경우, is_valid하지 않아 다시 create로 돌아가는 경우, 작성하던 내용을 그대로 가져와야 사용자의 UX 측면에서 좋다.
  작성하던 내용이 뭐 하나 잘못됐다고 싹 날아가면 안되기 때문이다.
-  else의 경우 빈 form을 그대로 보여준다.

### 2. 왜 request의 http method는 POST 먼저 확인하도록 작성하는가?

- DB에 어떤 변화를 주는 특정한 요청인 POST를 먼저 확인하고,
  그 외(GET, PUT, DELETE)의 명령어는 접근이 잘못된 경우에 그냥 페이지로 리턴시키면 되기 때문이다.
