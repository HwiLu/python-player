# 特点： 先进后出
#模拟栈结构
stack = []

#压栈(向栈里存数据)
stack.append("A")
print(stack)
stack.append("B")
print(stack)
stack.append("C")
print(stack)



#出栈(在栈里取数据)
res1 = stack.pop()
print("res1 =", res1)
print(stack)
res2 = stack.pop()
print("res2 =", res2)
print(stack)
res3 = stack.pop()
print("res3 =", res3)
print(stack)
