from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import render
from django.http.response import JsonResponse, HttpResponse
from django.core import serializers
from .models import Article
from .serializers import ArticleSerializer

# Create your views here.
def article_html(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/article.html', context)


def article_json_1(request):
    articles = Article.objects.all()
    articles_json = []

    for article in articles:
        articles_json.append(
            {
                'id': article.pk,
                'content': article.content,
            }
        )
    # JsonResponse의 첫번째 인자의 Type이 Dictionary가 아니면 safe=False
    return JsonResponse(articles_json, safe=False)


def article_json_2(request):
    articles = Article.objects.all()
    data = serializers.serialize('json', articles)
    return HttpResponse(data, content_type='application/json')


@api_view(['GET'])
def article_json_3(request):
    articles = Article.objects.all()
    # 받는 값이 단일 객체가 아니라면 many=True로 설정해 줘야 한다.
    serializer = ArticleSerializer(articles, many=True)
    return Response(serializer.data)

