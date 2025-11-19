sumb = ['kim', 'lee', 'kim', 'park', ]





user_1 = {'SF', 'Action', 'Drama'}
user_2 = {'Drama', 'Romance', 'SF'}
print("공통 괸심 장르: ", user_1 & user_2)
print("다른 관심 장르: ", user_1 ^ user_2)
print("전체 장르: ", user_1 | user_2)




my_certificates = {'SQL', 'Python', 'Linux'}
job_required = {'SQL', 'Python'}
print(my_certificates.issuperset(job_required))

user = {
    "user_name": "walker",
    "email": "walker.example@gmail.com",
    "level": 6
}
user.update({"level": 8})
user.update({"nickname": "jin"})
print(user)
signup_date = user.setdefault("sigup_date", "2025-07-08")
print(signup_date)



'''
money = int(input("금액을 넣어주세요: "))
item = input("김밥 / 삼각김밥 / 도시락 중 골라주세요: ")

KIMBAB = "김밥"
SAMKIM = "삼각김밥"
DOSIRAK = "도시락"
k_price, s_price, d_price = 2500, 1500, 4000

if item == KIMBAB:
    if money >= k_price:
        print(f"{KIMBAB}을 구입했습니다")
    else:
        print("금액이 부족합니다")
elif item == SAMKIM:
    if money >= s_price:
        print(f"{SAMKIM} 을 구입했습니다")
    else:
        print("금액이 부족합니다")
elif item == DOSIRAK:
    if money >= d_price:
        print(f"{DOSIRAK}을 구입했습니다")
    else:
        print("금액이 부족합니다")
else:
    print("입력이 잘못되었습니다")

# 2) 딕셔너리 사용
prices = {
    "김밥" : 2500,
    "삼각김밥" : 1500,
    "도시락" : 4000 
}

if item in prices:
    if money >= prices[item]:
        print(f"{item}을 구입했습니다")
    else:
        print("금액이 부족합니다")
else:
    print("입력이 잘못되었습니다")

# 11.18
numbers = [3,6,1,8,4]
doubled= []
for nuber in numbers:
    doubled.append(numbers*2)
#    print(doubled)



coordinates = [(1,2), (3,4), (5,6), (7,8)]

x_values = []
y_values = []

for x,y in coordinates:
    x_values = x
    y_values = y

# 11.18
num = int(input("숫자 입력: "))
sum = 0

for i in range(num + 1):
    sum += i
print(sum)


dan = int(input("생성 숫자: "))

for i in range(1, 10):
    print(f"{dan} x {i} = {dan + i}")


result = 0

for i in range(3, 101, 3): #1
    result += i

for i in range(1, 101): # 2
    if i % 3 == 0:
        result += i

print("3의 배수의 합: ", result)

# ----------------------------------------

n = int(input("숫자를 입력하시오: "))

for i in range(1, n+1):
    if i % 2 == 0 and i % 5 == 0:
        print(i)

for x in range(2):
    for y in range(9):
        print("x, y", x*y)
'''

# 복습
'''
number = [3,6,1,8,4]
for x in number:
    print(x*2)

words = ["apple", "banana", "kiwi", "grape"]
for f_list in words:
    fruits = len(f_list)
    print(fruits)

coordinates = [(1,2), (3,4), (5,6), (7,8)]
for x_values, y_values in coordinates:
    print(f"x좌표: {x_values}, y좌표: {y_values}")

n = int(input("숫자 입력란: "))
for num in range(1, n):
    n += num
print(n)

X = int(input())
for hunter in range(1, 10):
    print(f"{X} x {hunter} = {X*hunter}")


z = int(input())
for i in range(1,z+1):
        print("*" * i)

for i in range(1, z + 1):
     print(("*" * i).rjust(z))
'''
# 11.19
'''
secret_code = "codingon"
user_input =  ""
while user_input != secret_code:
     user_input = input("비밀 코드를 입력해주세요: ")
print("환영합니다")
'''
# 문제 2
'''
import random
answer = random.randint(1, 100)
print(answer)
'''
'''
answer = 15
num = 0 # 사용자에게 입력 받을 변수
time = 0 # 실행 횟수를 저장할 수 있는 변수

while num != answer:
     num = int(input("1~100 사이의 수를 입력해주세요: "))
     time += 1
     
     if num > answer:
          print(f"정답이 {num}보다 작습니다")
     elif num < answer:
          print(f"정답이 {num}보다 큽니다")

print(f"{time}번 만에 정답을 맞췄습니다")
'''


'''
c_code = "codingonre3"
while True:
    user_code = input("코드를 입력해주세요: ")
    if user_code != c_code:
        print("정확한 코드를 입력해주세요")
    else:
        print("환영합니다")
        break

sum_age = 0
times = 0

while times < 5:
    age = int(input(f"{times+1}번째 나이를 입력하세요: "))
    if age <= 0 or age > 120:
        continue
    sum_age += age
    times += 1

average = sum_age / 5
print(f"합계나이는 {sum_age}세 이며, 평균나이는 {average}세 입니다")
'''
# 실습4
id = "jjwan"
pw = "just"
while True:
    print("""===로그인 화면===
1. 로그인
2. 종료
""")
    choice = input("선택: ")
    if choice == "2":
        print("프로그램을 종료합니다.")
        break
    elif choice == "1":
        while True:
            login = input("ID: ")
            if login == id:
                while True:
                    words = input("PW: ")
                    if words == pw:
                        print("로그인 성공!")
                        break
                    else:
                        print("로그인 실패! 다시 시도해주세요")
                        continue


