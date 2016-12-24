# coding:utf-8
# 742A. 1378 n次幂的末位

n=int(raw_input())
if n==0:
	print 1
else:
	ans=[8,4,2,6]
	print ans[(n-1)%4]

"""
题目：http://codeforces.com/problemset/problem/742/A
1378 n次幂的末位，n取值从0开始
"""