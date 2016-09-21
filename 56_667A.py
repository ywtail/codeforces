from __future__ import division
import math

d,h,v,e=map(int,raw_input().split())

drinkh=4*v/(math.pi*d*d)
if drinkh<=e:
	print "NO"
else:
	print "YES"
	print h/(drinkh-e)
