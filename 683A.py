a,x,y=map(int,raw_input().split())
if x>a or x<0 or y>a or y<0:
	print "2"
elif x==a or x==0 or y==a or y==0:
	print "1"
else:
	print "0"