n,m=map(int,raw_input().split())
count=0
r=[]
if n<5:
	for i in xrange(1,n+1):
		count+=(i+m)/5
else:
	for i in xrange(1,5):
		c=(i+m)/5
		r.append(c)
	r.append(m/5)
	count+=n/5*sum(r)
	for j in xrange(0,n%5):
		count+=r[j]
print count
