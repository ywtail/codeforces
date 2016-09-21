n,a,b=map(int,raw_input().split())

if n>a*b:
	print "-1"
else:
	outputs=range(1,n+1)+[0 for i in range(a*b-n)]	
	flag=1
	for i in xrange(a):
		for j in range(b-1): 
			print outputs[i*b:(i*b+b)][::flag][j],
		print outputs[i*b:(i*b+b)][::flag][b-1]
		flag=-flag