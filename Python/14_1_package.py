# 실습 (Leader)
'''
import math as m

x1, y1 = map(int, input("x1, y1을 입력해주세요.: ").split(","))
x2, y2 = map(int, input("x2, y2을 입력해주세요,: ").split(","))
dist = round(m.sqrt(m.pow((x2-x1), 2) + m.pow((y2-y1),2), 2))
print(f"두 점 사이의 거리: {dist}")
a = 18
b = 24
gcd = m.gcd(a, b)
lcm = m.lcm(a, b)
print(f"최대 간식 수: {gcd}")
print(f"최소 간식 개수: {lcm}")
'''

# 실습 4 랜덤 모듈 (Leader)
import random
result = sorted(random.sample(range(1, 46), k=6))
print(result)

# 4-2 
lotto = []
while len(lotto) < 6:
    number = random.randint(1,45)
    if number in lotto:
        continue
    
    lotto.append(number)

lotto.sort()
print(lotto)

# 실습 5 (Leader)
'''
rsp = ["가위", "바위", "보"]
win_count = 0

while win_count < 3:
    com_choice = random.choice(rsp)
    user_choice = input("가위, 바위, 보 중에 선택하시오.: ")
    print(f"사용자의 선택: {user_choice}")
    print(f"컴퓨터의 선택: {com_choice}")

    if user_choice == com_choice:
        print("무승부")
    elif (user_choice == '가위' and com_choice == '보') or \
     (user_choice == '바위' and com_choice == '가위') or \
     (user_choice == '보' and com_choice == '바위'):
        print("승리")
        win_count += 1
    elif user_choice in rsp:
        print("패배")
    else:
        print("입력을 잘못했습니다. 다시 입력해주세요.")
'''        
# 실습 6 (Leader) 
import time
import random
word = ["apple", "banana", "orange", "grape", "lemon", "peach", "melon", "cherry",
        "plum", "pear", "school","friend","family","flower","garden","window","bottle",
        "pencil","summer","winter","happy","future","travel","animal","market","doctor",
        "planet","energy","nature","memory"]

n = 1
input("[타자 게임] 준비되면 엔터키를 눌러주세요")
start = time.time()

while n < 11:
    print(f"{n}번 문제")
    question = random.choice(word)
    print(question)
    user_answer = input()

    while True:
        if question == user_answer:
            print("통과")
            n += 1
            break
        else:
            print("오타입니다.")

end = time.time()
play_time = end - start
print(f"총 소요시간: {play_time: .2f}초")
