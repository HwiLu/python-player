# 定义了一个无参无返回值的函数
def myPrint():
    print("sunck is a very good man!")
    print("sunck is a nice man!")
    print("sunck is a handsome man!")
myPrint()


#需求：编写一个函数，给函数一个字符串和一个年龄，在函数内部打印出来

#形参(形式参数)：定义函数时小括号中的变量，本质是变量
#参数必须按顺序传递，个数目前要对应
#def myPrint(str, age, hoby):
#    print(str, age)

def myPrint(str, age):
    print(str, age)

#实参(实际参数)：调用函数时给函数传递的数据，本质是值
myPrint("sunck is a good man", 18)

'''
函数的返回值
'''

#编写函数，实现功能，给函数两个数，返回这两个数的和
def mySum(num1, num2):
    #将结构返回给函数的调用者
    return num1 + num2
    #执行完return语句，该函数就结束了，return后面的代码不执行
    print("**********")
res = mySum(1, 2)
print(res)


'''
函数参数的传递
'''

'''
值传递：传递的不可变类型
string、tuple、number是不可变的
'''
def func1(num):
    print(id(num))
    num = 10
    print(id(num))

temp = 20
print(id(temp))
func1(temp)   #num = temp
print(temp)

'''
引用传递：传递的可变类型
list、dict、set是可变的
'''
def func2(lis):
    lis[0] = 100
li = [1,2,3,4,5]
func2(li)
print(li)

a = 10
b = 10
b = 40
print(id(a), id(b))

c = 20
d = 30
print(id(c), id(d))
d = c
print(id(c), id(d))


