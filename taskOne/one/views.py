#coding:utf-8
from django.shortcuts import render
from django import forms
from django.http import  HttpResponse
from django.shortcuts import render_to_response

# Create your views here.
#1-1
class Favorite(forms.Form):
    my_love_1 = forms.CharField()
    my_game= forms.CharField()

 #1-2
class Castle(forms.Form):
    castle = forms.IntegerField(label='建筑数') #建筑数
    ninija = forms.IntegerField(label='每个建筑的忍者数') #每个建筑的忍者数
    tunnel = forms.IntegerField(label='地道数')  #地道数
    warrier = forms.IntegerField(label='每个地道的武者数')  #每个地道的武者数


#1-3
class Name(forms.Form):
    first_name=forms.CharField(label='请输入你的姓：')
    second_name = forms.CharField(label='请输入你的名：')

#1-1
def my_favorite(request):
    if request.method == 'POST':
        like = Favorite(request.POST)
        if like.is_valid():
            a = like.cleaned_data
            # list = []
            # for k in a:
            #     list.append(a[k])
            return HttpResponse(u'喜欢的食物有:%s    <br><br>喜欢的体育有：%s'%(a['my_love_1'],a['my_game']))
    else:
        like = Favorite()
    return render_to_response('my_love.html',{'like':like})

#1-2
def total(request):
    ninijas = 0  #忍者的总数变量,初始化为0
    worriors = 0  #武士的总数变量，初始化为0
    totols = 0    #总的人数，初始化为0
    if request.method == 'POST':
        c = Castle(request.POST)
        if c.is_valid():
            t = c.cleaned_data
            print(t)
            ninijas = t['castle'] * t['ninija']
            worriors =t['tunnel'] * t['warrier']
            totols = ninijas + worriors
            return HttpResponse(u'忍者的总数为 %s <br><br> 武士的总数为 %s <br><br> 总人数为 %s'%(ninijas,worriors,totols))
    else:
        c = Castle()
    return render_to_response('castle.html',{'c':c})

#1-3
def my_name(request):
    if request.method =='POST':
        name = Name(request.POST)
        if name.is_valid():
            myName = name.cleaned_data
            first = myName['first_name']
            second = myName['second_name']
            return HttpResponse(u'你的名字是：<br>%s <br> %s'%(first.rjust(6),second.rjust(6)))

    else:
        name=Name()
    return render_to_response('myName.html',{'name':name})