n,b,d=map(int,raw_input().split())
sizeList=map(int,raw_input().split())
total=0
j=0

for i in xrange(0,n):
	if sizeList[i]<=b:
		total=total+sizeList[i]
		if total>d:
			total=0
			j+=1

print j