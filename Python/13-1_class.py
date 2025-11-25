# 실습 (Leader)
class Book:
    def __init__(self, title, author, total_pages, current_page):
        self.title = title
        self.author = author
        self.total_pages = total_pages
        self.current_page = current_page

    def read_page(self, pages):
        self.current_page += pages

        if self.current_page > self.total_pages:
            self.current_page = self.total_pages
            print("책을 끝까지 다 읽었어요.")

    def progress(self):
        percent = (self.current_page / self.total_pages) * 100
        print(f"현재 읽은 분량: {percent: .1f}%")

book1 = Book("넥서스", "유발 하라리", 500, 1)
book1.read_page(50)
book1.progress()

book1.read_page(500)
book1.progress()
        

# 실습 2 (Leader)
'''
class Rectangle:
    def __init__(self, width, heigh):
        self.width = width
        self.heigh = heigh
    
    def area(self):
        return self.width * self.heigh
    
w = int(input("가로 길이를 입력하세요.: "))
h = int(input("세로 길이를 입력해주세요.: "))

my_rect = Rectangle(w, h)

print(f"사각형의 넓이는 {my_rect.area()}입니다.")
'''
# 실습 3 (Leader)
class User:
    total_users = 0

    def __init__(self, username):
        User.total_users +=1
        self.total_username = username
        self.points = 0

    def add_points(self, amount):
        self.points += amount

    def get_level(self):
        if self.points >= 500:
            return "Gold"
        elif self.points >= 100:
            return "Silver"
        else:
            return "Bronze"
    
    @classmethod
    def get_total_users(cls):
        print(f"총 유저 수: {cls.total_users}")

# 실습 3 (Leader)
# 문제 1, UserAccount 클래스
class UserAccount:
    def __init__(self, username, password):
        self.username = username
        self.__password = password

    def change_password(self, old_pw, new_pw):
        if old_pw == self.__password:
            self.__password = new_pw
            print("비밀번호가 변경되었습니다.")
        else:
            print("기존 비밀번호가 일치하지 않습니다.")

    def check_password(self, password):
        return self.__password == password
    
user = UserAccount("user1", "pass123")
print(user.username)
print(user.check_password("pass123")) # True
user.change_password("wrongpass", "newpass") # False

# 실습 3 성적검증
class Student:
    def __init__(self, name, score):
        self.name = name
        self.__score = score

    @property # getter
    def score(self):
        return self.__score
    
    @score.setter
    def score(self, value):
        if 0 <= value <= 100:
            self.__score = value
        else:
            raise ValueError("성적은 0에서 100사이여야 합니다")

s1 = Student("Alice", 85)
print(s1.name)
print(s1.score)

# 실습 4
class Shape:
    def __init__(self, sides, base):
        self.sides = sides
        self.base = base
    
    def printinfo(self):
        print(f"변의 개수: {self.sides}")
        print(f"밑변의 길이: {self.base}")

    def area(self):
        print("넓이 계산이 정의되지 않았습니다")

class Rectangle(Shape):
    def __init__(self, sides, base, height):
        super().__init__(sides, base)
        self.height = height

    def area(self):
        area = self.base * self.height
        print(f"{self.sides}각형의 넓이: {area}")

class Triangle(Shape):
    def __init__(self, sides, base, height):
        super().__init__(sides, base)
        self.hegiht = height
    
    def area(self):
        area = int((self.base * self.hegiht) / 2)
        print(f"{self.sides}각형의 넓이: {area}")

r = Rectangle(4, 9, 10)
r.printinfo()
r.area()
t = Triangle(5, 6, 7)
t.printinfo()
t.area()

# 실습 5 (Leader)

from abc import ABC, abstractmethod
class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class CardPayment(Payment):
    def __init__(self):
        super().__init__()
    
    def pay(self, amount):
        print(f"카드로 {amount}원을 결제합니다.")

class CashPayment(Payment):
    def pay(self, amount):
        print(f"현금으로 {amount}원을 결제합니다.")

card = CardPayment()
card.pay(50000)
cash = CashPayment()
cash.pay(150000)
        