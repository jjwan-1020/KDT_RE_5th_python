def solution(a,b):
    concat = int(str(a) + str(b))
    mult = 2 * a *b
    if concat >= mult:
        return concat
    else:
        return mult

a, b = 12, 3

print(solution(12,3))

a = 4
b = 5
print(f'''a = {a}
b = {b}''')

s = "string"
print(s * 5)