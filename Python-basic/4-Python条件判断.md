```python
if age < 0:
    print("娘胎里")
elif age <= 3:
    print("婴儿")
elif age <= 6:
    print("儿童")
elif age <= 18:
    print("童年")
elif age <= 30:
    print("青年")
elif age <= 40:
    print("壮年")
elif age <= 50:
    print("中年")
elif age <= 100:
    print("老年")
elif age <= 150:
    print("老寿星")
else:
    print("老妖怪")

#elif        else if
#每个el都是对它上面所有表达式的否定
```

## 布尔值与空值

```
'''
布尔值：一个布尔值只有True、False两种值，
'''
b1 = True
b2 = False
print(b1, b2)

'''
空值：是Python里一个特殊的值，用None表示。None不能理解为0，因为0是有意义的，而None是一个特殊值。
'''
n = None
print(n)

```
