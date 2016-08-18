n,x=map(int,raw_input().split())
r=0
for i in xrange(0,n):
	d=raw_input().split()
	if d[0]=='+':
		x+=int(d[1])
	else:
		if x-int(d[1])<0:
			r+=1
		else:
			x-=int(d[1])
print x,r