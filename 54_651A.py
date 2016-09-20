from __future__ import division
import math

a1,a2=map(int,raw_input().split())

m=0

def joystick(x1,x2):
	global m
	if x1==1 and x2==1:
		print m
		return
	elif x1<=2 and x2<=2:
		print m+1
		return
	else:
		temp=int(math.ceil(x2/2)-1)
		m+=temp
		x1+=temp
		x2-=temp*2
		joystick(x2,x1)

if a1>a2:
	a1,a2=a2,a1
joystick(a1,a2)	