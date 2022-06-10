i = 1
while i <= 9:
    j = 1 #如果单独在外面则则不会循环递增
    while j <= i:
        print('%d*%d=%d'%(i,j,i*j),end=' ') #print(, ,end='')最后一位默认为换行符，end=‘ ’替换为\t
        j += 1
    print()
    i += 1

