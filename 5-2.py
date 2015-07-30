#coding:utf-8
#5-2计算体重（参数为当前体重和体重的年增量）

def weights(curren_weight,an_increase):
    for i in range(15):
        print("第 %s 年你的体重是 %s"%(i,curren_weight))
        curren_weight = curren_weight + an_increase

realweight = 50
increase = 1
weights(realweight,increase)
