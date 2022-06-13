list=[1,2,3,4,5]
print(all(list))
list1=[0,1,2,3,4,5]
# 0返回false
print(all(list1))
trul=(1,2,3,4,5,'')
# 空字符串返回false
print(all(trul))
list2=(False,1,2,3,4)
print(all(list2))
list3=[]
print(all(list3))
def all(*args, **kwargs):  # real signature unknown
    """
    Return True if bool(x) is True for all values x in the iterable.

    If the iterable is empty, return True.
    """
    pass
# all()判断是否存在false、0、空，如果存在则返回false,空列表、元组一样返回true

A=[0,1,2,3,4,5]
print(any(A))

def any(*args, **kwargs):  # real signature unknown
    """
    Return True if bool(x) is True for any x in the iterable.

    If the iterable is empty, return False.
    """
    pass
# any() 函数用于判断的给定的可迭代参数iterable是否全部为False，则返回False，如果有一个为true，则返回True
c=[1,4,6,2,4,7,1,22]
print(sorted(c))
b=('b','a','D','c')
print(sorted(b))
d=(2,4,1,12,4,5,3)
print(sorted(d,reverse=True))
#返回的是一个新列表,reverse=true降序操作
def sorted(*args, **kwargs):  # real signature unknown
    """
    Return a new list containing all items from the iterable in ascending order.

    A custom key function can be supplied to customize the sort order, and the
    reverse flag can be set to request the result in descending order.
    """
    pass
# sort与sorted的区别：sort是存在与列表的内部方法，sorted可以对所有可迭代参数操作
F=[1,2,3,4,5,6]
F.reverse()
print(F)
def reverse(self, *args, **kwargs): # real signature unknown
        """ Reverse *IN PLACE*. """
        pass
# 列表的降序方法

range()