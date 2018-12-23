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

