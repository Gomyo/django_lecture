## 결과

![variable_routing_result](./variable_routing_result.PNG)

## 코드

1. intro/urls.py

```python
from django.contrib import admin
from django.urls import path
from pages import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dinner/<str:menu>/<int:person_nums>/', views.dinner),
]
```
2. pages/views.py

```python
from django.shortcuts import render

# Create your views here.
def dinner(request, menu, person_nums):
    context = {
        'menu': menu,
        'person_nums': person_nums,
    }
    return render(request, 'dinner.html', context)
```

3. templates/dinner.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>
  <h1>저녁 메뉴</h1>
  <h1>저녁 먹을 사람?! {{ person_nums }}명</h1>
  <h1>어떤 메뉴?! {{ menu }} </h1>
</body>
</html>
```
