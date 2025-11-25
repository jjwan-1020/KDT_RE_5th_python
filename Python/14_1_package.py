# 실습 (Leader)
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