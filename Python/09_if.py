'''
조건문
- 조건에 따라서 프로그램의 실행 흐름을 분기시키는 제어문
- 조건 : 참/거짓을 구분할 수 있는 문장
'''

# 조건문의 기초 문법
# if + 조건 -> 조건이 참이면 실행

a = int(input())
if a > 10:

 print("a는 10보다 커요")
 print("조건문 종료")

# 들여쓰기 에러 예시
if a > 10:
    print("조건문 종료")

#    print("a는 10보다 커요") # IndentationError: expected an indented block after 'if' statement on line 16

# 조건문에 실행할 코드를 작성하지 않았을 때
# pass로 해당 조건문을 넘어갈 수 있음
#if a > 100:
#     pass

# 실습
weather = input("오늘의 날씨를 입력해주세요.: ")
if (weather == "비"):
    print("우산을 챙기세요!") # 오늘의 날씨를 입력해주세요.: 비 / 우산을 챙기세요!
if (weather == "맑음"):
    print("선크림을 바르세요!") # 오늘의 날씨를 입력해주세요.: 맑음 / 선크림을 바르세요!
    
    

# if - else 문
# 조건이 참일 때는 if문을 조건이 거짓일 때는 else문을 실행
# else -> ~아니라면 의 의미 -> 조건이 필요x, if 문과 반드시 같이 나와야함.

a= int(input())
if a > 10:
     print("a는 10보다 크다")
else:
   print("a는 10보다 작다")

# 실습 2
a = int(input("정수를 입력해주세요.: "))
b = a % 2
if (b == 0):
   print("짝수입니다.") # 12 / 짝수입니다.
else:
   print("홀수입니다.") # 13 /  홀수입니다.

# if - elif - else 문

# if - elif - else 구문
# elif : else if의 작자
# elif에서 조건을 반드시 기록
# if 가 있어야만 사용 가능

score = int(input())
if score >= 90:
     print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
     print("F")

# 실습 3

age = int(input())
if age >= 19:
     print("청소년 관람불가 가능") # 20 청소년 관람불가 가능
elif age >= 16:
     print("15세 이상 가능")  # 17 / 15세 이상 가능
elif age >= 13:
     print("12세 이상 가능") # 14 / 12세 이상 가능
else:
     print("전체 관람가") # 3 / 전체 관람가

# 실습 4
time  = int(input())
if (time < 60):
     print(time, "초") # 42 / 42초
elif (60 <= time, time < 3600):
     print((time // 60), "분", (time % 60), "초") # 89 / 1분 29초
elif (3600 <= time):
#    print((time // 3600), "시간", (time // 60), "분", (time % 60), "초") # 5419 / 1 시간 90 분 19초

 hour, minute, second = 0, 0, 0

 input_second = int(input())

 minute = input_second // 60
 second = input_second % 60
 hour = minute // 60
 minute %= 60

 if hour > 0:
     print(f"{hour}시간 {minute}분 {second}초")
 elif minute > 0:
     print(f"{minute}분 {second}초")
 else:
     print(f"{second}초")

# 중첩 조건문
# 하나의 if문 안에 또 다른 if문을 사용하는 것

username = input("관리자 아이디를 입력하세요: ")
password = input("비밀번호를 입력하세요: ")

if username == "admin":
     if password == "abcd":
         print("로그인 성공")
     else:
        print("로그인에 실패했습니다")
else:
     print("잘못된 사용자입니다")


# 실습 5

money = int(input())
food = input("음식이름을 넣어주세요: ")

if food == ("김밥"):
    if money >= 2500: 
        print("구매성공") # 2600 / 구매완료
    else:
        print("금액이 부족합니다.") # 2400 / 금액이 부족합니다
elif food == ("삼각김밥"):
    if money >= 1500:
        print("구매완료") # 1700 / 구매완료
    else:
        print("금액이 부족합니다.") # 1300 / 금액이 부족합니다
elif food ==("도시락"):
    if money >= 4000:
        print("구매완료") # 4500 / 구매완료
    else:
        print("금액이 부족합니다.") # 3700 / 금액이 부족합니다

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