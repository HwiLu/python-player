## while 循环写法


```python
num = 1
while num <= 5:
    print(num)
    num += 1


#计算1+2+3+……+100
sum = 0
num = 1
while num <= 100:
    sum += num   #1+……+99 + 100
    num += 1
print("sum = %d" % (sum))
'''
0 + 1
1 + 2
3 + 3
6 + 4
'''
# 打印str字符串中的每个字符
str = "sunck is a handsome man"
index = 0
while index <  len(str):   #  index < 19
    print("str[%d] = %s" % (index, str[index]))
    index += 1
```

## for循环

```python
#!/usr/bin/python
# -*- coding: UTF-8 -*-
 '''
    http://www.runoob.com/python/python-for-loop.html
 '''
for letter in 'Python':     # 第一个实例
   print('当前字母 :', letter)
 
fruits = ['banana', 'apple',  'mango']
for fruit in fruits:        # 第二个实例
   print('当前水果 :', fruit)
print("Good bye!")
```
## continue语句

作用：跳过当前循环中的剩余语句，然后继续下一次循环
注意：跳过距离最近的循环
```python

for i in range(10):
    print(i)
    if i == 3:
        continue
    print("*")
    print("&")
```
## break语句：
作用：跳出for和while循环
注意：只能跳出距离他最近的那一层循环
```python
for i in range(10):
    print(i)
    if i == 5:
        #结束这个循环
        break
 ```
