'''
概述:
使用键-值(key-value)存储，具有极快的查找速度

注意：字典是无序的

key的特性：
1、字典中的key必须唯一
2、key必须是不可变对象
3、字符串、整数等都是不可变的，可以作为key
4、list是可变的，不能作为key

思考：保存多位学生的姓名与成绩

使用字典，学生姓名为key,学生成绩作为值

'''

dict1 = {"tom":60, "lilei":70}

#元素的访问
#获取：字典名[key]
print(dict1["lilei"])
#print(dict1["sunck"])#没有
print(dict1.get("sunck"))
ret = dict1.get("sunck")
if ret == None:
    print("没有")
else:
    print("有")

#添加
dict1["hanmeimei"] = 99
#因为一个key对应一个value,所以，多次对一个key的value赋值，其实就是修改值
dict1["lilei"] = 80
print(dict1)

#删除
#dict1.pop("tom")
#print(dict1)

#遍历
for key in dict1:
    print(key, dict1[key])

#print(dict1.values())
for value in dict1.values(): #[60,80,90]
    print(value)

#print(dict1.items())
for k, v in dict1.items():
    print(k, v)

for i, v2 in enumerate(dict1):
    print(i, v2)

#和list比较
#1、查找和插入的速度极快，不会随着key-value的增加而变慢
#2、需要占用大量的内存，内存浪费多

#list
#1、查找和插入的速度随着数据量的增多而减慢
#2、占用空间小，浪费内存少

w = input()
#w = "good"

str = "sunck is a good man!sunck is a nice man!sunck is a hands man!sunck is a good man!sunck is a nice man!sunck is a great man!sunck is a noble man!sunck is a cool man!"

#print(str.count(w))

#字典
