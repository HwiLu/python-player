# 装饰器框架

def outer(func):
    def inner():
        pass
    return inner

fun():
    pass

# 用的较少
'''

概念：是一个闭包，把一个函数当做参数,返回一个替代版的函数，本质上就是一个返回函数的函数

'''
#简单的装饰器
def func1():
    print("hell world")

def outer(func): 
    def inner():
        print("*******************")
        func()
    return inner
#f是函数func1的加强版本
f = outer(func1)
f()

# 复杂一点的装饰器
def outer(func):
    def inner(age):
        if age < 0:
            age = 0
        func(age)
    return inner

#使用@符号将装饰器应用到函数
#@python2.4支持使用@符号
@outer   #相当于say = outer(say)
def say(age):
    print("sunck is %d years old" % (age))

say(-10)
