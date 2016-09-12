have=map(int,raw_input().split())
need=map(int,raw_input().split())

temp=0
s=0

for i in xrange(0,3):
	temp=have[i]-need[i]
	if temp>0:
		s+=temp/2
	else:
		s+=temp

if s<0:
	print "No"
else:
	print "Yes"