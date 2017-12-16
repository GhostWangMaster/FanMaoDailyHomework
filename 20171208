import os
import csv
'''
1.获取目录
2.打开文件
3.读取文件内容
'''
filepath = os.path.join(os.getcwd(),'test.csv')   #参数可以是多个，如果有多层文件夹，就逐层加入该参数
file = open(filepath)
reader = csv.reader(file)
users = []
next(reader,2)
for i in reader:
    print(i)
    users.append(i)
print(users)
