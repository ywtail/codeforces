n,m=map(int,raw_input().split())
inputs=""
for i in xrange(0,n):
	inputs+=raw_input()[1:]

def func(s):
	for i in xrange(1,m+1):
		if s.find(str(i))==-1:
			print "NO"
			return
	print "YES"
	return

func(inputs)
