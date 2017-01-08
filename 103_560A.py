# coding=utf-8
# 560A. Currency System in Geraldion

n=int(raw_input())
a=map(int,raw_input().split())
if 1 in a:
	print -1
else:
	print 1

"""
input
5
1 2 3 4 5
output
-1

http://codeforces.com/problemset/problem/560/A
Geraldion有自己的货币系统，现在有这些面值的钱，可以用这些钱的子集的和来表示不同的钱数，
问不能表示的最小的钱是多少。

分析了一下，有1就能表示所有的，而没有1不能表示的最小的就是1
"""