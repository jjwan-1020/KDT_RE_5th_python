class Shape:
    def __init__(self, sides, base):
        self.sides = sides
        self.base = base
    
    def printinfo(self):
        print(f"변의 개수: {self.sides}")
        print(f"밑변의 길이: {self.base}")

    def area(self):
        print("넓이 계산이 정의되지 않았습니다.")

class Rectangle(Shape):
    def __init__(self, sides, base, height):
        self.sides = sides
        self.base = base
        self.height = height
    
    def area(self):
        print(self.base * self.height)

class Triangle(Shape):
    def __init__(self, sides, base, height):
        self.sides = sides
        self.base = base
        self.height = height

    def area(self):
        print((self.base * self.height) / 2)

s = Shape(4, 6)
s.printinfo()
s.area()

r = Rectangle(5, 7, 3)
r.printinfo()
r.area()

t = Triangle(7, 6, 5)
t.printinfo()
t.area()


class Book:
    def __init__(self, title, author, total_pages, current_pages):
        self.title = title
        self.author = author
        self.total_pages = total_pages
        self.current_pages = current_pages
    
    def read_page(self, pages):
        self.current_pages += pages
        if self.current_pages > self.total_pages:
            self.current_pages = self.total_pages
            print(f"{pages} 읽었고 현재 페이지는 {self.current_pages}입니다.")
    def progress(self):
        percents = (self.current_pages / self.total_pages) * 100
        print(f"읽은 페이지 비율은 {percents:.1f}% 입니다.")
    def printinfo(self):
        print(f"제목은 {self.title}입니다.")
        print(f"저나는 {self.author}입니다.")
        print(f"전체 페이지는 {self.total_pages}입니다.")
        print(f"현재 페이지는 {self.current_pages}입니다.")

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self. width * self.height

w = int(input("가로 입력: "))
h = int(input("세로 입력: "))
r_area = Rectangle(w, h)
print(f"사각형의 넓이는 {r_area.area()}입니다")



class User:
    total_user = 0

    def __init__(self, username):
        self.username = username
        self.points = 0
        User.total_users += 1

    def add_points(self, amount):
        self.points += amount
    def get_level(self):
        if 0 <= self.points <= 99:
            return "Bronze"
        elif 100<= self.points <= 499:
            return "Silver"
        else:
            return "Gold"
        
    @classmethod
    def get_total_users(cls):
        print(f"총 유저수: {cls.total_users}명 입니다.")


class Person2:
    def __init__(self, name, age):
        self.name = name
        self.__age = age
        
    def get_age(self):
        return self.__age
    def set_age(self, value):
        if value > 120 or value < 0:
            print("유효하지 않은 나이입니다.")
        else:
            self.__age = value

p1 = Person2("Jeong", 26)
print(p1.name)
print(p1.get_age())
p1.set_age(10)

class UserAccount:
    def __init__(self, username, password):
        self.username = username
        self.__password = password
    def change_password(self, old_pw, new_pw):
        if self.__password == old_pw:
            self.__password


