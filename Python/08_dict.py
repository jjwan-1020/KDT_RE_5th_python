'''
딕셔너리 (dictionary)
- 키-값 쌍으로 묶어 데이터를 저장하는 자료형
- 키는 유일해야 함. 값은 중복 가능
-변경 가능한 자료형
- 순서가 보장되지 않았다가 py 3.7버전 이후 순서가 보장됨
'''

# dict 만들기



d1 = {} # 빈 dict 만들기
print(type(d1)) # <class 'dict'>

person = {"name": "홍길동", "age": 25}
print(person)

# dict 함수로 생성
d2 = dict()
print(d2, type(d2)) # {} <class 'dict'>

# 카가 문자열일 때 가능
movie = dict(title="int", director="nolan")
print(movie) # {'title': 'int', 'director': 'nolan'}
print(movie, movie["director"]) # {'title': 'int', 'director': 'nolan'} nolan

# 리스트나 튜플로 만들기
pairs = [("name", "정재완"), ("age", 26), ("city", "pohang")]
person2 = dict(pairs)
print(person2) # {'name': '정재완', 'age': 26, 'city': 'pohang'}

# zip 함수 활용
keys = ["title", "director", "year"]
valus = ["기생충", "붕준호", "2019"]
movie2 = dict(zip(keys, valus))
print(movie2) # {'title': '기생충', 'director': '붕준호', 'year': '2019'}

# 키로 사용할 수 없는 자료형
# 키 - 불변 자료형만 사용해야한다
d1 = {(1,2,3): (1,2,3)} # 튜플 사용 가능
d2 = { 1 :10 } # 숫자 사용 가능
# d3 = {[1,2,3]:"리스트 값을 키로?"} # TypeError: cannot use 'list' as a dict key (unhashable type: 'list')
# print(d3) # TypeError: cannot use 'list' as a dict key (unhashable type: 'list')

# dict 데이터 조회
print(person2["name"])
print(person2["age"])
# print(person2["email"]) # KeyError: 'email'

# get 메서드를 활용한 조회
print(person2.get("name"))
print(person2.get("email"))
# print(person2.get("email", "이메일이 존재하지 않습니다")) # 이메일이 존재하지 않습니다

# get 사용 예제
user_data = {
     "username": "정재완",
     "email": "jjwan1020@gmail.com",
     "password": "1597"
 }
#key = input("조회할 정보를 입력하세요(username, email, password): ")
# result = user_data.get(key, "존재하지 않는 데이터입니다.")
#print(result)

# 데이터 추가 및 수정
# 1) 기몬적인 추가, 수정 방법
user_data["phone"] = "010-1234-5678" 
user_data["username2"] = "jjwan"


# update 메서드 활용
user_data.update({"nickname" : "jjwan1020"})
print(user_data)

# 키가 문자열인 경우
user_data.update(phone="010-2257-6788")

# 다른 딕셔너리 추가
extra_data = {"city": "seoul"}
user_data.update(extra_data)
print(user_data)

# 데이터 삭제
del user_data["city"]
print(user_data)

# 키로 제거
nickname = user_data.pop("nickname")
print("pop >>", user_data, nickname, sep=" /// ")


# 가장 마지막 요소 제거
user_data.popitem()
# print(user_data, , sep=" /// " )

# dict 비우기
user_data.clear()
print(user_data)

# dict 삭제하기
# del user_data
# print(user_data)

# 메서드
user_data = {"username": "정재완",
     "email": "jjwan1020@gmail.com",
     "password": "1597"
}

# keys: 모든 키를 반환
print("키", user_data.keys()) # 키 dict_keys(['username', 'email', 'password'])
print("키", list(user_data.keys())) # 키 ['username', 'email', 'password']

# values: 모든 값을 반환
print("값", list(user_data.values())) # 값 ['정재완', 'jjwan1020@gmail.com', '1597']

# items: 모든 키값쌍을 반환
print("쌍", list(user_data.items())) # 쌍 [('username', '정재완'), ('email', 'jjwan1020@gmail.com'), ('password', '1597')]









# 실습
user = {
    "username": "skywalker",
    "email": "sky@example.com",
    "level": 5
}
#print(user)
email_value = user["email"]
#print(email_value) 
user.update({"level": 6})
#print(user) 
#print(user.get("phone", "미입력"))
user.update({"nickname" : "sky"}) 
#print(user)
del user["email"]
#print(user)
signup_date = user.setdefault("singup_date", "2025-07-10")
#print(signup_date) 



students = dict()
students = {"Alice": 85, "Bob": 90, "Charlie": 95}
#print(students)
students.update({"David": 80})
#print(students)
students.pop("Bob")
#print(students)