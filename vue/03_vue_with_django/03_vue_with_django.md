# 03_vue_with_django

**03_vue_with_django_TEMPLATE를 사용해서 실습하시면 됩니다. 주석처리한 것을 해제하는 방식으로 진행합니다.**

- django는 API 요청을 보내면 잘 응답하는 상태입니다.
- `npm run serve`로 client 폴더의 Vue 프로젝트를 시작해 보겠습니다.
  - Router, page 모두 완성되어 있는 코드입니다.

## TODOS CRUD, CORS

### GET TODOS

- 할일 목록을 불러오도록 하겠습니다.

```js
// TodoList.vue

getTodos: function () {
      axios({
        method: 'get',
        url: 'http://127.0.0.1:8000/todos/',
        headers: this.setToken()
      })
        .then((res) => {
          console.log(res)
          this.todos = res.data
        })
        .catch((err) => {
          console.log(err)
        })
    },
```

- getTodos 이벤트를 클릭에 대응하도록 하고, get Todos 버튼을 눌러보면 CORS 에러가 나옵니다. 둘의 Origin이 다르기 때문입니다. 서버는 제대로 응답해 주었지만 그 응답을 받지 못하는 상황입니다.
- Django 측에서 Vue 측의 출처를 Allow하도록 헤더를 추가해서 보내야 합니다.

### Django CORS headers

- 'corsheader'를 INSTALLED_APPS에, 'corsheaders.middleware.CorsMiddleware'를 MIDDLEWARE에 추가해 줍니다.
- ORIGIN을 선택적으로 허용하거나 전부 허용할 수 있습니다.

```python
# 1. 특정 Origin만 선택적으로 허용
CORS_ALLOWED_ORIGINS = [
    "https://example.com",
    "https://sub.example.com",
    "http://localhost:8080",
    "http://127.0.0.1:9000"
]

# 2. 모든 Origin 허용
CORS_ALLOW_ALL_ORIGINS = True
```

- 모든 Origin을 허용해 주고 다시 한번 todos를 가져와 봅시다. 잘 가져오죠?

### GET TODOS when created hook

- 버튼이 아니라, 새로고침할 때마다 리스트를 가져오도록 수정해 보겠습니다.
- get todos 버튼을 주석처리하고, created 훅에 getTodos() 메서드를 호출합니다.

```js
created: function () {
    this.getTodos()
  }
```

### CREATE TODO

- 할일을 만들어 보겠습니다.
- 확인을 위해, create에 성공했을 경우 TodoList로 이동해 주겠습니다.

```js
createTodo: function() {
      const todoItem = {
        title: this.title,
      };

      if (todoItem.title) {
        axios({
          method: "post",
          url: "http://127.0.0.1:8000/todos/",
          data: todoItem,
        })
          .then((res) => {
            console.log(res);
            this.$router.push({ name: "TodoList" });
          })
          .catch((err) => {
            console.log(err);
          });
      }
    },
```

### DELETE TODO

- 삭제에 성공했을 경우 데이터베이스의 변화를 반영하도록, todo의 리스트를 다시 가져오도록 합니다.

### UPDATE TODO

- 데이터베이스의 변화를 반영하도록, 할일의 completed 속성 값을 변환시켜 줍니다.

```js
.then((res) => {
        console.log(res);
        todo.completed = !todo.completed;
      });
```

## AUTH JWT

- JWT를 활용한 인증을 구현해 보겠습니다.

### SIGNUP

- 회원가입을 위한 data를 선언하고, input 태그와 양방향 바인딩을 합니다.
- signup을 위한 비동기 API 요청 함수를 axios를 사용해서 작성합니다.

```html
// Signup.vue
<template>
  <div>
    <h1>Signup</h1>
    <div>
      <label for="username">사용자 이름: </label>
      <input type="text" id="username" v-model="credentials.username" />
    </div>
    <div>
      <label for="password">비밀번호: </label>
      <input type="password" id="password" v-model="credentials.password" />
    </div>
    <div>
      <label for="passwordConfirmation">비밀번호 확인: </label>
      <input
        type="password"
        id="passwordConfirmation"
        v-model="credentials.passwordConfirmation"
      />
    </div>
    <button @click="signup(credentials)">회원가입</button>
  </div>
</template>
```

