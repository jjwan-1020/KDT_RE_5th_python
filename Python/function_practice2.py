# 실습

current_user = None
login_count = 0

def login(name):
    global current_user
    global login_count

    if current_user == None:
        current_user = name
        print(f"{name}님이 로그인에 성공하셨습니다.")
    else:
        print("이미 로그인되어 있습니다.")
        login_count += 1
        if login_count > 4:
            print("더 이상 로그인 시도를 할 수 없습니다.")


def logout():
    global current_user
    global login_count
    
    if current_user == None:
        print("로그인 상태가 아닙니다.")
    else:
        print("로그아웃 되었습니다.")
        current_user = None
        login_count = 0

logout()
login("lee")
login("kim")
logout()


def num(a,b):
    if b == 0:
        return 1
    elif b == 1:
        return a
    return a * num(a, b-1)

print(num(2,4))


# 팩토리얼
def factorial_for(n):
    if n < 0:
        return "음수의 팩토리얼은 정의되지 않았습니다"
    if n == 0 or n == 1:
        return 1
    return n * factorial_for(n-1)

print(factorial_for(5))

# 피보나치 수열
def fibonacci_for(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    
    a,b = 0,1
    for _ in range(1,n-1):
        a,b = b,a+b
        # 0 1 <= 1 1
        # 1 1 <= 1 2
        # 1 3 <= 2 3
        
        return b
    
print(fibonacci_for(6))


# 재귀함수
def fibonacci_for(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    
    return fibonacci_for(n-1) + fibonacci_for(n-2)

print(fibonacci_for(6))


# 람다 함수 실습(Leader)
