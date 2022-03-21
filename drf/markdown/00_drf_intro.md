# 00_drf_intro

## Serialization (직렬화)

- 데이터 구조나 객체 상태를 동일하거나 다른 컴퓨터 환경에 저장하고 나중에 재구성할 수 있는 포맷으로 변환하는 과정
- 예를 들어 DRF의 Serializer는 **Django의 Queryset 및 Model Instance와 같은 복잡한 데이터를, JSON, XML 등의 유형으로 쉽게 변환 할 수 있는** Python 데이터 타입으로 만들어 줌
- DRF의 Serialzer는 Django의 Form/ModelForm 클래스와 매우 유사하게 작동

## api_view decorator

- view 함수가 응답해야하는 http method 목록을 설정
- 작성하지 않으면 기본적으로 GET 메서드만 허용되며, 목록에 작성되지 않은 메서드일 경우 405 Method Not Allowed를 반환

### DRF Response 실습

```python
@api_view(['GET'])
def article_json_3(request):
    articles = Article.objects.all()
    # 받는 값이 단일 객체가 아니라면 many=True로 설정해 줘야 한다.
    # 단일 객체가 아닌, Queryset이므로 many=True.
    serializer = ArticleSerializer(articles, many=True)
    return Response(serializer.data)
```
