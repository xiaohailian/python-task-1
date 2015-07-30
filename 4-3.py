#coding:utf-8
#月球上你的体重是在地球上的16.5%，假设你每年增长1公斤，打印未来15年你的体重状况

realweight = 50
weight = realweight * 0.16
for i in range(15):
    print("在地球上第 %s 年你的体重是 %s"%(i,realweight))
    print('在月球上第%s年你的体重是%s'%(i,realweight * 0.16))
    realweight = realweight + 1
