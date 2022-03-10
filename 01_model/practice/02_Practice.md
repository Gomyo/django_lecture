`### 02_Practice

### 결과

![lotto_result](./lotto_result.PNG)

> 로또 당첨 번호 링크
>
> [lotto](https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=953)

1. views.py

   ```python
   from django.shortcuts import render
   import requests
   import random

   def play_lotto(n, lotto):
       res = [0]*6 # 1 ~ 6등

       for tc in range(n):
           cnt = 0
           bonus_cnt = 0
           gazua = random.sample(range(1, 46), 6)

           for num in gazua:
               if lotto[num] == 1:
                   cnt += 1
               elif num == lotto[0]:
                   bonus_cnt += 1

           if cnt == 6:
               res[0] += 1
           elif cnt == 5 and bonus_cnt:
               res[1] += 1
           elif cnt == 5:
               res[2] += 1
           elif cnt == 4:
               res[3] += 1
           elif cnt == 3:
               res[4] += 1
           else:
               res[5] += 1
       return res

   # Create your views here.
   def lotto(request):
       url = 'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=953'

       response = requests.get(url)
       lotto_data = response.json()
       lotto_nums = []
       lotto = [0] * 46

       for i in range(1, 7):
           tmp = lotto_data['drwtNo'+str(i)]
           lotto[tmp] = 1
           lotto_nums.append(tmp)

       bonus_num = lotto_data['bnusNo']
       lotto[0] = bonus_num

       lotto_result = play_lotto(10000, lotto)

       context = {
           'l': lotto_result,
           'life_change': lotto_result[0],
           'second': lotto_result[1],
           'third': lotto_result[2],
           'fourth': lotto_result[3],
           'fifth': lotto_result[4],
           'bomb': lotto_result[5],
           'lotto_nums': lotto_nums,
           'bonus_num': bonus_num,
       }
       return render(request, 'lotto.html', context)

   ```

2. urls.py

   ```python
   from django.urls import path
   from . import views

   urlpatterns = [
       path('lotto/', views.lotto),
   ]
   ```

3. lotto.html

   ```django
   <!DOCTYPE html>
   <html lang="en">
<head>
     <meta charset="UTF-8">
     <meta http-equiv="X-UA-Compatible" content="IE=edge">
     <meta name="viewport" content="width=device-width, initial-scale=1.0">
     <title>Document</title>
   </head>
   <body>
     <h1>로또 당첨 횟수를 알아보자.</h1>
     <hr>
     <h2>이번 회차 당첨 번호 : {{ lotto_nums }} + {{ bonus_num }} </h2>
     <ul>
       <li>1등 : {{ life_change }} 번</li>
       <li>2등 : {{ second }} 번</li>
       <li>3등 : {{ third }} 번</li>
       <li>4등 : {{ fourth }} 번</li>
       <li>5등 : {{ fifth }} 번</li>
       <li>꽝 : {{ bomb }} 번</li>
     </ul>
   </body>
   </html>

   ```

