n=int(raw_input())
m=int(raw_input())
sizes=[]
for i in xrange(0,n):
	sizes.append(int(raw_input()))

def func():
	sumsize=0
	count=0
	for x in sorted(sizes,reverse=1):
		sumsize+=x
		count+=1
		if sumsize>=m:
			print count
			return
		
func()