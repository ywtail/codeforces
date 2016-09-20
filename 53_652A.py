from __future__ import division
import math

h1,h2=map(int,raw_input().split())
a,b=map(int,raw_input().split())

def func(h1,h2,a,b):
	day=0
	for i in xrange(0,dmax):
		if day>0:
			h=a*12+h1
		else:
			h=a*8+h1
		if h>=h2:
			print day
			return
		else:
			h1=h-12*b
			day+=1

if a<=b:
	if h1+8*a>=h2:
		print "0"
	else:
		print "-1"
else:
	dmax=int(math.ceil((h2-h1)/(8*(a-b))))
	func(h1,h2,a,b)

