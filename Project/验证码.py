import random

sj = ''
for i in range(2):
    zimu = chr(random.randint(65, 90)) + chr(random.randint(97, 122))
    sj = sj + zimu
print(sj)
user_input = input()
# 把验证码和用户输入的字符全部变成小写或大写，然后对比
if user_input.upper() == sj.upper():
    print("验证码正确")
else:
    print("验证码错误，请重新输入")