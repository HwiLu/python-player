#存储5个人的年龄，求他们的平均年龄
age1 = 18
age2 = 19
age3 = 20
age4 = 21
age5 = 22
print((age1 + age2 + age3 + age4 + age5) / 5)

#思考：要存储100个人的年龄，难道要定义100个变量？？
#解决：使用列表
#本质：是一种有序的集合


'''创建列表
格式：列表名 = [列表选项1, 列表选项2, ……, 列表选项n]
'''
#创建了一个空列表
list1 = []
print(list1)
#创建带有元素的列表
list2 = [18, 19, 20, 21, 22]
index = 0
sum = 0
#嵌套最好不要超过3层
while index < 5:
    sum += list2[index]
    index += 1
    if index == 5:
        print("平均年龄:%d" % (sum / 5))
#注意：列表中的元素数据可以是不同类型的
list3 = [1, 2, "sunck", "good", True]
print(list3)

#列表元素的访问
#注意不要越界(下标超出了可表示的范围)
#取值  格式：列表名[下标]
list4 = [1,2,3,4,5]
print(list4[2])

#替换
list4[2] = 300
print(list4)

#列表操作：
#列表组合
list5 = [1,2,3]
list6 = [4,5,6]
list7 = list5 + list6
print(list7)

#列表的重复
list8 = [1,2,3]
print(list8 * 3)

#判断元素是否在列表中
list9 = [1,2,3,4,5]
print(3 in list9)
print(6 in list9)

#列表截取
list10 = [1,2,3,4,5,6,7,8,9]
print(list10[2:6])
print(list10[3:])
print(list10[:5])

#二维列表
    #其元素也是列表
list11 = [[1,2,3], [4,5,6], [7,8,9]]
print(list11[1][1])

#列表方法
#append   在列表中末尾添加新的元素
list12 = [1,2,3,4,5]
list12.append(6)
list12.append([7,8,9])
print(list12)

#在末尾一次性追加另一个列表中的多个值
list13 = [1,2,3,4,5]
list13.extend([6,7,8])
print(list13)

#在下标处添加一个元素，不覆盖原数据，原数据向后顺延
list14 = [1,2,3,4,5]
list14.insert(2, 100)
list14.insert(2, [200,300])
print(list14)


#pop(x=list[-1])
#移除列表中指定下标处的元素（默认移除最后一个元素）,并返回删除的数据
list15 = [1,2,3,4,5]
list15.pop()
list15.pop(2)
print(list15.pop(1))
print(list15)

#remove  移除列表中的某个元素第一个匹配的结果
list16 = [1,2,3,4,5,4,5,4]
list16.remove(4)
print(list16)

#清除列表中所有的数据
list17 = [1,2,3,4,5]
list17.clear()
print(list17)

#从列表中找出某个值第一个匹配的索引值
list18 = [1,2,3,4,5, 3,4,5,6]
index18 = list18.index(3)
#圈定范围
index19 = list18.index(3, 3, 7)
print(index18, index19)


#列表中元素个数
list20 = [1,2,3,4,5]
print(len(list20))

#获取列表中的最大值
list21 = [1,2,3,4,5]
print(max(list21))

#获取列表中的最小值
list22 = [1,2,3,4,5]
print(min(list22))


#查看元素在列表中出现的次数
list23 = [1,2,3,4,5,3,4,5,3,3,5,6]
print(list23.count(3))

num24 = 0
all = list23.count(3)
while num24 < all:
    list23.remove(3)
    num24 += 1
print(list23)

#倒叙
list25 = [1,2,3,4,5]
list25.reverse()
print(list25)

#排序  升序
list26 = [2,1,3,5,4]
list26.sort()
print(list26)

#拷贝
#浅拷贝   引用拷贝
list27 = [1,2,3,4,5]
list28 = list27
list28[1] = 200
print(list28)
print(list27)
print(id(list28))
print(id(list27))
#深拷贝   内存的拷贝
list29 = [1,2,3,4,5]
list30 = list29.copy()
list30[1] = 200
print(list29)
print(list30)
print(id(list29))
print(id(list30))

#将元组转成列表
list31 = list((1,2,3,4))
print(list31)
