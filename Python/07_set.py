'''
set (집합)
- 원소의 중복을 허용하지 않는 여러 데이터의 모음
- 순서가 없는 컬렉션 자료형
'''

# set 만들기
s1 = {1,2,3}
print(s1, type(s1)) # {1, 2, 3} <class 'set'>

s2 = {1,1,1,2,2,2,3,3,3,4,4,4}
print(s2) # {1, 2, 3, 4}

# 빈 set 만들기
# - 중괄호에 원소를 넣지 않고 만들면 빈 dict로 인식됨
s3 = {}
print(type(s3)) # <class 'dict'>

# set 함수로 생성
s4 = set()
print(type(s4)) # <class 'set'>

# set 함수의 활용 : 원소의 중복 제거
my_list = [1,1,2,2,2,3,3,3,4,4,4]
s5= set(my_list)
print(s5) # {1, 2, 3, 4}로 나옴

# 인덱싱 X
# s1[1] # TypeError: 'set' object is not subscriptable가 일어남

# 자료형 제한
# - 가변 자료형은 원소로 사용할 수 없다
# s1 = {1,2,3, [1,2,3]} # TypeError: cannot use 'list' as a set element (unhashable type: 'list')가 뜬다

# set 연산
# 집합의 연산 : 합집합, 교집합, 차집합, 대칭차집합
a = {1,2,3}
b = {3,4,5}

# 합집합 (|, .union)
s_union1 = a | b
s_union2 = a.union(b)
print("합집합1", s_union1)
print("합집합2", s_union2)

# 교집합 (&, .intersection)
s_inter1 = a & b
s_inter2 = a.intersection(b)
print("교집합1", s_inter1)
print("교집합2", s_inter2)

# 차집합 ( -, .difference)
s_diff1 = a - b
s_diff2 = a.difference(b)
print("차집합1", s_diff1)
print("차집합2", s_diff2)

# 대칭 차집합 ( ^, .symmetric_difference)
s_symm1 = a ^ b
s_symm2 = a.symmetric_difference(b)
print("대칭 차집합1", s_symm1)
print("대칭 차집합2", s_symm2)

# set 메서드
s1 = {1,2,3}

# 원소 추가
s1.add(4)
print("원소 추가", s1)

# 여러 원소 추가
s1.update((5,6,7))
print("여러 원소 추사", s1)

# 원소 제거
s1.remove(4)
print("원소 제거1", s1)
# s1.remove(100) # KeyError: 100 - 존재하지 않는 원소 삭제 시 에러

s1.discard(100)
s1.discard(6)
print("원소 제거2", s1)

deleted = s1.pop() # 임의의 값 하나 제거
print("원소 제거3", s1, deleted)

# 부분 집합 (subset) 관련 메서드
a = {10,20,30,40,50} # 상위집합
b = {20,30,50} # 부분집합
c = {10,200,300,400,500}

#부분집합 여부 판단
print(b.issubset(a)) #True
print(a.issubset(b)) #False

#상위집합 여부 판단
print(a.issuperset(b)) # True
print(b.issuperset(a)) # False

#공통 원소가 없는지 확인
print(a.isdisjoint(b)) # False
print(a.isdisjoint(c)) # False
print(b.isdisjoint(c)) # True


# 실습
submissions = {"kim","lee","kim","park","choi","lee","park"}
stu1 = len(set(submissions))
print("제출한 학생 수: " , (stu1))
print("제출자 명단: ", (submissions))

user1 = {'SF', 'Action', 'Drama'}
user2 = {'Drama', 'Romance', 'Action'}
same1 = user1 & user2
diffe2 = user1 ^ user2
all3 = user1 | user2
print("공통 관심 장르: ", (same1))
print("서로 다른 장르: ", (diffe2))
print("전체 장르: ", (all3))

my_certificates = {'SQL','Python','Linux'}
job_required = {'SQL', 'Python'}
print("지원 자격 충족 여부: ", job_required.issubset(my_certificates))

