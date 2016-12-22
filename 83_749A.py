#coding=utf-8
#749A. Bachgold Problem

n=int(raw_input())
print n/2
for i in range(n/2-1):
	print 2,
if n%2==0:
	print 2
else:
	print 3

"""
5

2
2 3

题目：
http://codeforces.com/contest/749/problem/A
给出整数n，n可以由k个素数相加得到，使k尽量大。
求k和这些素数

解答：观察发现，所有的素数都可以由2和3相加得到。奇数由一个3贡献。
"""