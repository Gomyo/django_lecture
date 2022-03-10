## 1. MTV 

Django는 MTV 디자인 패턴으로 이루어진 Web Framework이다. 여기서 MTV는 무엇의 약자이며 각각 MVC 디자인 패턴과 어떻게 매칭이 되며 각 키워드가 django에서 하는 역할을 간략히 서술하시오.

|    MVC     |   MTV    |                   |
| :--------: | :------: | :---------------: |
|   Model    |  Model   | 데이터베이스 관리 |
|    View    | Template | 인터페이스, 화면  |
| Controller |   View   |   중심 컨트롤러   |

## 2. URL

__(a)__는 Django에서 URL 자체를 변수처럼 사용해서 동적으로 주소를 만드는 것을
의미한다. __(a)__는 무엇인지 작성하시오.

```shell
variable routing (동적 라우팅)
```



## 3. Django template path
Django 프로젝트는 render할 template 파일들을 찾을 때, 기본적으로 settings.py에
등록된 각 앱 폴더 안의 __(a)__ 폴더 내부를 탐색한다. __(a)__에 들어갈 폴더 이름을
작성하시오.

```python
templates
```



## 4. Static web and Dynamic web
Static web page와 Dynamic web page의 특징을 간단하게 서술하시오.

### Static web page (정적 웹 페이지)

- 보통 정해진 레이아웃에 페이지 수를 고정하려 할 때 정적으로 구성한다.
- 이미 구성된 html 문서를 서버에 저장해 놓은 뒤, 클라이언트가 요청하면 보여주며 문서의 내용은 바뀌지 않는다.

### Dynamic web page (동적 웹 페이지)

- 사용자의 요청이 들어오면 웹 어플리케이션 서버 (django 등)에서 상황에 맞는 문서(html) 를 제공한다.
- 상황에 따라 문서를 생성해서 제공하기 때문에 사용자 별로 서로 다른 문서를 제공해줄 수 있다. 요청에 맞는 데이터를 DB에서 찾거나 생성해서 보여주는 것도 가능하다.
- 따라서 정적 페이지보다 더 기능적이다. 사용자가 페이지에 나열되는 정보들과 상호작용을 가능하게 해 준다.
- 정적 페이지는 HTML과 CSS만 사용하는 반면, 동적 페이지는 JavaScript, PHP, ASP 등을 사용할 수 있다.



