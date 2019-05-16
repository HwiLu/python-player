

#编码
path = r"C:\Users\xlg\Desktop\Python-1704\day08\1-文件读写\file5.txt"
with open(path, "wb") as f1:
    str = "sunck is a good man凯"
    f1.write(str.encode("utf-8"))

with open(path, "rb") as f2:
    data = f2.read()
    print(data)
    print(type(data))
    newData = data.decode("utf-8")
    print(newData)
    print(type(newData))

















