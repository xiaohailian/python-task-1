#coding:utf-8
#5-3计算体重（参数为当前体重、体重的年增量和统计的年数）
def weights(curren_weight,an_increase,years):
    for i in range(years):
        print("第 %s 年你的体重是 %s"%(i,curren_weight))
        curren_weight = curren_weight + an_increase

realweight = 50
increase = 1
years = 15
weights(realweight,increase,years)
