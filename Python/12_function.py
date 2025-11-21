'''
함수(function)
- 특정 작업을 수행하는 코드들의 모음이다
- 복잡한 코드를 작은 단위로 나눌 수 있게 도와줌
- 특정한 코드들을 재사용 할 수 있게 함
'''

# 사용자 정의 함수 기본 문법
# 함수의 정의 : define의 약자로 def를 사용
def 함수이름(매개변수):
    # 실행할 코드
    print(매개변수)
    return "반환값"

# 함수의 실행(호출 call)
result = 함수이름("인자")
print(result)

# 매개변수(Parameter): 매개 + 변수
# 매개: 둘 사이를 연결해줌
# 햄수가 실행될 때 인자로부터 입력되는 값을 함수의 코드블록으로 전달하는 역할


# 함수의 필요성 예제
'''
a = 10
b = 20

if a > b:
    print(a - b)
else:
    print(a + b)

c = 30
d = 40

if c > d:
    print(c - d)
else:
    print(c + d)

# ......

def my_func(a,b):
    if a > b:
        return a - b
    else:
        return a + b
'''  
#print(my_func(10,20))
#print(my_func(30,40))


# 실습
def calculate(a, b, operator):
    if operator == "+":
        return a + b
    elif operator == "-":
        return a - b
    elif operator == "*":
        return a * b
    elif operator == "/":
        return(float(a / b))
    else:
        return("지원하지 않는 연산입니다")
    
print(calculate(8, 6, "+" ))
print(calculate(3, 9, "-"))
print(calculate(82, 12 , "*"))
print(calculate(875, 521, "/"))
print(calculate(60, 50 , "^"))



# 키워드 인자
# 예시 1.
'''
print("안녕하세여", "반갑습니다", sep="-", end= " / ")

# 예시 2.
def my_func(a, b, c=None, operator=None):
    if operator == "+":
        return a + b
    else:
        return c
    
print(my_func(10,20, operator="+"))
    

# 기본값 인자
# 단, 기본값 매개변수는 뒤쪽에 위치해야함
def greet(name, message="안녕하세요~!"):
    print(f"{name}님, {message}")

# 호출 시 인자 생략 -> 기본값 사용
greet("jjwan") 
greet("jj", "반갑습니다")

# 위치 가변 인자
# 여러개의 값을 유동적으로 받을 수 있다
# 값이 튜플 형태로 받아진다

def add_all(*args):
    return sum(args)

print(add_all(1,2,3,4,5))

# 키워드 가변 인자
# 여러 키워드 인자를 유동적으로 받을 수 있다
# 딕셔너리 형태로 값이 입력됨

def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} : {value}")

print_info(name="jjwan", age=26, city="pohang")
'''
# 실습
'''
def average(*args):
    if len(args)== 0:
        return 0
    return sum(args) / len(args)
print(average(10, 16, 20, 60))

def l_words(*args):
    if len(args) == 0:
        return ""
    return max(args, key=len)
print(l_words("apple", "banana","watermelon", "pear","orange"))

def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} : {value}")

print_info(name="jjwan", age=26, city="pohang", email="jj1020@naver.com")

def d_count(**kwargs):
    for item, price in kwargs.items():
        discount = price * 0.9
        print(f"{item} : {discount}원")

d_count(apple=3000, banana=4500, kiwi=240)



# 전역 변수: 함수 밖에 선언된 변수
# 지역 변수: 함수 안에 선언된 변수

# 전역 변수
x = 200

#예제
def my_func():
    # 지역변수
    x = 10
    print(x)

my_func()
print("함수 밖", x)


# 예제 2 (global 사용 예제)
'
x = 10

def my_func2():
    #x = 20
    x +=5
    print("지역변수", x)

my_func2()

print("전역변수", x)


# 예제 2 (UnboundLocalError 에러)




# 예제 3 (global 사용)
x = 10

def my_func3():
   global x
x +=5
print("지역", x)

my_func3()

print("전역", x)



# 권장되는 패턴
# 부수효과 (side effect)를 발생시키지 않는 함수를 위주로 프로그래밍

x = 10
def my_func4(x):
    x +=5
    return x

x = my_func4(x)

print("전역", x)



# 실습
current_user = ""

def login(u_name):
    global current_user
    if current_user:
        print(f"{u_name}님이 이미 로그인되어 있습니다")
    else:
        current_user = u_name
        print(f"{u_name}님이 로그인했습니다")

def logout():
    global current_user
    if not current_user:
        print("로그인 상태가 없습니다")
    else:
        current_user = ""
        print("로그아웃되었습니다")

login("jjwan")
login("codingon")
logout()
logout()
login("codingon")
print(current_user)
'''


