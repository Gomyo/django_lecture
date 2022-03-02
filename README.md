# Django Curriculum

## 시작하기 전에

### Python 설치

3.8.x 이상의 버전으로 설치. 이때, PATH에 추가하는 옵션을 체크해 주세요.

![image-20220302204608860](README.assets/image-20220302204608860.png)

만일 체크하지 않으셨다면 `시스템 속성 > 환경 변수` 탭에서 추가해 주시면 됩니다.

shell 창에서 `python --version`을 입력했을 때, 아래와 같은 결과가 출력되어야 합니다.

![image-20220302204809886](README.assets/image-20220302204809886.png)

### vscode django extension 설치

![image-20220302202128633](README.assets/image-20220302202128633.png)

### django extension 설정

`ctrl + shift + p` -> `json 검색` -> `Preferences: Open Settings (JSON) 선택 후, 아래의 내용 추가`

 ```json
 // setting.json
 ...
 "files.associations": {
     "**/*.html": "html",
     "**/templates/**/*.html": "django-html",
     "**/templates/**/*": "django-txt",
     "**/requirements{/**,*}.{txt,in}": "pip-requirements",
 },
 "emmet.includeLanguages": {
     "django-html": "html",
 },
 ```

