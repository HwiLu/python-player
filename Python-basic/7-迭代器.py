from  collections import Iterable
from  collections import Iterator
'''
可迭代对象：可以直接作用于for循环的对象统称为可迭代对象(Iterable)。可以用isinstance()去判断一个对象是否是Iterable对象

可以直接作用于for的数据类型一般分两种
1、集合数据类型，如list、tuple、dict、set、string
2、是generator，包括生成器和带yield的generator function
'''
print(isinstance([], Iterable))
print(isinstance((), Iterable))
print(isinstance({}, Iterable))
print(isinstance("", Iterable))
print(isinstance((x for x in range(10)), Iterable))
print(isinstance(1, Iterable))

'''
迭代器：不但可以作用于for循环，还可以被next()函数不断调用并返回下一个值，直到最后跑出一个StopIteration错误表示无法继续返回下一个值
可以被next()函数调用并不断返回下一个值的对象称为迭代器(Iterator对象)
可以使用isinstance()函数判断一个对象是否是Iterator对象
'''
print(isinstance([], Iterator))
print(isinstance((), Iterator))
print(isinstance({}, Iterator))
print(isinstance("", Iterator))
print(isinstance((x for x in range(10)), Iterator))

l = (x for x in [23,4,5,64,3435])
print(next(l))
print(next(l))
print(next(l))
print(next(l))
print(next(l))
#print(next(l))

#转成Iterator对象
a = iter([1,2,3,4,5])
print(next(a))
print(next(a))

print(isinstance(iter([]), Iterator))
print(isinstance(iter(()), Iterator))
print(isinstance(iter({}), Iterator))
print(isinstance(iter(''), Iterator))
