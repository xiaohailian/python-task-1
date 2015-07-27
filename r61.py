#coding:utf-8
class weight(object):
    # def __init__(self,weights,an_increase,years):
    #     self.weights = weights
    #     self.an_increase = an_increase
    #     self.years = years

    # def caculate(self):
    #     for i in range(self.years):
    #         print("第 %s 年你的体重是 %s"%(i,self.weights))
    #         self.weights = self.weights + self.an_increase

    #test 5-2
    def caculate_2(self,weight2,increase,years=10):
        for i in range(years):
             print("第 %s 年你的体重是 %s"%(i,weight2))
             weight2 = weight2 + increase

    #test 5-3
    def caculate_3(self,weight3,increase,year):
         for i in range(year):
             print("第 %s 年你的体重是 %s"%(i,weight3))
             weight3 = weight3 + increase

    #test 5-4
    def caculate_4(self):
        print('请输入你当前的体重：')
        realweight = int(input())
        print('请输入你预计每年的增量：')
        increase = int(input())
        print('请输入想计算的年数：')
        years = int(input())
        return self.caculate_3(realweight,increase,years)

