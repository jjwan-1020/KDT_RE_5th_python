# 사용자 입력 (input)
# - input 함수 : 콘솔을 통해 사용자로부터 문자열 형태로 입력 받음

# input 함수 사용법
my_input = input()("콘솔에 띄울 설명")
name = input("이름을 입력하세요: ")
print(name)

# 숫자로 활용 시 ' 형 변환' 필요
a = int(input())
b = int(input())
print(a + b)

c = float(input())
d = float(input())
print(c + d)

# 여러 자료 입력하기
# 문자열을 쪼개주는 함수 : spit()
# - 기본 구분자 : 공백
과일1, 과일2, 과일3 = input().split()
print(과일1, 과일2, 과일3)

# 다른 구분자 사용
apple, banana, grape = input().split("-")
print(apple, banana, grape)

name = input("이름을 입력하세요: ")
age = int(input("나이를 입력하세요: "))
print(f"안녕하세요. 저는 {name}이고, {age}살 입니다")

a = float(input())
b = float(input())
print("넓이:", a * b), print("둘레:", 2 * (a + b))

number = int(input("네 자리 수를 입력하시오"))
number1 = input('천의 자리: ')
number2= input('백의 자리: ')
number3= input('십의 자리: ')
number4 = input('일의 자리:')
print(number, number1, number2, number3, number4)

이름1, 이름2, 이름3 = input("발표자 이름 3명을 입력해주세요: ").split()
주제1, 주제2, 주제3 = input("주제 3개를 입력해주세요: ").split()
print(f'''발표순서및 주제입니다
1조 발표자: {이름1} -주제1: {주제1}
2조 발표자: {이름2} -주제2: {주제2}
3조 발표자: {이름3} -주제3: {주제3}''')

년도, 월, 일 = input("년, 월, 일을 입력해주세요").split()
시간, 분, 초 = input("시간, 분, 초를 입력해주세요").split()
print(f'''"RED의 개강일은 {년도}년 {월}월 {일} 입니다
시작시간은 {시간}시 {분}분 {초}초 입니다"''')

