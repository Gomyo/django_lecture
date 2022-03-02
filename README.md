# Django Curriculum

## 시작하기 전에

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

