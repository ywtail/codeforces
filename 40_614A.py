from __future__ import division
import math

l,r,k=map(int,raw_input().split())

a=int(math.ceil(math.log(l)/math.log(k)))
b=int(math.log(r)/math.log(k))

def func():
	for i in xrange(a,b+3):
		temp=k**i
		if l<=temp<=r:
			print temp,
		else:
			return

if a>b or k**a<l:
	print "-1"
else:
	func()