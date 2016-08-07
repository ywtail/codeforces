from __future__ import division
import math

n,k=map(int,raw_input().split())
if n>k:
	print int(math.floor(n/k)+1)*k
elif n==k:
	print k*2
else:
	print k