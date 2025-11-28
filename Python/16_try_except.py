# 예외처리
# - 에러: 프로그램이 실행이 되지 않게 하는 문제
# - 예외: 에러가 발생될 것 같은 부분을 예외로 처리
# => 프로그램이 예기치 않게 종료되는 것을 방지

# 예외 처리 기본 문법
try:
    # 예외가 발생할 수 있는 코드
    pass
except:
    pass
    # 예외가 발생했을 때 실행할 코드
    # 특정 에러를 지정 가능


# 예외 종류
# 1. 인덱스 에러
# - 리스트 인덱스 범위 오류
shop = ['반팔', '청바지', '이어폰', '키보드']
print(shop[2])
# print(shop[10]) # File IndexError: list index out of range
print("예외처리")

# ValueError
# - 부적절한 값을 가진 인자를 받았을 때 발생
# number = int("hello") # ValueError: invalid literal for int() with base 10: 'hello'
# print(shop.index("x")) # ValueError: list.index(x): x not in list

# 3. ZeroDivisionError
# - 0으로 나눌 때 발생
# print(5 / 0) # ZeroDivisionError: division by zero

# 4. NameError
# - 존재하지 않는 변수를 호출할 때
# print(x) # NameError: name 'x' is not defined

# 5. FileNotFoundError
# - 존재하지 않는 파일을 호출할 때
# file = open('test.txt') # FileNotFoundError: [Errno 2] No such file or directory: 'test.txt'

# 예외 처리
#try:
#    num = int(input("숫자를 입력하세요: "))
#    print(10 / num)
#except:
#    print("예외 발생")

# 2) 특정 예외 처리
try:
    num = int(input("숫자를 입력하세요: "))
    print(10 / num)
except ValueError as e:
    print("숫자가 아닙니다", e)
except ZeroDivisionError as e:
    print("0으로 나눌 수 없습니다", e)

# 예외 처리 구조
'''
try:
    # 예외가 발생할 수 있는 코드
    pass
except 오류내용1:
    pass
    # 예외가 발생했을 때 실행할 코드
    # 특정 에러를 지정 가능
except 오류내용2:
    # 특정 에러 2
else:
    # 예외 없는 경우에 실행
flnally:
    # 예외 발생 여부와 상관없이 실행
'''
# 실습 1
try:
    number = int(input("숫자를 입력하세요: "))
except ValueError as er:
    print(er)
    number1 = -1
if number > 0:
    print("0보다 큽니다.")
else:
    print("숫자가 아닙니다")

# 실습 2
def calc(n1, oper, n2):
    if oper == "+": # 5 + 9 = 14
        return n1 + n2
    elif oper == "-": # 857 - 256 = 601
        return n1 - n2
    elif oper == "*": #9 * 4 = 36
        return n1 * n2
    elif oper == "/":
        return n1 / n2 # 652 / 36 = 18.1111111
while True:
    try:
        n1 = int(input("첫 번째 숫자를 입력하세요: "))
        break
    except ValueError as er1:
        print(er1, "숫자가 아닙니다")
while True:
    oper = input("연산자를 입력하세요: ")
    if oper in ["+", "-", "*", "/"]:
        break
    else:
        print("올바른 연산자가 아닙니다. 다시 입력해주세요.")
while True:
    try:
        n2 = int(input("두번째 숫자를 입력해주세요: "))
        break
    except ValueError as er2:
        print(er2, "숫자가 아닙니다. 다시 입력해주세요.")

result = calc(n1, oper, n2)
print(n1, oper, n2, "=", result)

