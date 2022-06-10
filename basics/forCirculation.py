#continue 的使用
sum=0
# for i in range(1,101):
#     if i%2==1:
#         continue
#     else:
#         print("i的值为%d"%i)
#         sum+=i
#         print(sum,end=' ')

# for i in range(1,11):
#     print(i)
# else:
#     print('执行完毕')

for i in range(1,10):
    for j in range(1,i+1):
        print("%d*%d=%d"%(i,j,i*j),end=' ')
    print()