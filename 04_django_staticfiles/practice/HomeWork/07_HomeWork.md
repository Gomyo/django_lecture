# 07_HomeWork

Related project path : ssafy_mygit/django_webex/0317_03_django_form

### 1. static 파일 기본 설정

- 개발자가 작성한 CSS 파일이나 넣고자 하는 이미지 파일 등이 Django 프로젝트 폴더 내부 의 ‘/assets’에 있다. ‘이 폴더 안에 Static 파일이 있다.’라고 Django 프로젝트에게 알려 주기 위하여 settings.py에 작성해야 하는 설정을 작성하시오. 

파일이 있는 경로를 STATICFILES_DIRS 넣어 주어야 한다.

여러 가지 방법으로 넣을 수 있다.

```python
STATIC_URL = '/static/'
STATIC_DIR2 = BASE_DIR / 'Django' / 'static' / 'assets'
STATIC_DIR3 = os.path.join(BASE_DIR, 'Django', 'static', 'assets')

STATICFILES_DIRS = [
    BASE_DIR / 'Django' / 'static' / 'assets',
    STATIC_DIR2,
    STATIC_DIR3,
]
```



### 2. media 파일 기본 설정 

- 업로드 파일 저장 위치를 Django 프로젝트 폴더 내부의 ‘/uploaded_files’로 지정하고자 한 다. 이 때, settings.py에 작성해야 하는 설정을 모두 작성하시오. 

경로와 URL을 지정해 주어야 한다.

```python
# Django 프로젝트 폴더 내부의 media로 넣는다
MEDIA_ROOT = BASE_DIR / 'Django' / 'media'
MEDIA_URL = '/media/'

# 글을 업로드하게 되면 프로젝트 구조는 아래와 같아진다.
Django/
	media/
    	uploaded_files/
        	files
```



### 3. Serving files uploaded by user during development 

- settings.py에 MEDIA_URL 값이 작성되어 프로젝트에 사용자가 업로드한 파일이 업로드 될 수 있게 되었다. 하지만 사용자가 실제 웹 페이지 내에서 이 파일을 조회 할 수 있도록 하기 위해선 업로드 된 파일에 대한 URL을 생성 해주는 설정이 필요하다. 빈칸 __(a)__, __(b)__, __(c)__, __(d)__에 들어 갈 코드를 작성하시오.

  ```python
  from django.conf import __(a)__
  from __(b)__ import __(c)__
  
  urlpatters = [
      ...
  ] + static( __(d)__ )
  ```

  ```
  a : settings
  b : django.conf.urls.static
  c : static
  d : settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
  ```
  
  