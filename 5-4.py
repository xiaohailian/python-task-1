#coding:utf-8
#5-4计算体重，当前体重、体重的年增量和统计年数都由输入给出。
def weights():
    print('请输入你当前的体重：')
    realweight = int(input())
    print('请输入你预计每年的增量：')
    increase = int(input())
    print('请输入想计算的年数：')
    years = int(input())
    for i in range(years):
        print("第 %s 年你的体重是 %s"%(i,realweight))
        realweight = realweight + increase


weights()
