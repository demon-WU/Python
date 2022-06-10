grade=[]
num = int(input("请输入学生人数："))
while num > 0:
        name = input("请输入姓名：")
        score = int(input("请输入学生成绩："))
        if score <0 or score>100:
                print("输入非法分数，请注意")
                pass
        else:
                if score>=0 and score<60:
                        b=score * 0
                else:
                        b = score/10-5
        c=name+':'+str(round(b,3))
        grade.append(c)
        num-=1
print(grade[::-1])