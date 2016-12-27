# coding=utf-8
# 735A. Ostap and Grasshopper Ostap和蚱蜢

def function():
	n,k=map(int,raw_input().split())
	s=raw_input()

	g,t=sorted([s.index('G'),s.index('T')])
	if (t-g)%k==0:
		for i in range(1,(t-g)/k):
			if s[g+i*k]=='#':
				print "NO"
				return
		print "YES"
	else:
		print "NO"

function()

"""
input
5 2
#G#T#
output
YES

input
6 1
T....G
output
YES

input
7 3
T..#..G
output
NO

input
6 2
..GT..
output
NO

http://codeforces.com/problemset/problem/735/A
n k
s
从G跳到T，k是步长，“#”不可以跳
"""