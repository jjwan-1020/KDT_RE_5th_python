# 파일 입출력
#  - 저장장치에 저장된 파일을 읽어오거나 저장하는 작업

# 파일 열기와 닫기
# 파일 열기 : open()
# open("파일 경로", mode="r", encoding="원하는 입코딩 - utfe")
# open으로 파일을 읽으면 '파일 객체'를 반환
f = open("example.txt", "w", encoding="utf-8")

f.write("파이썬 파일 입출력 예제\n")
f.write("파이썬 공부!!")

# 파일 닫기: close()
# 열린 파일을 닫아 시스템 자원을 헤제함

f.close()

# 파일 읽기
# read(): 전체 내용을 한번에 읽기
f = open("example.txt", "r", encoding="utf-8")
content = f.read()
print(content)
f.close()

# readline(): 한 줄씩 순차적으로 읽기
f = open("example.txt", "r", encoding="utf-8")
line1 = f.readline()
line2 = f.readline()
print("첫 번째 줄:", line1.strip())
print("두 번째 줄:", line2)
f.close()


# for문으로 읽기
f = open("example.txt", "r", encoding="utf-8")
for line in f:
    print(line.strip())
f.close()


# readlines(): 모든 줄을 한번에 리스트로 읽기
f = open("example.txt", "r", encoding="utf-8")
contents = f.readlines()
print(contents)
f.close()

# tell(): 현재 읽고 있는 위치(바이트)를 반환
f = open("example.txt", "r", encoding="utf-8")
print("처음 위치:", f.tell())
f.read(5)
print("5바이트 읽은 후 위치:", f.tell())
f.close()


# seek(): 파일 포인터 위치를 이동
f = open("example.txt", "r", encoding="utf-8")
print(f.read(10)) # 10바이트를 읽기
f.seek(0) # 파일의 맨 처음으로 이동
print(f.read())
f.close()

# a 모드: 추가 쓰기
f = open("example.txt", "a", encoding="utf-8")
f.write("\n추가한 내용입니다.")
f.close()


# with 문
# 파일 입출력시에 자동으로 close()를 호출해주는 구문
# 파일 쓰기
with open("with_example.txt", "w", encoding="utf-8") as f1:
    f1.write("with문으로 작성한 파일입니다.\n")
    f1.write("파일 입출력 완료")


# 에제 1. 파일에서 랜덤 추출
with open("words.txt", "w", encoding="utf-8") as f1:
    words = ["apple", "banana", "orange", "grape", "lemon",
      "peach", "melon", "cherry", "plum", "pear",
      "school", "friend", "family", "flower", "garden",
      "window", "bottle", "pencil", "summer", "winter",
      "happy", "future", "travel", "animal", "market",
      "doctor", "planet", "energy", "nature", "memory"
      ]
    for i in words:
        f1.write(i + "\n")

import random

with open("words.txt", "r", encoding="utf-8") as f1:
    data = f1.readlines()
    for i in range(5):
        word = random.choice(data).strip()
        print(word)


# 예제 2. 입력 받아 파일 쓰기
'''
with open("with_example.txt", "a", encoding="utf-8") as f1:
    while True:
        text = input("저장할 내용을 입력해주세요.(종료 : z)")
        if text == "Z" or text =="z":
            break
        f1.write(text + "\n")
'''


# 실습 1
'''
import os
with open("member.txt", "w", encoding="utf-8") as f2:
    for i in range(3):
        name = input(f"{i + 1}번째 회원의 이름을 입력하시오.: ")
        password = input(f"{i + 1}번째 회원의 비밀번호를 입력하시오.: ")
        f2.write(f"{name} {password}\n")

print("\n회원님의 정보가 member.txt에 저장되었습니다.")

input_name = input("이름을 입력하시오.: ").strip()
input_password = input("비밀번호를 입력하시오.: ").strip()

with open("member.txt", "r", encoding="utf-8") as f2:
    for line in f2:
        name, password = line.strip().split()
        if input_name == name and input_password == password:
            login_success = True
            break
    else:
        print("로그인 실패")
        exit()
print("로그인에 성공했습니다.")

tel = input("전화번호를 입력하세요.: ")
if os.path.exists("member_tel.txt"):
    with open("member_tel.txt", "r", encoding="utf-8") as f3:
        tel_lines = f3.readlines()
else:
    tel_lines = []
for line in tel_lines:
    saved_name, saved_tel = line.strip().split()
    if saved_name == input_name:
        if saved_tel == tel:
            print("이미 존재하는 번호 입니다.")
        else:
            new_tel = input("새로운 전화번호를 입력해주세요.: ")
            print("새로운 전화번호가 등록되었습니다.")
''' 
            
# 바이너리 파일 읽기
import os
print(os.getcwd())
with open('./Python/images/recycle.jpg', 'rb')as f:
    img = f.read()
    print(img)

# 바이너리 파일 쓰기
with open("./Python/images/recycle_copy.jpg", "wb") as f:
    f.write(img)


# pickle모듈
# - 객체의 형태를 유지하면서 파일에 저장하고 불러올 수 있음

import pickle
# 리스트, 딕셔너리 파일 저장
with open('pickle.txt', 'wb') as f:
    li = ['dog', 'cat']
    dic = {1: 'dog', 2: 'cat'}

    pickle.dump(li, f)
    pickle.dump(dic, f)

# 읽기
with open('pickle.txt', 'rb') as f:
    li = pickle.load(f)
    dic = pickle.load(f)
    print(li, dic)
