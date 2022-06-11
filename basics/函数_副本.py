def function(n):
    if n==1:
        return 1
    else:
        return n*function(n-1)

n=5
print('阶乘{}'.format(function(3)))