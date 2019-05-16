import pickle   #数据持久性模块

myList = (1,2,3,4,5,"s i a am ")
path = r"..\file6.txt"
f = open(path, "wb")
pickle.dump(myList, f)
f.close()


#读取
f1 = open(path, "rb")
tempList= pickle.load(f1)
print(tempList)
f1.close()



