'''
作业：
1、判断从键盘输入的成绩，大于90优秀，60-90,及格，0-60不及格，其他“不合法分数输入”
2、“qwertyuiopasdfghjklzxcvbnm”
a,截取前三个;
b,截取第二个到倒数第二个
c，一个间隔一个截取
3，a=10,b=20 交换a,b的值，两种方法
'''
#第一题
num = float(input())
if num >= 90:
    print('优秀')
elif num >= 60 and num < 90:
    print('及格')
elif num < 60 and num >= 0:
    print('不及格')
else:
    print('非法输入')
    
#第二题
str = 'qwertyuiopasdfghjklzxcvbnm'
str_1 = str[0:3]
print(str_1)
str_2 = str[1:-1]
print(str_2)
str_3 = str[::-1] #反转
print(str_3)
str_4 = str[::2] #间隔取值
print(str_4)

#第三题
a = 10
b = 20
#a,b = b,a
#print(a,b)
a = a + b
b = a - b
a = a - b
print(a,b)
