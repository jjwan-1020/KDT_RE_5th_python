# 클래스(class)
# - 데이터와 기능을 하나로 묶는 구조
# - 개념적(기능적)으로 유사한 관계에 있는 것들을 묶어줌

# 클래스 기본 문법
# 클래스의 정의
class ClassName:
    #생성자 (constructor): 인스턴스(객체)가 생성될 때 호출
    # 인스턴스 변수를 초기화, 기본 상태 설정
    # 하나의 클래스에서 하나만 정의 가능
    def __init__(self, name):
        # 인스턴스 변수
        # self: 인스턴스 자기 자신을 가리킴
        self.name = name
        self.age = 0

    # (인스턴스) 메서드
    
    def method_name(self):
        print(f"이 인스턴스의 이름은 {self.name}입니다")

# 인스턴스 생성
my_instance = ClassName("K5")
print(my_instance.name)
my_instance.method_name()

another_instance = ClassName("K2")
another_instance.method_name()


# 실습
class Book:
    def __init__(self, title, author,total_pages, current_page):
        self.title = title
        self.total_pages = total_pages
        self.author = author
        self.current_page = current_page
    
    def read_page(self, pages):
        self.current_page += pages
        if self.current_page > self.total_pages:
            self.current_page = self.total_pages
        print(f"{pages}페이지 읽었고 현재 페이지는 {self.current_page}입니다")
    def progress(self):
        percent = (self.current_page / self.total_pages) * 100
        print(f"읽은 비율은 {percent:.1f}%입니다")
    def print_info(self):
        print(f"제목은 {self.title}입니다.")
        print(f"저자는 {self.author}입니다")
        print(f"전체 페이지는 {self.total_pages}입니다")
        print(f"현재 페이지는 {self.current_page}입니다")

book1 = Book("노인과 바다", "어니스트 헤밍웨이", 193, 75)
book1.print_info()
book1.read_page(50)
book1.progress()
        

# 실습 2
'''
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
 
w = int(input("가로값을 입력해주세요.: "))
h = int(input("세로값을 입력받아주세요.: "))
r_area = Rectangle(w, h)
print(f"사각형의 넓이는 {r_area.area()}입니다.")
'''

# 클래스 변수
# - 클래스가 가지고 있는 변수
# - 모든 인스턴스가 공유할 수 있음
class Dog:
    # 클래스 변수
    kind = "강아지"

    def __init__(self, species, name, age):
        self.species = species
        self.name = name
        self.age = age

dog1 = Dog("포메라니안", "리치", 12)
dog2 = Dog("비숑", "구름", 10)

print("인1", dog1.kind)
print("인2", dog2.kind)
print("클래스", Dog.kind)

# 클래스 메서드
# 클래스 자체를 대상으로 동작하는 메서드
# 클래스 데이터를 조작하는데 사용

class Book2:
    book_count = 0

    def __init__(self, title, author):
        Book2.book_count += 1
        self.title = title
        self.title = author

    # 클래스 메서드
    @classmethod # 데코레이터
    def get_count(cls):
        print(f"현재 {cls.book_count}권의 책을 가지고 있습니다.")

book1 = Book2("B1", "author1")
book2 = Book2("B2", "author2")
print(Book2.book_count)
Book2.get_count()

# 정적 메서드
# - 클래스나 인스턴스의 데이터를 조작하지 않는 클래스 함수
# - 클래스나 인스턴스의 상태에 의존하지 않는 일반 함수
# - 개념적으로는 클래스와 연관이 있으나, 클래스나 인스턴스의 데이터를 조작하지 않음

class OperationTool:

    @staticmethod # 데코레이터
    def add(a, b):
        return a + b

print(OperationTool.add(10,20))

# 실습 3

class User:
    total_users = 0

    def __init__(self, username):
        self.username = username
        self.points = 0
        User.total_users += 1

    def add_points(self, amount):
        self.points += amount

    def get_level(self):
        if 0 <= self.points <= 99:
            return "Bronze"
        elif 100 <= self.points <= 499:
            return "Silver"
        else:
            return "Gold"
    @classmethod
    def get_total_users(cls):
        print(f"총 유저수: {cls.total_users}명 입니다")


u1 = User("Ailce")
u2 = User("Bob")
u3 = User("Chaile")
u1.add_points(50)
u2.add_points(190)
u3.add_points(501)
User.get_total_users()
print(u1.username, u1.points, u1.get_level())
print(u2.username, u2.points, u2.get_level())
print(u3.username, u3.points, u3.get_level())



# 접근 제어와 정보 은닉
# 데이터 무결성을 보호하기 위함
# 코드 안정성을 향상 시키기 위함

class Person2:
    def __init__(self, name, age):
        # public
        self.name = name
        # private: 언더바 (__) 두개를 변수 앞에 붙여서 정의
        self.__age = age
    
    # getter
    def get_age(self):
        return self.__age
    
    # setter
    def set_age(self, value):
        if value > 120 or value < 0:
            print("유효하지 않은 나이입니다")
        else:
            self.__age = value



p1 = Person2("lee", 15)
print(p1.name)
# print(p1.__age) X
print(p1.get_age())
p1.set_age(10)


# @property 데코레이터
# - 메서드를 속성처럼 보이게 만들어주는 데코레이터

class Ex:
    def __init__(self):
        self.__value = 0

    # getter
    @property
    def value(self):
        return self.__value
    
    # setter
    @value.setter
    def value(self, val):
        if val < 0:
            print("유효하지 않은 값입니다.")
        else:
            self.__value = val

ex1 = Ex()
print(ex1.value)
ex1.value = 100
print(ex1.value)



# 실습 3

class UserAccount:
    def __init__(self, username, password):
        self.username = username
        self.__password = password

    def change_password(self, old_pw, new_pw):
        if self.__password == old_pw:
            self.__password = new_pw
            print("비밀번호가 변경되었습니다.")
        else:
            print("비밀번호가 일치하지 않습니다.")

    def check_password(self, password):
        return self.__password == password

user = UserAccount("jjwan", "jj0852")
print(user.check_password("jj0852"))
print(user.check_password("just"))

user.change_password("jj0852", "just")
user.change_password("jjjust", "stardust")

class Student:
    def __init__(self, score):
        self.score = score
    
    @property
    def score(self):
        return self.__score
    
    @score.setter
    def score(self, value):
        if 0 <= value <= 100:
            self.__score = value
        else:
            raise ValueError
        
s = Student(85)
print(f"이 학생의 점수는 {s.score}점 입니다") 



