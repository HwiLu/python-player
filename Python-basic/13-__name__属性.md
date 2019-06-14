

# `__name__`的作用



python模块中通常会定义很多变量和函数，这些变量和函数相当于模块中的一个功能，模块被导入到别的文件中，可以调用这些变量和函数。那么这时 `__name__` 的作用就彰显了，它可以标识模块的名字，可以显示一个模块的某功能是被自己执行还是被别的文件调用执行，假设模块A、B，模块A自己定义了功能C,模块B调用模块A，现在功能C被执行了：

如果C被A自己执行，也就是说模块执行了自己定义的功能，那么 __name__=='__main__'

**如果C被B调用执行，也就是说当前模块调用执行了别的模块的功能，那么__name__=='A'（被调用模块的名字）**

其实换一种说法也就是表示当前程序运行在哪一个模块中。

如存在以下模块，文件名为differ.py

```python
#coding:utf-8
def Differ():
    if __name__=='__main__':
        print('I execute myself')
        print ('%s'%__name__)
    else:
        print ('I was executed by others')
        print ('%s'%__name__)
Differ()

```

执行结果为：
```
 I execute myself

 __main__
```
如果有其他文件调用了该模块，如：

```python
import differ
print ('%s'%__name__)
differ.Differ()
```

output

```python
I was executed by others
differ
__main__
I was executed by others
differ
```