```js
// Signup.vue
  name: 'Signup',
  data: function () {
    return {
      credentials: {
        username: null,
        password: null,
        passwordConfirmation: null,
      }
    }
  },
  methods: {
    signup: function() {
      axios({
        method: "post",
        url: "http://127.0.0.1:8000/accounts/signup/",
        data: this.credentials,
      })
        .then((res) => {
          console.log(res);
          this.$router.push({ name: "Login" });
        })
        .catch((err) => {
          console.log(err);
        });
    },
  },
```

- 이제 Todo 모델에 유저의 외래키를 추가해 줍니다.

```python
from django.db import models
from django.conf import settings

# Create your models here.
class Todo(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='todos')
    title = models.CharField(max_length=50)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title
```

- makemigrations, migrate를 순차적으로 실행합니다.
- 다음으로 User의 Serializer를 완성합니다. password는 정보를 받기는 하지만, 응답에는 포함시키지 않을 것이기 때문에 `write_only`옵션을 활성화합니다.
- signup의 url을 설정해 주고, signup view 함수의 주석을 해제합니다.

```python
urlpatterns = [
    path('signup/', views.signup),
]
```

- 회원가입을 직접 해 보면, 잘 되는 것을 확인할 수 있습니다.

### LOGIN

- 로그인을 위한 JWT의 설정을 먼저 해주겠습니다.

- 가장 먼저 DRF의 jwt 라이브러리를 설치합니다.
- `pip install djangorestframework-jwt`

- JWT와 관련된 설정은 많지만, 이번에는 만료 기간만 설정해 주겠습니다.

```python
# settings.py
JWT_AUTH = {
    'JWT_EXPIRATION_DELTA': datetime.timedelta(days=1),
}
```

- 템플릿은 회원가입에 사용한 것을 그대로 가져가서 살짝만 변형합니다.
- localStorage에 jwt를 저장하고, 이를 사용해서 세션을 유지하는 방식으로 진행하겠습니다.

```js
// Login.vue
<template>
  <div>
    <h1>Login</h1>
    <div>
      <label for="username">사용자 이름: </label>
      <input type="text" id="username" v-model="credentials.username">
    </div>
    <div>
      <label for="password">비밀번호: </label>
      <input type="password" id="password" v-model="credentials.password">
    </div>
    <button @click="login">로그인</button>
  </div>
</template>

<script>
import axios from 'axios'

// const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'Login',
  data: function () {
    return {
      credentials: {
        username: null,
        password: null,
      }
    }
  },
  methods: {
    login: function () {
      axios({
        method: 'post',
        url: 'http://127.0.0.1:8000/accounts/api-token-auth/',
        data: this.credentials,
      })
        .then(res => {
          console.log(res)
          localStorage.setItem('jwt', res.data.token)
          this.$router.push({ name: 'TodoList' })
          this.$emit('login') // 로그인 직후 App 전체에 login 상태값을 true로 변경하기 위한 event emit
        })
        .catch(err => {
          console.log(err)
        })
    }
  }
}
</script>
```

- 이제 django의 url을 연결해 주겠습니다. 직접 함수를 만들지 않고, `obtain_jwt_token`을 import해서 사용합니다.

```python
# urls.py

from rest_framework_jwt.views import obtain_jwt_token

from django.urls import path
from . import views


urlpatterns = [
    path('signup/', views.signup),
    path('api-token-auth/', obtain_jwt_token),
]
```

- 그럼 로그인을 해 보겠습니다.
- localStorage를 확인하면 jwt가 제대로 발급되었음을 확인할 수 있습니다.

### login 상태에 따른 VUE 조건부 렌더링

- 로그인에 따라 nav router를 다르게 렌더링하는 방식으로, 로그인 상태를 확실하게 체크해 보도록 하겠습니다.
- 로그아웃 함수까지 작성하겠습니다.

```js
// App.vue
<template>
  <div id="app">
    <div id="nav">
      <span v-if="isLogin">
        <router-link :to="{ name: 'TodoList' }">Todo List</router-link> |
        <router-link :to="{ name: 'CreateTodo' }">Create Todo</router-link> |
        <router-link @click.native="logout" to="#">Logout</router-link>
      </span>
      <span v-else>
        <router-link :to="{ name: 'Signup' }">Signup</router-link> |
        <router-link :to="{ name: 'Login' }">Login</router-link>
      </span>
    </div>
    <router-view @login="isLogin = true"/>
  </div>
</template>

<script>
export default {
  name: 'App',
  data: function () {
    return {
      isLogin: false,
    }
  },
  methods: {
    logout: function () {
      this.isLogin = false
      localStorage.removeItem('jwt')
      this.$router.push({ name: 'Login' })
    }
  },
  created: function () {
    const token = localStorage.getItem('jwt')
    if (token) {
      this.isLogin = true
    }
  }
}
</script>
```

