
import random#导入随机库
f1 = open('题目.txt', 'a', encoding='utf-8')#创建初始文件
fang=[]
for v in range(16):
    fang.append(v**2)
num=0#计次变量
nump=0
numf=0
def derta(a,b,c):
    global nump,numf
    ll=a**2-4*a*c
    if ll>=0 and ll in fang:#判别是否有实根并限制实根范围
        nump+=1
        print('TRUE',nump,numf)

        return True#返回真
    else:
        numf+=1
        print('FLASE',nump,numf)
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

    if num==300000000:#设定题目数量
        break

#以下为去除重复部分
f2 = open('2.txt', 'a', encoding='utf-8')#创建最终文件
list1=[]
for line in open("题目.txt"):
    if line not in list1:
        list1.append(line)
for i in list1:
    f2.write(i)#写入最终文件
f1.close()#关闭文件
f2.close()
