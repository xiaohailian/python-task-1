#coding=utf-8
castles = 3  #建筑为3
ninija = 25   #每座有25个忍者
tunnels = 2    #每座有两个地道
warrior = 40   #每个地道有40个武士

ninijas = castles * ninija   #忍者的总数
print(ninijas)
warriors = tunnels * warrior  # 武士的总数
print(warriors)
total = ninijas + warriors    #总的投入人数
print(total)
