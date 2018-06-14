#coding=utf-8
#!/usr/bin/env python
#1
for line in open('/tmp/hello.txt'):
        line=line.strip('\n')
        print line
print "\n"

#2
fo = open("/tmp/hello.txt", "r")

for line in fo.readlines():
        line=line.strip('\n')
        print line
fo.close


