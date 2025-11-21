# 함수 실습

def calculate(a, b, operator):
    if operator == "+":
        return a + b
    elif operator == "-":
        return a - b
    elif operator == "*":
        return a * b
    elif operator == "/":
        return float(a / b)
    else:
        return "지원하지 않는 연산입니다"
    
print(calculate(20, 30, "+"))
print(calculate(10, 30, "-"))
print(calculate(10, 30, "*"))
print(calculate(60, 5, "/"))
print(calculate(20, 10, "^"))

def average(*arge):
    if len(arge) == 0:
        return ""
    return sum(arge) / len(arge)
print(average(20, 35, 49, 50, 13, 1))

def l_words(*arge):
    if len(arge) == 0:
        return ""
    return max(arge, key=len)
print(l_words("apple", "watermelon","kiwi","melon","pear"))


def average(*args):
    if len(args) == 0:
        return "입력값이 없습니다"
    return sum(args) / len(args)
print(average(1,2,3))

def longgest(*args):
    answer = ""
    for s in args:
        if len(s) > len(answer):
            answer = s
    return answer
print(longgest("apple","watermelon","pear"))

def longgest2(*args):
    if len(args) == 0:
        return "입력값이 없습니다"
    return max(args, key=len)

longgest2()

# dict.items()활용

def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="j", age=10, city="서울", job="student")

def discount_price(**kwarge):
    for key, value in kwarge.items():
        discount = value * 0.9
        print(f"{key}: 할인가 {discount} (원가 {value})")

discount_price(apple=3000, watermelon=12000, chocolate=4000)


# 전역 변수
current_user = None         # 현재 로그인 사용자
login_attempts = 0          # 로그인 실패 횟수
MAX_ATTEMPTS = 3            # 최대 허용 실패 횟수


def login(name, password):
    global current_user, login_attempts

    # 3회 실패 시 로그인 차단
    if login_attempts >= MAX_ATTEMPTS:
        print("로그인 시도 횟수를 초과했습니다. 더 이상 로그인할 수 없습니다.")
        return

    # 이미 로그인한 상태
    if current_user is not None:
        print("이미 로그인되어 있습니다.")
        return

    # 예시 계정
    correct_name = "admin"
    correct_password = "1234"

    # 로그인 성공
    if name == correct_name and password == correct_password:
        current_user = name
        login_attempts = 0  # 성공하면 실패 횟수 초기화
        print(f"{current_user} 님이 로그인했습니다.")
    else:
        login_attempts += 1
        print(f"로그인 실패! (실패 {login_attempts}회)")

        # 3번 실패 시
        if login_attempts >= MAX_ATTEMPTS:
            print("로그인 시도 횟수가 초과되어 계정이 잠겼습니다.")


def logout():
    global current_user
    if current_user is None:
        print("로그인 상태가 아닙니다.")
    else:
        print(f"{current_user} 님이 로그아웃되었습니다.")
        current_user = None


# 실행 예시
login("admin", "0000")   # 실패 1회
login("admin", "1111")   # 실패 2회
login("admin", "2222")   # 실패 3회 → 계정 잠김
login("admin", "1234")   # 더 이상 로그인 불가
logout()                 # 로그인 안돼서 로그아웃도 불가


# 11.21
# 실습
def power_rec(a,b):
    if b == 0:
        return 1
    return a * power_rec(a, b-1)
    # a * a * a* ... *1 (=> b = 0)
print("재귀함수", power_rec(2,3))
# 2 * 2 * 2 * 1 => b = 3, b = 0이 되는 순간까지 포함 총 4개 곱



def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)

print("팩토리얼", factorial(5))


def f_num(n):
 if n <= 0:
     return [0]
 elif n == 1:
     return [0]
 a_num = [0,1]
 for n in range(1,n):
     a_num.append(a_num[-1] + a_num[-2])
 return a_num

print(f_num(3))

def fib_num(n):
    if n <= 0:
        return 0 
    a, b = 1, 1

    for n in range(1, n-1):
        a, b = b, a + b
    return b
print(fib_num(7))
     

def fib_num2(c):
    if c <= 0:
        return 0
    elif c <= 2:
        return 1
    return fib_num2(c-1) + fib_num2(c-2)

print(fib_num2(6))

students = [("Alice", [80,90]), ("Bob", [60,65]), ("Charlie", [70,70])]
print(list(filter(lambda s: sum(s[1] )/ len(s[1]) >= 70, students)))

sentences = ["Python is fun", "Lambda functions are powerful", "Coding is creative"]
print(list(map(lambda str: str.split()[0], sentences)))

people = [("Alice", 30), ("Bob", 25), ("Charlie", 35)]
print(sorted(people, key=lambda x : x[1]))