list1=[1,2,3,4,5]
set1=set(list1)
# 强制转换列表为set集合
print(set1)
# print(type(set1))
# 无序，不重复
print('----------------add()---------------------')
set1.add(5)
# 增加一个元素,如果已存在,则不增加
print('增加一个元素,如果已存在,则不增加{}'.format(set1))
print('-----------------clear()---------------------')
set1.clear()
# 清除set集合中所有数据
print('清除set集合中所有数据{}'.format(set1))
print('--------------difference()------------------------')
a={1,2,3,4,5}
b={2,3,4,5,6}
c=a.difference(b)
print('找a集合中b集合不存在的数据{}'.format(c))
print('------------------intersection()--------------------')
c={1,2,3,4,5,6,7}
d={7,8,9,10}
f=c.intersection(d)
print('找c集合于d集合相同元素{}'.format(f))
print('--------------------union()------------------')
g={1,2,3,4,5}
h={5,7,8,9,10}
j=g.union(h)
print('集合的元素整合成一个新集合{}'.format(j))
print('-----------------pop()---------------------')
print(j.pop())
print('随机拿走一个元素并删除{}'.format(j))
print('------------------discard()--------------------')
g.discard(6)
print('取走集合中的一个元素如果存在于集合中{}'.format(g))
print('-----------------update()---------------------')
g.update(h)
print('使用自身和其他集合的并集更新集合{}'.format(g))
print('--------------------------------------')










