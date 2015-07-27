#coding:utf-8
#循环递增打印年龄，若年龄为偶数，则从2开始打印；若年龄为奇数，则从1开始打印
age = 23
if age % 2 == 0:  #若岁数为偶数，则从2开始打印
    for i in range(2,age):
        print('your ages is %s'%i)
else:           #若岁数为奇数，则从1开始打印
    for i in range(1,age):
        print('your ages is %s'%i)