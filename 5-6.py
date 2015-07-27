#coding:utf-8
#将上面6个函数写成一个模块，并写一个测试程序引用并写执行函数，打印执行结果。
from r55 import test

#5-1
game = ["羽毛球","看电影","打扑克"]
food = ["西瓜","香蕉","苹果","烤鸡"]
favorites_list = test.favorites_1(game,food)
print(favorites_list)


castles = 3  #建筑为3
ninija = 25   #每座有25个忍者
tunnels = 2    #每座有两个地道
warrior = 40   #每个地道有40个武士
test.total_1(castles,ninija,tunnels,warrior)

first_name = "肖"
second_name = "海连"
test.my_name_1(first_name,second_name)
print('test 5-1 end')

#5-2
realweight = 50
increase = 1
test.weights_2(realweight,increase)
print('test 5-2 end')


#5-3
realweight = 40
increase = 2
years = 10
test.weights_3(realweight,increase,years)
print('test 5-3 end')

#5-4
test.weights_4()
print('test 5-4 end')

