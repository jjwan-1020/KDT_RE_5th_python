'''
while 문
- 조건이 True인 동안 코드를 반복하는 반복문
- 조건이 False가 되면 반복을 멈춤
- 반복횟수가 정해지지 않았을 때 사용
'''

# while문 기본 문법
# 조건 : 참/거짓을 구분할 수 있는 문장
# while 조건:
    # 반복할 코드


# 무한루프
# 사용시 주의. 반드시 종료 조건이 있어야 한다
# while True:
#     print("반복중")

# 예제1

light = "green"

while light == "green":
    print("계속가세요!")
    light = input("신호등의 신호를 입력하세요(green/yellow/red)")

print("중지!")

# 예제 2. 별도의 반복 변수를 정의
i = 0

while i < 5:
    print(i, "반복")
    i += 1
print("반복 종료") 

# 실습

s_code = "codingonre3"
while True:
    n_code = input("비밀코드를 입력해주세요: ")
    if n_code != s_code:
        print("다시입력해주해요")
    else:
        print("환영합니다")
        break

    
bingo = 13
count = 0
while True:
    answer = int(input("숫자를 입력하세요: "))
    count += 1
    if bingo == answer:
        print(f"축하합니다.{count}번 만에 정답을 맞추셨습니다")
        break
    elif bingo < answer:
        print(f"{answer}보다 작습니다.")
    else:
        print(f"{answer}보다 큽니다")




# 루프 제어문
'''
running  = True
while running:
    if 조건1:
        running = False
    if 조건2:
        running = False

# break문
while True:
    if 조건:
        break
'''

# 예제 1
i = 0

while True:
    print(i, "실행")
    my_select = input("메뉴를 골라주세요: ")

    if my_select == "종료":
        break

    i += 1

print("반복문 종료")

# continue
i = 0
while i < 5:
    i += 1
    if i % 2 == 0:
        continue
    print(i)
print("반복 종료")

# 실습

c_code = "codingonre3"
while True:
    u_code =  input("코드를 입력해주세요: ")
    if u_code != c_code:
        print("비밀코드가 틀렸습니다. 다시 시도해주세요")
    else:
        print("입장 완료. 환영합니다")
        break


times = 0
sum_age = 0

while times < 5:
    age = int(input("나이를 입력해주세요: "))
    if age <= 0 or age > 120:
        continue
    sum_age += age
    times += 1
        
average = sum_age / 5
print(f"합계 나이는 {sum_age}세 이며, 평균나이는 {average}세입니다")



# 중첩 while문
# 예제

dan = 2
while dan <= 9:
    num =1
    print(f"[{dan}단]")

    while num <= 9:
        num += 1
        if num % 2 != 0:
            break
        else:
            print(f"{dan} x {num} = {dan * num}")

    print()
    dan +=1


# 실습

id = "jjwan"
password = "jj0852"

while True:
    login = input("ID를 입력해주세요: ")
    if login == id:
        while True:
            words = input("비밀번호를 입력해주세요: ")
            if words == password:
                print("로그인에 성공하였습니다")
                break
            else:
                print("비밀번호가 틀립니다. 다시 입력해주세요")
        break
    else:
        print("ID가 존재하지 않습니다")    