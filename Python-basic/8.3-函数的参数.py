## 关键字参数

'''
概念：允许函数调用时参数的顺序与定义时不一致

'''
def myPrint(str, age):
    print(str, age)

#使用关键字参数
myPrint(age = 18, str = "sunck is a good man")


## 默认参数
'''
概念：调用函数时，如果没有传递参数，则使用默认参数
'''
#以要用默认参数，最好将默认参数放到最后
def myPrint(str, age = 18):
    print(str, age)

myPrint("kaige")


## 不定长参数
'''
概念：能处理比定义时更多的参数
'''
#加了星号(*)的变量存放所有未命名的变量参数，如果在函数调用时没有指定参数，它就是一个空元组
def func(name, *args):
    print(name)
    print(type(args))
    for x in args:
        print(x)

func("sunck", "good", "nice", "handsom")

def mySum(*l):
    sum = 0
    for i in l:
        sum += i
    return sum
print(mySum(1,2,3,4,5,6,7))

#**代表简键值对的参数字典，和*所代表的意义类似
def func2(**kwargs):
    print(kwargs)
    print(type(kwargs))

func2(x=1, y=2, z=3)

def func3(*args, **kwargs):
    pass #代表一个空语句


## 匿名参数
'''
概念：不使用def这样的语句定义函数，使用lambda来创建匿名函数

特点：
1、lambda只是一个表达式，函数体比def简单
2、lambda的主体是一个表达式，而不是代码块，仅仅只能在lambda表达式中封装简单的逻辑
3、lambda函数有自己的命名空间,且不能访问自由参数列表之外的或全局命名空间的参数
4、虽然lambda是一个表达式且看起来只能写一行，与C和C++内联函数不同。

格式：lambda 参数1,参数2,……,参数n:expression
'''
sum = lambda num1, num2:num1 + num2
print(sum(1,2))
