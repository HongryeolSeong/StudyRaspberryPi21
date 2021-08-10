n = 0                       # n 초기화
numbers = []                # 리스트 numbers 초기화
sum3 = 0                    # 3의 배수들의 총합
sum7 = 0                    # 7의 배수들의 총합

# 1. 리스트 numbers에 값 넣기 : n = 2 ~ 100까지 반복
while True:
    n = n + 1               # n은 1씩 증가
    numbers.append(n)       # numbers에 n 추가
    if (n == 100):          # n = 100이면
        break               # 반복문 종료

# 2. numbers의 요소들 중 3 or 7의 배수를 뽑아 더한다
for i in numbers:
    if i % 3 == 0:          # i가 3의 배수인 경우
        sum3 += i           # sum3에 해당 n이 더해진다.

    if i % 7 == 0:          # i가 7의 배수인 경우
        sum7 += i           # sum7에 해당 n이 더해진다.

# 3. 출력
print(sum3)                 # 3의 배수 총합 출력
print(sum7)                 # 7의 배수 총합 출력