# coding=utf-8
# 750A. New Year and Hurry

import math
n,k=map(int,raw_input().split())
t=(240-k)/5
ans=0
for i in range(1,n+1):
	if t>=i:
		t-=i
		ans+=1
	else:
		break
print ans

"""
input
3 222
output
2

input
4 190
output
4

input
7 1
output
7

http://codeforces.com/problemset/problem/750/A
"""