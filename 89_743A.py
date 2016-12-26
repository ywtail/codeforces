#coding=utf-8
#743A. Vladik and flights

n,a,b=map(int,raw_input().split())
s=raw_input()
if s[a-1]==s[b-1]:
	print 0
else:
	print 1

"""
4 1 4
1010

1

题目：http://codeforces.com/problemset/problem/743/A
给出字符串长度和索引，相同输出0，否则输出1
"""