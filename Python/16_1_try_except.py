# 실습 2 (Leader)
answer = input("숫자 입력: ")

try:
    num = int(answer)
except:
    num = -1

if num > 0:
    print("0보다 큽니다")
else:
    print("숫자가 아닙니다.")

# 실습 2 (Leader)
def print_result(n1,op,n2,result):
   print(f"{n1} {op} {n2} = {result}")
   
while True:
    try:
        num1 = float(input(" 첫 수를 입력하세요: "))
        op = input("연산자(+,-,*,/)중 하나: ")
        num2 = float(input("두 번째 수: "))
        
        if op not in ['+','-','*','/']:
            raise ValueError("잘못된 연산자이다")
        if op == '/' and num2 == 0:
            raise ZeroDivisionError("0으로 나눌 수 없습니다.")
    
        if op == '+':
         result = num1 + num2
        elif op == '-':
         result = num1 - num2
        elif op == '*':
         result = num1 * num2
        else:
         result = num1 / num2

        print_result(num1, op, num2, result)
        break
    except ValueError:
       print("입력이 잘못되었습니다. 다시 입력해주세요.\n")
    except ZeroDivisionError as e:
       print(e)
       print("0으로 나눌 수 없습니다. 다시 입력해주세요.\n")
    except Exception:
       print("알 수 없는 오류가 발생했습니다.\n")

