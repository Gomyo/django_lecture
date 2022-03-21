from django.urls import path
from . import views

app_name = 'either'

urlpatterns = [
    path('', views.index, name='index'),
    path('create', views.create, name='create'),
    path('<int:vote_pk>/', views.detail, name='detail'),
    path('<int:vote_pk>/comment', views.create_comment, name='create_comment'),
    path('random/', views.random_pick, name='random_pick'),
]
