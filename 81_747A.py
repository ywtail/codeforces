#coding=utf-8
import math
n=int(raw_input())
t=int(math.floor(math.sqrt(n)))
while t>0:
	if n%t==0:
		print t,n/t
		break
	else:
		t-=1

#题目：
#http://codeforces.com/problemset/problem/747/A
#n=ab，给定n，求a、b，要求a<=b且b-a尽量小