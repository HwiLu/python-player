## 为什么Python速度慢还用它？
答：Python的几大特性。

计算密码型消费大量CPU资源。需解释为CPU可识别的机器码。所以python不适合作为计算密集型作业的语言。
IO密集型作业CPU不会成为瓶颈。所以作业运行速度不会受到Python解释为CPU可识别的机器码时速度慢的影响。所有Python适合于IO密集型作业。


Python的可嵌套性。Python发布程序的时候发布的是源代码，而类似C语言的编译型语言发布为只有机器能看懂的二进制文件。如果希望发布的Python代码中部分不给别人看懂，可以嵌入C语言代码。
计算密集型和IO密集型。

Python：解释型语言。

## 为什么使用计算机？

计算和存储数据。
数据存在哪里？

内存里。

存在disk里的数据叫做持久化数据。

32位操作系统寻址空间较小。最大只能匹配到约4G内存。64位操作系统理论上来说寻址空间是无限大。

### 计算机如何存储数据？
所有数据转化为二进制存储。
抽象理解：
  一个开关，有两种状态，开启和关闭。一种状态对应1，另一种对应0。把8个开关放在一个房间里面，这个房间叫做一个字节。一个开关代表一位。每个房间房间都有门牌号，
  看做地址。把无数开关堆叠起来组成摩天大厦，摩天大厦可以看做内存。
  
 内存地址使用十六进制表示。
## Python程序开头
```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Hwilu
# @Date:   2017-06-19 
# @Last Modified by:   HwiLu
# @Last Modified time: 2017-07-19  06:12:30
```

##注释
```python
注释一行
# 一行
注释多行
'''
    1行
    2行
    3行
'''

"""
    1行
    2行
    3行

"""
```
## first python programe
```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Hwilu
# @Date:   2017-06-19 
# @Last Modified by:   HwiLu
# @Last Modified time: 2017-07-19  06:12:30

print ("hello world")
```
