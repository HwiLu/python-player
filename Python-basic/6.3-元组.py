'''
tuple

本质：是一种有序集合

特点：
1、与列表非常相似
2、一旦初始化就不能修改--元组的元素不能变
3、使用小括号
'''
#创建tuple
#格式：元组名 = (元组元素1, 元组元素2, ……, 元组元素n)
#创建空的元组
tuple1 = ()
print(tuple1)
#创建带有元素的元组
#元组中的元素的类型可以不同
tuple2 = (1, 2, 3, "good", True)
print(tuple2)
#定义只有一个元素的元组
tuple3 = (1, )
print(tuple3)
print(type(tuple3))

#元组元素的访问
#格式：元组名[下标]
#下标从0开始
#取值
tuple4 = (1,2,3,4,5)
print(tuple4[0])
print(tuple4[1])
print(tuple4[2])
print(tuple4[3])
print(tuple4[4])
#print(tuple4[5]) #下标超过范围(越界)
#获取最后一个元素
print(tuple4[-1])

print(tuple4[-2])
print(tuple4[-5])
#print(tuple4[-6])#越界

#修改元组
tuple5 = (1,2,3,4,[5,6,7])
#tuple5[0] = 100  #报错，元组不能变
#tuple5[-1] = [7,8,9]
tuple5[-1][0] = 500
print(tuple5)

#删除元组
tuple6 = (1,2,3)
del tuple6

#print(tuple6)

#元组的操作
t7 = (1,2,3)
t8 = (4,5,6)

#拼接
t9 = t7 + t8
print(t9)
print(t7, t8)

#元组重复
t10 = (1,2,3)
print(t10 * 3)

#判断元素是否在元组中
t11 = (1,2,3)
print(4 in t11)

#元组的截取
#格式：元组名[开始下标:结束下标]
#从开始下标开始截取，截取到结束下标之前
t12 = (1,2,3,4,5,6,7,8,9)
print(t12[3:7])
print(t12[3:])
print(t12[:7])

#二维元组:  元素为一维元组的元组
t13 = ((1,2,3),(4,5,6),(7,8,9))
print(t13[1][1])

#元组的方法

#len()   返回元组中元素的个数
t14 = (1,2,3,4,5)
print(len(t14))

#max()   返回元组中的最大值
#min()
print(max((5,6,7,8,9)))
print(min((5,6,7,8,9)))

#将列表转成元组
list = [1,2,3]
t15 = tuple(list)
print(t15)


#元组的遍历
for i in (1,2,3,4,5):
    print(i)
