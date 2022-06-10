height=float(input('请输入你的身高(M)：'))
weight=float(input('请输入你的体重(KG)：'))
BMI=weight/(height**2)
if BMI<18.5:
    print("过轻")
elif BMI>=18.5 and BMI<25:
    print('正常')
elif BMI>=25 and BMI<28:
    print('过重')
elif BMI>=28 and BMI<32:
    print("肥胖")
else:
    print('严重肥胖')
print("你的BMI为%f"%BMI)
