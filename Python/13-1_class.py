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