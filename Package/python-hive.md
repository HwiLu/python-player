'''	
'''

# 安装python 3.6.3
- python update
  https://www.jianshu.com/p/ae6cd13ce0f1
  
  安装时出现
  ```
  zlib data not available
  ```
  安装zlib-devel-1.2.7-0.10.128.x86_64.rpm

  启动python出现
    
  ```
  import readline ImportError: No module named readline
  ```
  
  安装

  libreadline5-5.2-147.17.30.x86_64.rpm     
  
  
# 安装pyhive所需依赖包
  
  顺序及版本
- 顺序

	- six> future>pure>ply

  tar -zvxf 
  
  python setup.py install

	- sasl>thrift>thrift-sasl>pyhive

  tar -zvxf 
  
  python setup.py install
- 版本
  
```
localhost# ll *.tar.gz
-rw-r--r-- 1 root root  41221 Jun 20 10:14 PyHive-0.5.1.tar.gz
-rw-r--r-- 1 root root 824484 Jun 20 10:14 future-0.16.0.tar.gz
-rw-r--r-- 1 root root 159130 Jun 20 10:14 ply-3.11.tar.gz
-rw-r--r-- 1 root root  10950 Jun 20 10:14 pure-sasl-0.5.0.tar.gz
-rw-r--r-- 1 root root  30409 Jun 20 10:14 sasl-0.2.1.tar.gz
-rw-r--r-- 1 root root  29860 Jun 20 10:14 six-1.11.0.tar.gz
-rw-r--r-- 1 root root  52467 Jun 20 10:14 thrift-0.11.0.tar.gz
-rw-r--r-- 1 root root   3761 Jun 20 10:14 thrift_sasl-0.3.0.tar.gz
```

- 安装sasl出现

```vim
   gcc -pthread -fno-strict-aliasing -g -O2 -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -fPIC -Isasl -I/usr/local/include/python2.7 -c sasl/saslwrapper.cpp -o build/temp.linux-x86_64-2.7/sasl/saslwrapper.o  
    cc1plus: warning: command line option "-Wstrict-prototypes" is valid for Ada/C/ObjC but not for C++  
    In file included from sasl/saslwrapper.cpp:254:  
    sasl/saslwrapper.h:22:23: error: sasl/sasl.h: No such file or directory  
    In file included from sasl/saslwrapper.cpp:254:  
```
安装
cyrus-sasl-devel-2.1.22-182.20.1.x86_64.rpm、python-devel-2.6.8-0.15.1.x86_64.rpm

 
 - 安装gcc-c++【rpm -ivh gcc47-c++-4.7.2_20130108-0.15.45.x86_64.rpm】出现
 ```
  rpm -ivh gcc47-c++-4.7.2_20130108-0.15.45.x86_64.rpm 
error: Failed dependencies:
	gcc47 = 4.7.2_20130108-0.15.45 is needed by gcc47-c++-4.7.2_20130108-0.15.45.x86_64
	libstdc++47-devel = 4.7.2_20130108-0.15.45 is needed by gcc47-c++-4.7.2_20130108-0.15.45.x86_64
	libcloog.so.0()(64bit) is needed by gcc47-c++-4.7.2_20130108-0.15.45.x86_64
	libmpc.so.2()(64bit) is needed by gcc47-c++-4.7.2_20130108-0.15.45.x86_64
	libppl.so.9()(64bit) is needed by gcc47-c++-4.7.2_20130108-0.15.45.x86_64
	libppl_c.so.4()(64bit) is needed by gcc47-c++-4.7.2_20130108-0.15.45.x86_64

```
安装
```
cpp47-4.7.2_20130108-0.15.45.x86_64.rpm      libcloog0-0.15.10+ppl-4.7.1.x86_64.rpm        
libmpc2-0.8.2-1.7.1.x86_64.rpm          libstdc++47-devel-4.7.2_20130108-0.15.45.x86_64.rpm
gcc47-4.7.2_20130108-0.15.45.x86_64.rpm      libppl9-0.11.2-3.7.25.x86_64.rpm       
libppl_c4-0.11.2-3.7.25.x86_64.rpm        
这些lib包，均为gcc所需依赖包
```

**注意**

所有包，必须与操作系统版本严格对应吗，谨慎使用--nodeps参数，否则后面会很难受。
