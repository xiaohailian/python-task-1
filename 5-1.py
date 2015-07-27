#coding:utf-8
#函数化：任务一的:用列表game列出爱好，用列表列出喜欢的食物。把两个列表连在一起，并把结果打印出来
def favorites(a,b):
    favorite = [a,b]
    return favorite

game = ["羽毛球","看电影","打扑克"]
food = ["西瓜","香蕉","苹果","烤鸡"]
favorites_list = favorites(game,food)
print(favorites_list)


#函数化：任务一的：有三座建筑，每座藏有25个忍者，有两个地道，每个地道藏40个武士，问一共有多少人可以投入战斗？
def total(castles,ninija,tunnels,warrior):
    ninijas = castles * ninija   #忍者的总数
    warriors = tunnels * warrior  # 武士的总数
    totals = ninijas + warriors    #总的投入人数
    print('忍者的总数为 %s ,武士的总数为 %s ,总的投入人数为 %s .'%(ninijas,warriors,totals))

castles = 3  #建筑为3
ninija = 25   #每座有25个忍者
tunnels = 2    #每座有两个地道
warrior = 40   #每个地道有40个武士
total(castles,ninija,tunnels,warrior)


#函数化：任务一：创建连个变量，创建一个字符串，用占位符使用这两个变量打印你名字的信息
def my_name(firstName,secondName):
    print(firstName.rjust(6))
    print(secondName.rjust(5))

first_name = "肖"
second_name = "海连"
my_name(first_name,second_name)
