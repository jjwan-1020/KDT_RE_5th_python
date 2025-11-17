sumb = ['kim', 'lee', 'kim', 'park', ]





user_1 = {'SF', 'Action', 'Drama'}
user_2 = {'Drama', 'Romance', 'SF'}
print("공통 괸심 장르: ", user_1 & user_2)
print("다른 관심 장르: ", user_1 ^ user_2)
print("전체 장르: ", user_1 | user_2)




my_certificates = {'SQL', 'Python', 'Linux'}
job_required = {'SQL', 'Python'}
print(my_certificates.issuperset(job_required))

user = {
    "user_name": "walker",
    "email": "walker.example@gmail.com",
    "level": 6
}
user.update({"level": 8})
user.update({"nickname": "jin"})
print(user)
signup_date = user.setdefault("sigup_date", "2025-07-08")
print(signup_date)