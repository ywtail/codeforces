# coding=utf-8
# 748A. Santa Claus and a Place in a Class

from __future__ import division
import math

n,m,k=map(int,raw_input().split())
r=int(math.ceil(k/(2*m)))
t=k-(r-1)*2*m
if t%2==0:
	print r,int(t/2),"R"
else:
	print r,int((t+1)/2),"L"

"""
http://codeforces.com/problemset/problem/748/A
简单数学问题
"""