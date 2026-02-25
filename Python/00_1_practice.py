class UserAccount:
    def __init__(self, username, password):
        self.username = username
        self.__password = password   

    def change_password(self, old_pw, new_pw):
        if self.__password == old_pw:
            self.__password = new_pw
            print("비밀번호가 변경되었습니다.")
        else:
            print("비밀번호 불일치")

    def check_password(self, password):
        return self.__password == password

user1 = UserAccount("홍길동", "1234")

print(user1.check_password("1234"))   
print(user1.check_password("0000"))   

user1.change_password("1234", "abcd") 
user1.change_password("0000", "xxxx") 
