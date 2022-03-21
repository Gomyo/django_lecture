# 0316_Homework

1) 모델 폼을 정의하기 위해 빈칸에 들어갈 코드를 작성하시오.

```python
from django import forms
from .models import Article

class ReservationForm(__(a)__):

    class __(b)__:
        model = Reservation
        fields = '__all__'
```

```
a : forms.ModelForm
b : Meta
```

2) 글 작성 기능을 구현하기 위해 다음과 같이 코드를 작성하였다. 서버를 실행시킨 후 기능을 테스트 해보니 특정 상황에서 문제가 발생하였다. 이유와 해결방법을 작성하시오.

```python
def create(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save()
            return redirect('reservations:detail', reservation.pk)
    else:
        form = ReservationForm()
        context = {
            'form': from,
        }
        return render(request, 'reservations/create.html', context)
```

Model 설정과 DB의 괴리가 있는 등의 오류로 잘못된 정보를 DB에 저장하려고 하면 is_valid에서 False가 나오게 된다.

이처럼 form.is_valid하지 않을 경우, 작성하던 정보와 에러를 가지고 create page로 리턴해줘야 하는데 그에 대한 처리가 되어 있지 않다.

이를 해결하기 위해서는 context 이하의 코드를 if-else 단으로 한 탭 당겨줘야 한다.

3) 글 수정 기능을 구현하기 위해 빈칸에 들어갈 코드를 작성하시오.

```python
def update(request, pk):
    reservation = Reservation.objects.get(pk=pk)
    if request.method == 'POST':
		__(a)__
        if form.is_valid():
            reservation = form.save()
            return redirect('reservations:detail', reservation.pk)
    else:
        __(b)__
    context = {
        'reservation': reservation,
        'form': form,
    }
    return render(request, 'articles/update.html', context)
```

```
a : form = ReservationForm(request.POST, instance=reservation)
b : form = ReservationForm(instance=reservation)
```



4) 글 수정 기능을 구현하기 위해 빈칸에 들어갈 수 있는 코드를 모두 작성하시오.

```html
<h1>UPDATE</h1>
  <form action="{% url 'articles:update' article.pk %}" method="POST">
    {% csrf_token %}
		{{ form.__(a)__ }}
    <input type="submit">
  </form>
```

```
as_p (단락 구성)
as_ul (unordered list로 구성)
as_table (표로 구성)
```

