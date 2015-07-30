#coding:utf-8

class test(object):
    #5-1函数化：任务一的:用列表game列出爱好，用列表列出喜欢的食物。把两个列表连在一起，并把结果打印出来
    def favorites_1(a,b):
        favorite = [a,b]
        return favorite

    #5-1函数化：任务一的：有三座建筑，每座藏有25个忍者，有两个地道，每个地道藏40个武士，问一共有多少人可以投入战斗？
    def total_1(castles,ninija,tunnels,warrior):
        ninijas = castles * ninija   #忍者的总数
        warriors = tunnels * warrior  # 武士的总数
        totals = ninijas + warriors    #总的投入人数
        print('忍者的总数为 %s ,武士的总数为 %s ,总的投入人数为 %s .'%(ninijas,warriors,totals))


    #5-1函数化：任务一：创建连个变量，创建一个字符串，用占位符使用这两个变量打印你名字的信息
    def my_name_1(firstName,secondName):
        print(firstName.rjust(6))
        print(secondName.rjust(5))

    #5-2计算体重（参数为当前体重和体重的年增量）
    def weights_2(curren_weight,an_increase):
        for i in range(15):
            print("第 %s 年你的体重是 %s"%(i,curren_weight))
            curren_weight = curren_weight + an_increase

    #5-3计算体重（参数为当前体重、体重的年增量和统计的年数）
    def weights_3(curren_weight,an_increase,years):
        for i in range(years):
            print("第 %s 年你的体重是 %s"%(i,curren_weight))
            curren_weight = curren_weight + an_increase


    #5-4计算体重，当前体重、体重的年增量和统计年数都由输入给出。
    def weights_4():
        print('请输入你当前的体重：')
        realweight = int(input())
        print('请输入你预计每年的增量：')
        increase = int(input())
        print('请输入想计算的年数：')
        years = int(input())
        for i in range(years):
            print("第 %s 年你的体重是 %s"%(i,realweight))
            realweight = realweight + increase