current_user = None         
login_attempts = 0         
MAX_ATTEMPTS = 5         


def login(name, password):
    global current_user, login_attempts

    
    if login_attempts >= MAX_ATTEMPTS:
        print("로그인 시도 횟수를 초과했습니다. 더 이상 로그인할 수 없습니다.")
        return

   
    if current_user is not None:
        print("이미 로그인되어 있습니다.")
        return

   
    correct_name = "admin"
    correct_password = "1234"

   
    if name == correct_name and password == correct_password:
        current_user = name
        login_attempts = 0  
        print(f"{current_user} 님이 로그인했습니다.")
    else:
        login_attempts += 1
        print(f"로그인 실패! (실패 {login_attempts}회)")

        
        if login_attempts >= MAX_ATTEMPTS:
            print("로그인 시도 횟수가 초과되어 계정이 잠겼습니다.")


def logout():
    global current_user
    if current_user is None:
        print("로그인 상태가 아닙니다.")
    else:
        print(f"{current_user} 님이 로그아웃되었습니다.")
        current_user = None



login("admin", "0000")   
login("admin", "1111")   
login("admin", "2222")   
login("admin", "3333") 
login("admin", "4545")
login("admin", "5554")  
logout()                 


# 재귀함수
# 1. 자기 자신을 호출하는 함수
# 2. 반드시 기본 조건 (종료 조건)이 있어야 함
# - 큰 문제를 작은 문제로 나누었을 때 일정한 패턴이 있어야 한다

import time


def recursive_func(n):
    #기본 조건
    if n == 0:
        return
    
    recursive_func(n-1)
    print("재귀 호출", n)
    time.sleep(0.05)

recursive_func(5)
    

# 실습

def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)

print("팩토리얼", factorial(5))


# 람다 (lambda) 함수
# 익명 함수
# 간단한 함수를 한줄로 표현할 때 사용

# 람다 함수의 기본 문법
# lambda 매개변수: 표현식
# - 표현식: 값이 반환되는 식

# 일반 함수
def add(x, y):
    return x + y

# 람다 함수
add_func = lambda x, y: x + y
print(add_func(3,5))

# 람다로 값을 반환하고 사용을 끝내는 경우
print((lambda x: x ** 2)(10))

# 람다 함수의 활용
# 1. map 에서 활용
my_list = [1,2,3,4]

# 일반 함수를 사용
def square_func(x):
    return x **2

# 함수를 인자로 받는 함수
print(list(map(square_func, my_list)))

# 람다함수를 사용
print(list(map(lambda x: x ** 2, my_list)))

#  filter 에서 활용
my_list2 = [1,2,3,4,5,6,7,8,9,10]

# 일반 함수 사용
def is_even(x):
    return x % 2 == 0
print(list(filter(is_even, my_list2)))

print(list(filter(lambda x: x % 2 == 0, my_list2)))

# 3. sorted 에서 활용

my_list3 = ["apple", "banana", "watermelon", "grape"]
print(sorted(my_list3, key=lambda word: len(word)))


# 실습

students = [("Alice", [80,90]), ("Bob", [60,65]), ("Charlie", [70,70])]
print(list(filter(lambda s: sum(s[1]) / len(s[1]) >= 70, students)))


sentences = ["Python is fun", "Lambda functions are powerful", "Coding is creative"]
print(list(map(lambda str: str.split()[0], sentences)))

people = [("Alice", 30), ("Bob", 25), ("Charlie", 35)]
print(sorted(people, key=lambda x: x[1]))

