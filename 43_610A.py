n=int(raw_input())

if n%2==1:
	print "0"
else:
	count=n/4
	if n%4==0:
		print count-1
	else:
		print count