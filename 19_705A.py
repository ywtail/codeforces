n=int(raw_input())
for i in xrange(0,n-1):
	if i%2==0:
		print "I hate that",
	else:
		print "I love that",
if n%2==0:
	print "I love it"
else:
	print "I hate it"