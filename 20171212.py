'''
阿姆斯特朗数，如果一个n位正整数等于各位数字n次方的和，我们称该数为阿姆斯特朗数，
如：1*3+5*3+3*3=153，那么153就是阿姆斯特朗数。
1000以内的阿姆斯特朗数有：1,2,3,4,5,6,7,8,9，153,370，371,407
写一个程序检测输入的数是否是阿姆斯特朗数
'''

num = int(input())
length = len(str(num))
if num < 1000 and num > 0:
    if length == 1:
        if num ** length == num:
            print(num ,'是阿姆斯特朗数')
        else:
            print(num,'不是阿姆斯特朗数')
    elif length == 2:
        shi = num // 10
        ge = num % 10
        if shi ** length + ge ** length == num:
            print(num, '是阿姆斯特朗数')
        else:
            print(num,'不是阿姆斯特朗数')
    else:
        bai = num // 100
        shi = num % 100 // 10
        ge = num % 10
        if shi ** length + ge ** length + bai ** length == num:
            print(num, '是阿姆斯特朗数')
        else:
            print(num,'不是阿姆斯特朗数')
else:
    print("您的输入有误！")
