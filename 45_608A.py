n,s=map(int,raw_input().split())
floors=[]
for i in xrange(0,n):
	floors.insert(0,map(int,raw_input().split()))

floors.append([0,0])

time=s-floors[0][0]

for j in xrange(0,n):
	if floors[j][1]>time:
		time=floors[j][1]
	time+=(floors[j][0]-floors[j+1][0])

print time+floors[-1][0]
