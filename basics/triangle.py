# i = 1
# while i < 10:
#     j = 1
#     while j <= i:
#         print('*',end='')
#         j += 1
#     i += 1
#     print()
#
#
# p=10
# while p > 0:
#     k = 1
#     while k <= p:
#         print(' *',end='')
#         k += 1
#     p -= 1
#     print()
d= int(input('输入等腰三角形的长度：'))
row = 1
while row <=d:
    j = 1
    while j<= d-row: #控制前面空格的数量
        print(' ',end='')
        j+=1
    k = 1
    while k<=2*row-1: #控制*的数量
        print('*',end='')
        k+=1
    print()
    row+=1
