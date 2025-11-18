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


