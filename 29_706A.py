from __future__ import division

a,b=map(int,raw_input().split())
n=int(raw_input())
times=[]
for i in xrange(0,n):
	x,y,v=map(int,raw_input().split())
	time=round(((x-a)**2+(y-b)**2)**0.5/v,20)
	times.append(time)

print sorted(times)[0]
