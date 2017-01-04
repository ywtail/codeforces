# coding:utf-8
# 584A. Olesya and Rodion

n,t=map(int,raw_input().split())
l=len(str(t))
if n<l:
	print -1
elif n==l:
	print t
else:
	print t*10**(n-l)

"""
http://codeforces.com/problemset/problem/584/A
给出n和t，要求ans有n位并且能被t整除
注意：int不能len()，需要先转换为str
"""