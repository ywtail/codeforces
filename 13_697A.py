time=map(int,raw_input().split())
m=(time[2]-time[0])%time[1]
if time[2]-time[0]==1 or time[2]<time[0]:
	print "NO"
elif m==0 or m==1:
	print "YES"
else:
	print "NO"