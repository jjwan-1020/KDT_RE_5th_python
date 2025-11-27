# 실습 (Leader)
import os
if os.path.exists("m_leader.txt"):
    print("m_leader.txt가 이미 존재합니다. 회원 등록을 건너뜁니다.\n")
with open("m_leader.txt", "w", encoding="utf-8") as f:
    for i in range(3):
        name = input(f"{i+1}번째 회원의 이름.: ")
        password = input(f"{i+1}번째 회원 비번.: ")
        f.write(f"{name}, {password}\n")

print("\n[회원 명부 저장 완료]")

input_name = input("이름을 입력하세요: ")
input_password = input("비밀번호를 입력하세요: ")

login = False
with open("m_leader.txt", "r", encoding="utf-8") as f:
    for line in f:
        name, password = line.strip().split(",")
        if input_name == name and input_password == password:
            login = True
            break

if login:
    print("\n로그인 성공")
 # 기존 전화번호 데이터 로드
    phone_data = {}
    if os.path.exists("m_t_leader.txt"):
        with open("m_t_leader.txt", "r", encoding="utf-8") as f:
            for line in f:
                name, phone = line.strip().split(",")
                phone_data[name] = phone
  # 전화번호 입력
    new_phone = input(f"{input_name}님의 전화번호를 입력하세요: ")
 # 추가 또는 수정
    if input_name in phone_data:
        print("기존 전화번호 수정")
    else:
        print("전화번호 새로 추가")

    phone_data[input_name] = new_phone

    #전화번호 파일 갱신
    with open("m_t_leader.txt", "w", encoding="utf-8") as f:
        for name, phone in phone_data.items():
            f.write(f"{name}, {phone}\n")
    
    print("전화번호 저장이 완료되었습니다.")
else:
    print("\n로그인 실패")

