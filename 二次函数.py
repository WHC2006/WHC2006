import math

def derta(a,b,c):
	return b**2-4*a*c

def kaifang_n(i):
	f=1
	for y in range(1,i//2):
		if y**2<=i:
			if i%(y**2)==0:
				if y>=f:
					f=y
	if f==1:
		return i
	else:
		return i//f**2

def kaifang_w(i):
	f=0
	for y in range(1,i//2):
		if y**2<=i:
			if i%(y**2)==0:
				if y>=f:
					f=y
	if f==1:
		return f
	else:
		return f

while True:
	print('y=ax^2 + bx +c')
	a=int(input('a='))
	b=int(input('b='))
	c=int(input('c='))
	if a==0:    
		print('数学错误')
	else:
		print('当y=0时')
		if b>=0:
			print('0='+str(a)+'x^2+'+str(b)+'x+'+str(c))
		elif b<0:
			print('0='+str(a)+'x^2'+str(b)+'x+'+str(c))
		print('解得')
		yue=math.gcd(2*a,b,kaifang_w(derta(a,b,c)))
		if kaifang_n(derta(a,b,c))==1:
			print('x1=',(-b+kaifang_w(derta(a,b,c)))/(2*a))
			print('x2=',(-b-kaifang_w(derta(a,b,c)))/(2*a))
		print('与x轴的交点为')
		print('(',(-b+kaifang_w(derta(a,b,c)))/(2*a),',',0, ')')
		print('(',(-b-kaifang_w(derta(a,b,c)))/(2*a),',',0, ')')
		print('当x=0时')
		print('y='+str(c))
		print('与y轴交与（0，'+str(c)+')')
		if (b/(a*2))>=0:
			print('y='+str(a)+'(x+'+str(b/(a*2))+')^2-'+str(derta(a,b,c)/(4*a)))
		elif (b/(a*2))<0:
			print('y='+str(a)+'(x'+str(b/(a*2))+')^2-'+str(derta(a,b,c)/(4*a)))
		print('顶点坐标为('+str(-(b/(a*2)))+','+str(-(derta(a,b,c)/(4*a)))+')')
		print('对称轴为x='+str(-(b/(a*2))))
		if a>0:
			print('y的最小值为'+str(-(derta(a,b,c)/(4*a))))
		else:
			print('y的最大值为'+str(-(derta(a,b,c)/(4*a))))
		input("Press Enter to continue...")
