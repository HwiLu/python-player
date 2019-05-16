import os

'''
os:包含了普遍的操作系统的功能
'''

#获取操作系统类型  nt->windows   posix->Linux、Unix或Mac OS X
print(os.name)

#打印操作系统详细的信息（windows不支持）
#print(os.uname())
'''
posix.uname_result(sysname='Darwin', nodename='sunck.local', release='15.5.0', version='Darwin Kernel Version 15.5.0: Tue Apr 19 18:36:36 PDT 2016; root:xnu-3248.50.21~8/RELEASE_X86_64', machine='x86_64')
'''

#获取操作系统中的所有环境变量
#print(os.environ)
#获取指定环境变量
#print(os.environ.get("APPDATA"))

#获取当前目录    ./a/
print(os.curdir)
#获取当前工作目录，即当前python脚本所在的目录
print(os.getcwd())

#以列表的形式返回指定目录下的所有的文件
print(os.listdir(r"C:\Users\xlg\Desktop\Python-1704\day08"))

#在当前目录下创建新目录
#os.mkdir(r"C:\Users\xlg\Desktop\Python-1704\day08\kaige")
#os.mkdir("sunck")

#删除目录
#os.rmdir("sunck")


#获取文件属性
#print(os.stat("sunck"))

#重命名
#os.rename("sunck", "kaige")


#删除普通文件
#os.remove("file1.txt")

#运行shell命令
#os.system("notepad")
#os.system("write")
#os.system("mspaint")
#os.system("msconfig")
#os.system("shutdown -s -t 500")
#os.system("shutdown -a")
#os.system("taskkill /f /im notepad.exe")



#有些方法存在os模块里，还有些存在于os.path
#查看当前的绝对路径
print(os.path.abspath("./kaige"))


#拼接路径
p1 = "C:\\Users\\xlg\\Desktop\\Python-1704\\day08\\"
p2 = r"sunck\abc\d"
#注意：参数2里开始不要有斜杠
#r"C:\Users\xlg\Desktop\Python-1704\day08\sunck"

p3 = "/root/sunck/home"
p4 = "kaige"
#/root/sunck/home/kaige
print(os.path.join(p3, p4))


#拆分路径
path2 = r"C:\Users\xlg\Desktop\Python-1704\day08\2-os模块\kaige.txt"
print(os.path.split(path2))

#获取扩展名
print(os.path.splitext(path2))

#判断是否是目录
print(os.path.isdir(path2))


#判断文件是否存在
path3 = r"C:\Users\xlg\Desktop\Python-1704\day08\函数也是一种数据类型.py"
print(os.path.isfile(path3))

#判断目录是否存在
path4 = r"C:\Users\xlg\Desktop\Python-1704\day081"
print(os.path.exists(path4))


#获得文件大小(字节)
print(os.path.getsize(path3))

#文件的目录
print(os.path.dirname(path3))
print(os.path.basename(path3))