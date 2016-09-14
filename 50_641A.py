n=int(raw_input())
characters=raw_input()
intergers=map(int,raw_input().split())

temp=0
count=0

def func(temp):
	for count in xrange(0,n):
		if characters[temp]==">":
			temp+=intergers[temp]
			if temp>n-1:
				print "FINITE"
				return
		else:
			temp-=intergers[temp]
			if temp<0:
				print "FINITE"
				return
	print "INFINITE"
	return

func(temp)