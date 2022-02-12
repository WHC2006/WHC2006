import os
import random#导入随机库
from datetime import datetime
from threading import Timer
cout=''
co=0
f1 = open('题目.txt', 'w', encoding='utf-8')
f1.write('')
f1.close()
f1 = open('题目.txt', 'a', encoding='utf-8')#创建初始文件
fang=[]
for v in range(16):
    fang.append(v**2)
num=0#计次变量
nump=0
numf=0
max_num=int(input())
def printTime(inc):
    global cout
    print(cout)
    t = Timer(inc, printTime, (inc,))
    if co==1:
        t.cancel()
    t.start()

printTime(0.5)

print('随机题目生成开始')
def derta(a,b,c):
    global nump,numf,max_num,cout
    ll=a**2-4*a*c
    if ll>=0 and ll in fang:#判别是否有实根并限制实根范围
        nump+=1
        bai=nump/max_num*100
        cout= '随机题目生成'+str('%.3f'%  bai)+'%' 
        

        return True#返回真
    else:
        numf+=1
        return False#返回假
while True:
    a=random.randint(1,10)#随机取abc值
    b=random.randint(0,10)
    c=random.randint(0,50)
    p=random.randint(0,6)#随机选题型
    if p==0:#题型1
        if derta(a,b,c):
            num+=1
            f1.write(str(a)+'K+'+str(b)+'X'+str(c)+'=0\n')#写入式子，K代表平方

    if p==1:#题型2
        if derta(a,-b,c):
            num+=1#计次
            f1.write(str(a)+'K-'+str(b)+'X+'+str(c)+'=0\n')

    if p==2:#题型3
        if derta(-a,b,c):
            num+=1
            f1.write('-'+str(a)+'K+'+str(b)+'X+'+str(c)+'=0\n')

    if p==3:#题型4
        if derta(-a,b,c):
            num+=1
            f1.write(str(b)+'X+'+str(c)+'='+str(a)+'K'+'\n')
    if p==4:#题型5
        if derta(a,b,c):
            n=random.randint(1,10)
            num+=1
            f1.write(str(n*a)+'K+'+str(n*b)+'X'+'=-'+str(n*c)+'\n')
    if p==5:#题型6
        if derta(a,b,-c):
            n=random.randint(1,10)
            num+=1
            f1.write(str(n*a)+'K+'+str(n*b)+'X'+'='+str(n*c)+'\n')
    if p==6:#题型
        if derta(1,b,c):
            num+=1
            f1.write(str(a)+'K+'+str(a*b)+'X'+'=-'+str(a*c)+'\n')

    if num==max_num:#设定题目数量
        break
f1.close()
#以下为去除重复部分
f1 = open('题目.txt', 'r', encoding='utf-8')
print('开始去重')
f2 = open('2.txt', 'w', encoding='utf-8')
f2.write('')
f2.close()
f2 = open('2.txt', 'a', encoding='utf-8')#创建最终文件
list1=[]
listlen=len(f1.read().split('\n'))
i=0
for line in open("题目.txt"):
    i+=1
    bai2=i/listlen*100
    
    if line not in list1:
        list1.append(line)
        cout='去重:'+ str('%.3f'%  bai2)+'%'
        
y=0
for i in list1:
    y+=1
    bai3=y/len(list1)*100
    cout='写入:'+ str('%.3f'%  bai3)+'%'
    co=1
    f2.write(i)#写入最终文件
f1.close()#关闭文件
f2.close()
