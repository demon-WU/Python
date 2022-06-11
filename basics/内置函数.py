a = -3
print(abs(a))
# 取绝对值abs()

b=1.3434341
print('取近似值{}'.format(round(b,2)))
# 取近似值，四舍五入round()

print('幂函数{}'.format(pow(2,3,)))
# 求幂函数x的y次方pow()

print('返回商和余数的一个元组{}'.format(divmod(3,3)))
# 求商和余数（商，余数）divmod()

print('求最大值：{}'.format(max(-100,0,100)))
# 求最大值max()

print("求最小值{}".format(min(-100,0,100)))
# 求最小值函数min()

print('求和{}'.format(sum([1,2,3,4],2)))
# 求和函数sum(a,b),a为需要加的数或元组、列表，b为结束后继续加上b

def test():
    print('在执行内置函数')
eval('test()')
print(eval('a+b'))
# eval()执行字符串表达式，格式为eval('')
# 赋值必须为字典对象：eval("a+b+c",{a:1,b:2,c:3})