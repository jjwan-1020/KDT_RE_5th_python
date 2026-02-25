# 모듈(module)
# - 여러 기능(함수)의 묶음
# - 하나의 py파일로 여러 기능을 모아놓은 것

# 모듈 불러오기(1)
import hellow
hellow.greeting("lee")

# 모듈 불러오기(2)
from hellow import greeting

greeting("kim")

# 모듈 불러오기(3)
from hellow import *
introduce("sin", 20)

# 모듈 불러오기(4)
import hellow as h 
h.greeting("Jeong")


# 패키지
# 모듈의 묶음
# 모듈을 폴더 단위로 묶어놓은 것

# 패키지에서 모듈 불러오기(1)
from my_package import calc as c
c.add(10,20)

# 패키지에서 모듈 불러오기(2)
from my_package.calc import add
add(10,20)

# 파이썬 표준 라이브러리

# math모듈: 수학적 연산에 사용되는 모듈
import math as m

# 1. 올림/내림
# ceil: 올림, 소수점 지정 x 
print(m.ceil(3.14))

# floor: 내림, 소수점 지정 x
print(m.floor(3.14))

# round: 반올림 - 내장 함수
print(round(3.141592, 2))

# 2. 제곱, 제곱근
# pow(x, y): 제곱 - x^y
m.pow(2, 3)

# sqrt(x): 제곱근 반환
m.sqrt(16)

# 3. 상수
# pi: 원주율
print(m.pi)

# 4. 수학 계산 편의 기능
print(m.factorial(3))
# 최대 공약수
print(m.gcd(12, 20))
# 최소 공배수
print(m.lcm(12,20))

# 실습
'''
import math

x1 = float(int(input("x1입력: ")))
y1 = float(int(input("y1입력: ")))
x2 = float(int(input("x2입력: ")))
y2 = float(int(input("y2입력: ")))

dis = math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2))
print(f"두점 사이의 거리: {dis:.2f}")

import math
s = 18
t = 24
gcd_st = math.gcd(s, t)
lcm_st = math.lcm(s, t)
print(f"공평하게 나눠 가질 수 있는 최대 간식개수: {gcd_st}개")
print(f"포장 단위별 동시에 맞게 나눠 떨어지즌 최소 간식 개수: {lcm_st}개")
'''
print("==========================")
# random 모듈: 랜덤 값(난수) 생성 시 사용
import random

# 1. 난수 생성

# random(): 0이상 1미만의 float난수 반환
print(random.random())

# uniform(a,b): a 이상 b이하의 실수 난수 반환
print(random.uniform(1,10))

# randint(a,b): a 이상 b 이하의 정수 난수 반환
print(random.randint(1,100))

#randrange(start, stop, step): 범위 안의 정수 난수 반환, 간격 지정 가능
print(random.randrange(0,100,5))

# 2. 랜덤 선택
fruits = ["apple", "banana", "watermelon", "grape", "orange"]

# choices(seq): 시퀀스에서 임의의 요소 1개 반환
print(random.choice(fruits))

# choices(seq,k): 시퀀스에서 "중복 혀용" k개 요소 리스트를 반환
print(random.choices(fruits, k=2))

# 3. 섞기
# sample(seq,k): 시퀀스에서 "중복 없이" k개 요소 리스트를 반환
print(random.sample(fruits, k = 2))

# suffle(seq): 시퀀스의 요소를 무작위로 섞음 -> 원본 시퀀스를 변경
numbers = [1,2,3,4,5]
print(random.shuffle(numbers))
print(numbers)


# 실습 3
import random
num = random.sample(range(1,46),6)
num.sort()
print(num)
'''
import random
choices = ['가위', '바위', '보']
cpu = random.choice(choices)
user = input("가위, 바위, 보 중 하나를 입력하세요.: ")
print(f"컴퓨터: {cpu}")

if user == cpu:
    print("무승부")
elif (user == '가위' and cpu == '보') or \
     (user == '바위' and cpu == '가위') or \
     (user == '보' and cpu == '바위'):
    print("승리")
else:
    print("패배")
'''

# datetime 모듈
# 날짜와 시간의 생성, 조작, 현실 변환과 같은 시간 관련 기능을 제공
import datetime

# 1. 날짜/시간 구하기
# 현재 날짜와 시간 구하기
now = datetime.datetime.now()
print(now)

# 오늘 날짜만 구하기
today = datetime.date.today()
print(today)

