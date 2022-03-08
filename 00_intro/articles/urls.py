from django.urls import path
# 명시적 상대경로 표현
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('variables/', views.variables, name='variables'),
    path('filters/', views.filters, name='filters'),
    path('throw/', views.throw, name='throw'),
    path('catch/', views.catch, name='catch'),
    path('varRoute/<str:name>/', views.varRoute, name='varRoute'),
    # 기본값이 string이어서 str:은 생략해도 됩니다. int는 생략할 수 없어요.
    # path('varRoute/<name>/', views.varRoute),
]
