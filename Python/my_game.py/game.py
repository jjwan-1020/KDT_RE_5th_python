import time
player_name = input("당신의 이름은 무엇입니까?: ")
health = 100
inventory = []

print(f"{player_name}님 여기는 지하 던전 입니다.\n구조대는 일주일 뒤에 올 것입니다.\n일주일동안 생존하세요.\n")
time.sleep(1)
print("[day1] 일어나보니 남은 식량이 없다.")
food = input("사냥을 하시겠습니까? (yes / no): ")
if food == "yes":
    print("사냥에 성공했습니다. (체력 -10)")
    health -= 10
    inventory.append("생고기")
    print("사냥에 성공하여 고기를 섭취했습니다 (체력 + 20)")
    health += 20
    print(f"현재 체력: {health}")
    if health <= 0:
        print("체력이 바닥났습니다. Game Over")
    else:
        print("")
else:
    health -= 15
    print("사냥을 하지 않아 배고픔이 몰려 옵니다. (체력 -15)")
    print(f"현재 체력{health}")
time.sleep(1)
if health > 0:
    print("[day2] 다음 층으로 올라가는 길을 발견했다 올라가시겠습니까?")
    n_floor = input("다음 층으로 올라갈까? (yes / no): ")
    if n_floor == "yes":
        print("다음 층으로 올라가니 상당한 보석이 있었다 대신 체력이 깎였다 (체력 - 30)")
        health -=30
        inventory.append("사파이어")
        print(f"현재 체력 {health}")
        print(inventory)
    else:
        print("올라가지 않고 구조대를 기대하겠다.")
        health -= 30
        print(f"현재 체력: {health}")
        if health <= 0:
            print("구조대를 기다리다 굶주려 사망했습니다. Game Over")
        else:
            print("")
time.sleep(1)
if health > 0:
    print("[day3] 갈림길이다 어디로 가야 할까?")
    c_road = input("어디로 선택하시겠습니까? (left / right): ")
    if c_road == "right":
        print("몬스터 소굴에 들어왔습니다. 체력이 기하급수적으로 깎입니다. (체력 - 50)")
        health -= 50
        print(f"현재 체력 {health}")
        if health <= 0:
            print("몬스터에 의해 사망했습니다. Game Over")
        else:
            print("")
    elif c_road == "left":
        print("지하에서 어울리지 않는 문을 발견했습니다.")
        s_moon = input("들어가시겠습니까? (yes / no)")
        if s_moon == "yes":
            print("피로를 풀어주는 샘을 발견했습니다. 이게 왜있지..? (체력 + 25)")
            health += 25
            print(f"현재 체력 {health}")
        else:
            print("아무일도 일어나지 않았다 (체력 변화 없음)")
            print(f"현재 체력 {health}")
        if health <= 0:
            print("체력이 다하여 사망했습니다. Game Over")
        else:
            print("")
time.sleep(1)
if health > 0:
    print("[day4] 있으면 안될 물건이 있다.")
    p_thing = input("열어보시겠습니까? (yes / no)")
    if p_thing == "yes":
        print("상자 몬스터 미믹이었다! (체력 - 60)")
        health -= 60
        print(f"현재 체력 {health}")
        if health <= 0:
            print("미믹에 잡아먹혔습니다. Game Over")
        else:
            print("")
    elif p_thing == "no":
        print("꺼림직해서 안열었더니 체력포션이 떨어졌다 (체력 + 20)")
        health += 20
        print(f"현재 체력 {health}")
time.sleep(1)
import random as r
if health > 0:
    print("[day5] 던전안에서 판도라의 상자를 발견했다. 뭔가 위험해보인다..")
    open = input("열어보시겠습니까? (yes / no): ")
    if open == "yes":
        print("체력이 점점 빨려 가는걸 느꼈다..힘이 빠진다..(체력이 랜덤하게 내려갑니다)")
        health -= r.randint(1, 50)
        print(f"현재 체력 {health}")
        if health <= 0:
            print("호기심에 의해 돌아올 수 없는 강을 건넜습니다. Game Over")
    else:
        print("위험하니 열지 말자..(체력 변동이 없습니다)")
        print(f"현재 체력 {health}")
time.sleep(1)
if health > 0:
    print("[day6] 앞에 언데드 몬스터가 있습니다.")
    attack = input("공격하시겠습니까 (yes / no) ")
    if attack == "yes":
        health -= r.randint(1, 10)
        print(f"현채 체력 {health}")
        if health > 0:
            print("체력이 떨어졌지만 금이빨을 손에 넣었다. 왜 있지..?")
        elif health <= 0:
            print("언데드 몬스터에 의해 당신도 언데드가 되었습니다. Game Over")
    else:
        print("36계 줄행량을 쳤습니다 (체력 - 20)")
        if health <= 0:
            print("도망 치다 기력을 다하여 사망했습니다. Game Over")
            print("")
        elif health >= 0:
            print(f"현재 체력 {health}")
time.sleep(1)
if health > 0:
    print("[day7] 오늘만 버티면 된다..그럼 구조대가 올것이다..")
    stay = input("더 나아가시겠습니까? (yes / no)")
    if stay == "yes":
        print("앞으로 더 나아가니 레이스를 마주쳤다 어떡하지?")
        at2 = input("공격하시겠습니까? 처치하면 보상이 있지만 대신 처치를 못하면 사망합니다.\n (yes / no)")
        if at2 == "yes":
            words = ["win", "lose"]
            pick = r.choice(words)
            print(pick)
            if pick == "win":
                print("축하합니다 용기를 얻었습니다 (체력 - 10)")
                health -= 10
                print(f"현재 체력 {health}")
            else:
                print("처치 실패 했습니다..")
                health -= 100
                print("레이스 처치 실패로 영혼이 흡수 되었습니다. Game Over")
    else:
        print("오늘만 버티면 된다 아무것도 하지말자 (체력 변동 없음)")
time.sleep(1)
if health > 0:
    print("구조대가 도착했습니다. 축하합니다! 당신은 생존하셨습니다")
    inventory.pop(all)
    print(f"현재 인벤토리 {inventory}")
else:
    print("구조대가 오기 전 간발이 차로 언데드가 되었습니다. Game Over")


