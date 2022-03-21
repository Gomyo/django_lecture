# 09_Practice

### 1. 가상환경 설정하기

​	1-1. 가상환경 활성화

### 2. .gitignore

​	2-1. 추가사항 설정 해서 수정하기

### 3. django 설치 및 프로젝트 생성

​	3-1. django 설치 후, requirements.txt 만들어 주기

### 4. base.html 만들기 혹은 articles app 생성하기.

​	4-1. base.html 설정

		- django_bootstrap-v5 설치 및 등록
		- pip freeze

​	4-2. articles app 설정

### 5. articles model 정의하기

​	5-1. title, content, created_at, updated_at

### 6. CRUD

	1. index
	2. craete
	3. detail
	4. update
	5. delete

### 7. accounts app 생성하기

​	7-1. accounts 설정

### 8. auth CRUD

### 9. dump data

`python manage.py dumpdata > crud.json`

그러나 위의 명령어만 치면 보기가 불편하므로, 어플리케이션 단위로 가져온다.

- article

`python manage.py dumpdata --indent 2 articles.article > article.json`

- auth 전체 정보 가져오기

`python manage.py dumpdata --indent 2 auth > auth.json`

- auth의 user 테이블만 가져오기

`python manage.py dumpdata --indent 2 auth.user > auth.json`

## Troubleshooting

**AttributeError**

`AttributeError at /accounts/password/`
`'User' object has no attribute 'get'`

에러가 발생한다. 문제는 views.py > def change_password에서,
GET으로 접속했을 때 받아오는 Form 인자로 request.user(현재 유저 정보)만 받아야 하는데 엉뚱하게 request도 같이 받아와서 문제였다. 다음에도 같은 에러가 발생한다면, 필요 없는 정보를 받지는 않았나 생각해보자.
