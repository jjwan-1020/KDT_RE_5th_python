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