# 2. 날짜/시간 형식 변환
formatted = now.strftime("%Y/%m/%d %H:%M:%S")
print(formatted)

parsed = datetime.datetime.strptime(formatted, "%Y/%m/%d %H:%M:%S")
print(parsed)

# 3. 날짜/시간 연산
dt = datetime.date(2025, 7, 7)
passed_time = today - dt
print(f"{passed_time.days}일이 지났습니다.")

# 4. 요일반환: weekday
# 0: 월요일 ~ 7:일요일
days = ["월", "화", "수", "목", "금", "토", "일"]
day_num = today.weekday()
days[day_num]
print(days[day_num])

# datetime 또는 date 객체에는 년/월/일 시간 등이 속성으로 들어있다
print(datetime.datetime.now().year)

# 실습 5

#from datetime import datetime
#birthday_input = input("생일을 입력해주세요.(예: 07-25): ")

#month, day = map(int, birthday_input.split("-"))
#today = datetime.today()
#birthday = datetime(today.year, month, day)
#
#if birthday < today:
#    b_next = datetime(today.year + 1, month, day)
#    d_left = (b_next - today).days
#else:
#    d_left = (birthday - today).days
#print(f"생일까지 남은 일수는 {d_left}일 입니다.")


# calender 모듈
# 날짜와 달력 관련 기능을 제공

import calendar

# 1. 달력 조회
print(calendar.prmonth(2025, 9))
print(calendar.prcal(2025))

# 텍스트로 값을 반환
print(calendar.month(2025, 11))

# 요일 반환
print(calendar.weekday(2025, 11, 26))


# time 모듈
# 시간의 측정, 지연, 변환과 같은 시간 관련 기능 제공
import time

# 1. 시간 변환
# time()
# Unix 타임스탬프로 반환(1970.1.1부터 경과 초)
print(time.time())

#ctime(): 현재 시간을 문자열로 반환
print(time.ctime())
print(time.ctime(0)) # 기준시로 반환 (1970.1.1)

# strftime(): 원하는 포맷의 문자열로 시간 객체 변환
lt = time.localtime()
formatted = time.strftime("%Y-%m-%d %H:%M:%S", lt)
print(formatted)

# strptime(): 문자열을 struct_time 객체로 변환
parsed = time.strptime(formatted, "%Y-%m-%d %H:%M:%S")
print(parsed)

# 2. 시간 지연
# sleep(seconds): 지정한 초만큼 프로그램이 일시 정지
time.sleep(1)
print("time sleep")

# 시간 측정하기
start = time.time()

for i in range(5):
    print(i)
    time.sleep(1)

end = time.time()
print(f"수행시간: {end - start: .2f}초")


# 실습 6
'''
import random
import time

word = ["apple", "banana", "orange", "grape", "lemon", "peach", "melon", "cherry",
        "plum", "pear", "school","friend","family","flower","garden","window","bottle",
        "pencil","summer","winter","happy","future","travel","animal","market","doctor",
        "planet","energy","nature","memory"]

input("게임을 시작하려면 엔터키를 누르세요")
correct_count = 0
total_word = 10
start_time = time.time()
random.shuffle(word)

for i in range(1, total_word + 1):
    words = word[i - 1]
    print(f"\n 문제 {i}: {words}")
    user_input = ""
    while user_input != words:
        user_input = input("입력 >> ")
        if user_input == words:
            print("다음")
            correct_count += 1
        else:
            print("오타입니다. 다시 도전해주세요.")

end_time = time.time()
total_time = end_time - start_time


print("종료되었습니다.")
print(f"통과한 문제 수: {correct_count} / {total_word}")
print(f"총 타자 시간: {total_time: .2f}초")
'''

# sys모듈
# 파이썬 인터프리터와 관련된 다양한 기능 제공
import sys

# 파이썬 버전 정보
print(sys.version)

# 운영체제 정보
print(sys.platform)

# 프로그램 종료
print("프로그램 시작")
# sys.exit() # 강제종료
# print("실행되지 않는 코드")

# os 모듈
# 운영체제와 상호작용 할 수 있도록 도와주는 기능 제공
import os

# getcwd(): 현재 작업 디렉토리 반환
print(os.getcwd())

# listdir():현재 폴더 내 파일, 디렉토리 목록 반환
print(os.listdir())

# 폴더 생성
folder_name = "sample_folder"
if not os.path.exists(folder_name):
    os.mkdir(folder_name)
else:
    print(f"{folder_name} 폴더가 이미 존재합니다.")

print(os.listdir())