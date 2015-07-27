#coding:utf-8
#创建列表并按照顺序循环打印物品的序号和物品名出来
goods = ['apple','desk','chairs','computer','mobile_phone']
for i in range(len(goods)):
    print('The number is %s for %s'%(i,goods[i]))