# 03_vue_with_django

**03_vue_with_django_TEMPLATE를 사용해서 실습하시면 됩니다. 주석처리한 것을 해제하는 방식으로 진행합니다.**

- django는 API 요청을 보내면 잘 응답하는 상태입니다.
- `npm run serve`로 client 폴더의 Vue 프로젝트를 시작해 보겠습니다.
  - Router, page 모두 완성되어 있는 코드입니다.

## GET TODOS

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

## Django CORS headers

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

## CREATE TODO

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

## DELETE TODO

- 삭제에 성공했을 경우 데이터베이스의 변화를 반영하도록, todo의 리스트를 다시 가져오도록 합니다.

## UPDATE TODO

- 데이터베이스의 변화를 반영하도록, 할일의 completed 속성 값을 변환시켜 줍니다.

```js
.then((res) => {
        console.log(res);
        todo.completed = !todo.completed;
      });
```
