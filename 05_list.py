'''
리스트 (List)
- 여러 값들을 순서대로 저장할 수 있는 자료형
- 인덱스(index): 각 값에 부여된 순서(0부터 시작)
- 가변 자료형(mutable): 원소의 추가/수정/삭제 가능
'''

# 리스트 만들기
list1 = [] # 빈 리스트
list2 = ["안녕하세요", "반갑슴니다"]
list3 = [10, "good", 3.14, [1,2,3,4]]

print(list1, list2, list3)

list4 = list()
list5 = list("Codingon")
print(list4, list5)


# ---------------------
# 인덱싱과 슬라이싱
my_list = [1,2,3,4,5]
print(my_list[0])
print(my_list[-1])
my_list[3] = -1
print(my_list)

# number = input("네 자릿수 정수를 입력하세요: ")
# 천 = number[0]
# 백 = number[1]
# 십 = number[2]
# 일 = number[3]
# print(천, 백, 십, 일)

# --------------
# 슬라이싱
my_numbers = [10,20,30,40,50,60,70,80,90,100]
print(my_numbers[1:4]) # [20,30,40]
print(my_numbers[3:]) # [40, 50, 60, 70, 80, 90, 100]
print(my_numbers[:4])
my_numbers[2:4] = [300,400]
print(my_numbers)

numbers = [10,20,30,40,50]
print(numbers[0]), print(numbers[4])

nums = [100,200,300,400,500,600,700]
print("new_list", [nums[2], nums[3], nums[4]])

nums = [1,2,3,4,5]
nums = [2,4,6,8,10]
print(nums[:])

items = ["a", "b", "c", "d", "e"]
print(items[::-1])

data = ["zero", "one", "two", "three", "four", "five"]
print(data[::2])

movies = ["인셉션", "인터스텔라", "어벤져스", "라라랜드", "기생충"]
movies[2:4] = ["매트릭스", "타이타닉"]
print(movies)

subjects = ["국어", "수학", "영어", "물리", "화학", "생물", "역사", "지구과학", "윤리"]
subjects[3::2]
print(subjects[3::2])

data = ["A", "B", "C", "D", "E", "F", "G", "H", "i"]
data1 = data[0:3]
data2 = data[3:6]
data3 = data[6:9]
print(data1[::-1], data2[::-1], data3[::-1])

# 인덱싱, 슬라이싱 주의 사항
my_list = [1,2,3,4]
# my_list[5] # IndexError: list index out of range 가 일어난다

my_list = [1,2,3,4,5]
print(my_list[4:1:2]) # 공백([])이 나옴
print(my_list[1:3:-1]) # 공백([])이 나옴

#-------------------------------
# 리스트 연산 - del
my_list = [10,20,30,40,50]
del my_list[2] # 특정 요소 삭제
print(my_list)
del my_list[1:3] # 슬라이스 범위 삭제
print(my_list)
del my_list # 리스트 삭제
# print(my_list) # NameError: name 'my_list' is not defined가 나옴

# 리스트 연결 - +
list1 = ["가", "나", "다"]
list2 = ["다", "라", "마"]
new_list = list1 + list2
# print(list1, list2, new_list, sep=" / ")

# 리스트 반복 - *
medal = ["금", "은", "동"]
new_list = medal * 3
# print(medal, new_list, sep=" / ")

#포함 여부 (in, not in)
fruits = ["토마토", "사과", "포도", "바나나", "수박"]
print("포도" in fruits)
print("참외" not in fruits)

fruits = ["apple", "banana", "cherry", "grape", "watermelon", "strawberry"]
del fruits[1:4]
print((fruits))

letters = ["A", "B"]
new_letters = letters * 3
del new_letters[2]
print(new_letters)

# ==================================
# 리스트 주요 메서드
# =============================

# 길이
number = [1,2,3,4,5]
print("1. len()", len(number), len("codingon"))

# 삽입
number.append(6)
number.append(7)
number.append(8)
print("2. append()", number)

number.insert(2, 2.5)
number.insert(4, 3.5)
print("3. insert()",  number)

number.extend([9,10])
print("4. extend", number)


# 삭제
number.append(2.5)
number.remove(2.5)
print("5. remove()", number) 

a = number.pop(1)
print("6. pop() 삭제한 요소", a)
print(number)
b = number.pop()
print("6. pop() 삭제한 요소", b)
print(number)

# 정렬
numbers1 = [3,2,1,4]
numbers1.sort()
print("7-1. sort()", numbers1) # 7-1. sort() [1, 2, 3, 4]
numbers1.sort(reverse=True)
print("7-1. sort(reverse=True)", numbers1) # 7-1. sort(reverse=True) [4, 3, 2, 1]

numbers2 = [50, 52, 53, 51]
new_numbers2 = sorted(numbers2)
new_numbers2_desc = sorted(numbers2, reverse=True)
print("7-2. sorted()", numbers2, new_numbers2, new_numbers2_desc)

# 뒤집기
my_numbers = [100, 101, 104, 103, 102]
my_numbers.reverse()
print("8-1. reverse()", my_numbers) # [102, 103, 104, 101, 100]

my_numbers2 = list(reversed(my_numbers))
print("8-2. reversed()", my_numbers2, my_numbers)

# count, min, max, sum
number3 = [1, 2, 2, 2, 2, 3, 4, 5, 6, 7]
print("9. count()", number3.count(2))
print("10. min/max", min(number3), max(number3))
print("11. sum", sum(number3))

# 실습
p1 = ["철수", "영희"]
p1.append("민수")
p1.append("지훈")
p1.pop(1)
p1.insert(0, "수진")
p1.pop(2)
p1.reverse()
print(p1)

num = [5, 3, 7]
num.extend([4, 9])
print(max(num), min(num))
print(sum(num))
num.sort()
num.pop(4)
print(num)