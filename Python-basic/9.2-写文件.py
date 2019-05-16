import time
path = r"C:\Users\xlg\Desktop\Python-1704\day08\1-文件读写\file2.txt"
f = open(path, "a")


#写文件
#1、将信息写入缓冲区
f.write("sunck in")

#2、刷新缓冲区
#直接把内部缓冲区的数据立刻写入文件，而不是被动的等待自动刷新缓冲区写入
f.flush()


f.close()



with open(path, "a") as f2:
    f2.write("good man")





