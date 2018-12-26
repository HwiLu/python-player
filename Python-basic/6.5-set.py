
'''
set:类似dict，是一组key的集合，不存储value
本质：无序和无重复元素的集合
'''

#创建
#创建set需要一个list或者tuple或者dict作为输入集合
#重复元素在set中会自动被过滤
s1 = set([1,2,3,4,5,3,4,5])
print(s1)
s2 = set((1,2,3,3,2,1))
print(s2)
s3 = set({1:"good", 2:"nice"})
print(s3)

'''
{1, 2, 3, 4, 5}
{1, 2, 3}
{1, 2}
'''

#添加
s4 = set([1,2,3,4,5])
s4.add(6)
s4.add(3) #可以添加重复的，但是不会有效果
#s4.add([7,8,9]) #set的元素不能是列表，因为列表是可变的
s4.add((7,8,9))
#s4.add({1:"a"}) #set的元素不能是字典，因为字典是可变的
print(s4)

#插入整个list、tuple、字符串，打碎插入
s5 = set([1,2,3,4,5])
s5.update([6,7,8])
s5.update((9,10))
s5.update("sunck")
print(s5)

#删除
s6 = set([1,2,3,4,5])
s6.remove(3)
print(s6)

#遍历
s7 = set([1,2,3,4,5])
for i in s7:
    print(i)
#set没有索引的
#print(s7[3])

for index, data in enumerate(s7):
    print(index, data)
s8 = set([1,2,3])
s9 = set([2,3,4])

#交集
a1 = s8 & s9
print(a1)
print(type(a1))

#并集
a2 = s8 | s9
print(a2)
print(type(a2))
