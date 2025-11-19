# for 문
# - 이터러블(순회가 가능한) 요소를 하나씩 꺼내서 실행 블록에 전달하는 반복문

# 리스트 반복
fruits = ['apple', 'banana', 'cherry']
for fruit in fruits:
    print(f"I like {fruit}")

# 문자열 반목
my_str = "Apple"
for char in my_str:
    print(char)

# 튜플 반복
# coords = [(1,2), (10,15), (-6,8)]
# 언패킹 (구조분해 가능)
# for x,y in coords:
#     print(f"x좌표: {x}, y좌표: {y}")

# 딕셔너리 반복
person = {
    "name": "kim",
    "age": 15,
    "address": "seoul"
}

# 기본
for key in person:
    print(f"key: {key}, value: {person[key]}")

# value 만 가져오기
for value in person.values():
    print(f"value: {value}")

# item 가져오기
for key, value in person.items():
    print(f"key: {key}, value: {value}")

# set 반복
# my_set = {1,2,3,4}

# for s in my_set:
#    print(s)


# 실습

numbers = [3,6,1,8,4]
for num in numbers:
    print(num*2)

words = ["apple", "banana", "kiwi", "grape"]
for f_list in words:
    word = len(f_list)
    print(word)

    



coordinates = [(1,2), (3,4), (5,6), (7,8)]
for x_values,y_values in coordinates:
    print(f"x죄표: {x_values}, y죄표: {y_values}")

#-------------------------------------------------------

# for문 range()
# range 함수: 지정된 범위의 정수 시퀀스 생성

# 기본 문법
# range(start, end, step)
# - start: 생략 가능. 가본값 0
# - end: end-1 까지 생성
# - step: 생략 가능. 기본값 -1

range(1,5)

for i in range(1, 5):
    print(i)

for i in [1,2,3,4]:
    print(i)

print("========================")

# start 생략
for i in range(10):
    print(i)

# 간격 (step)지정
for i in range(0,11,2):
    print(i)

for i in range(11,0,-2):
    print(i)

print("===================")
# 실습
'''
n = int(input())
for num in range(1,n):
    n += num
print(n)


z = int(input())
for number in range(1, 10):
    print(f"{z}x{number} = {z*number}")

print("================")

t = 0
for num in range(3, 101, 3):
    t += num
print(t)

total = int(input("숫자를 입력하세요: "))
for o in range(1, total+1):
    if o % 2 == 0 and o % 5 ==0:
        print(o)
'''


# 루프 제어문
# - 특정 조건 하에서만 작동하도록 구현

# break: 반복을 즉시 중단
'''
for i in range(10):
    if i == 5:
        break
    print(i)
print("반복 종료")


# continue: 현재 반복을 넘어감
for i in range(5):
    if i == 2:
        print("continue = 건너뜀")
        continue
    print(i)

print("반복 종료")
'''
# pass
for i in range(10):
    pass

# for - else 구문
for i in range(5):
    if i == 2:
        break
    print(i)
else:
    print("반복 종료")

# 중첩 for문
# - 하나의 for문 안에 다른 for문이 들어있는 구조

# 이중 for문 
for i in range(5):
    for j in range(5):
        print("i, j", i, j)
    print()

# 실습

for x in range(2, 10):
   print(f"{x}단")
   for y in range(1, 10):
       print(f"{x} x {y} = {x * y}")
# 왼쪽 정렬
    
n = int(input("몇 줄?: "))

for i in range(1, n+1):
    for j in range(i):
        print("*", end="")
    print()

# 오른쪽 정렬
n = int(input("몇 줄?: "))
for i in range(1, n+1):
    for j in range(n - i):
        print(" ", end="")
    for j in range(i):
        print("*", end="")
    print()

# 가운데 정렬
n = int(input("몇 줄?: "))

for i in range(1, n+1):
# 공백 줄력
    for j in range(n - i):
        print(" ", end="")
    for j in range(2 * i - 1):
        print("*", end="")
    print()



# 리스트 컴프리헨션
# - for문을 리스트에 한줄로 축약하여 새 리스트를 생성하는 문법
# - [표현식(리스트의 원소) for 변수 in 반복대상 if 조건]
# - 표현식 : 값을 유도하는 식 (표현)

# for문 이용
squares = []
for x in range(1,6):
    squares.append(x ** 2)
print(squares)

#리스트 컴프리헨션
squares2 = [x ** 2 for x in range(1,6)]
print(squares2)

# 조건문 추가하기
squares3 = [x ** 2 for x in range(1,11) if x % 2 == 0]
print(squares3) 



# 실습
num = [number ** 2 for number in range(1,11)]
print(num)

n_list = [total for total in range(1, 51) if total % 3 == 0]
print(n_list)

fruits = ["apple", "fig", "banana", "plum", "cherry", "pear","orange"]
f_list = [fruit for fruit in fruits if len(fruit) >= 5]
print(f_list)