- 로그인 후 JWT를 받아오고, 로그인 조건부 렌더링까지 작업을 완료했습니다.

### login 상태에 따른 todos의 처리 분기

- 이제 TODOS의 목록을 가져오고, 새로 작성하는 함수를 django에서 로그인 유무를 체크하도록 하겠습니다. todos의 view 함수들에서 API의 타입만 체크하는 것이 아니라, JWT도 체크하게 됩니다.

```python
# todos/views.py
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

# JWT 을 활용한 인증을 할 때 JWT 자체를 인증 여부와 상관 없이 JWT가 유효한지 여부만 파악
@authentication_classes([JSONWebTokenAuthentication])
# 인증이 되지 않은 상태로 요청이 오면
# "자격 인증 데이터"가 제공되지 않았습니다와 같은 메세지를 응답함
@permission_classes([IsAuthenticated])
```

### jwt를 Axios 요청에 헤더로 넣기

- JWT의 유무를 체크하기 때문에, 이제 axios 요청에 올바른 형태로 JWT를 넣어 주어야 합니다.

```js
// CreateTodo.vue - method
setToken: function () {
      const token = localStorage.getItem('jwt')
      const config = {
        Authorization: `JWT ${token}`
      }
      return config
    },
    createTodo: function () {
      const todoItem = {
        title: this.title,
      }

      if (todoItem.title) {
        axios({
          method: 'post',
          url: 'http://127.0.0.1:8000/todos/',
          data: todoItem,
          headers: this.setToken()
        })
          .then((res) => {
            console.log(res)
            this.$router.push({ name: 'TodoList' })
          })
          .catch((err) => {
            console.log(err)
          })
        }
    },
```

```js
// TodoList.vue - method
setToken: function () {
      const token = localStorage.getItem('jwt')
      const config = {
        Authorization: `JWT ${token}`
      }
      return config
    },
    getTodos: function () {
      axios({
        method: 'get',
        url: 'http://127.0.0.1:8000/todos/',
        headers: this.setToken()
      })
        .then((res) => {
          console.log(res)
          this.todos = res.data
        })
        .catch((err) => {
          console.log(err)
        })
    },
    deleteTodo: function (todo) {
      axios({
        method: 'delete',
        url: `http://127.0.0.1:8000/todos/${todo.id}/`,
        headers: this.setToken()
      })
        .then((res) => {
          console.log(res)
          this.getTodos()
        })
        .catch((err) => {
          console.log(err)
        })
    },
    updateTodoStatus: function (todo) {
      const todoItem = {
        ...todo,
        completed: !todo.completed
      }

      axios({
        method: 'put',
        url: `http://127.0.0.1:8000/todos/${todo.id}/`,
        data: todoItem,
        headers: this.setToken(),
      })
        .then((res) => {
          console.log(res)
          todo.completed = !todo.completed
        })
      },
    },
  created: function () {
    if (localStorage.getItem('jwt')) {
      this.getTodos()
    } else {
      this.$router.push({name: 'Login'})
    }
  }
```

### todo에 user 정보 추가로 넣고, 불러올 때도 사용하기

- 이제 모든 Todo를 불러오지 않고, 해당 유저가 작성한 todo만 불러오도록 하겠습니다.

```python
def todo_list_create(request):
    if request.method == 'GET':
        # todos = Todo.objects.all()
        serializer = TodoSerializer(request.user.todos, many=True)
        return Response(serializer.data)
```

- 그리고 해당 todo를 작성한 유저가 아니면 수정, 삭제가 되지 않도록 조치해 주겠습니다.

```python
# todos/views.py - todo_update_delete
    # 1. 해당 todo의 유저가 아닌 경우 todo를 수정하거나 삭제하지 못하게 설정
    if not request.user.todos.filter(pk=todo_pk).exists():
        return Response({'detail': '권한이 없습니다.'}, status=status.HTTP_403_FORBIDDEN)
```

- vue에서도 로그인 되었을 때에만 todos의 리스트를 렌더링합니다. created 훅의 함수를 변경합니다.

```js
// TodoList.vue
created: function () {
  if (localStorage.getItem('jwt')) {
    this.getTodos()
  } else {
    this.$router.push({name: 'Login'})
  }
}
```
