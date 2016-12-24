# coding=utf-8
# 740A. Alyona and copybooks

n,a,b,c=map(int,raw_input().split())
if n%4==0:
	print 0
else:
	t=4-n%4
	if t==1:
		print min(a,b+c,c*3)
	elif t==2:
		print min(a*2,b,c*2)
	else:
		print min(a*3,a+b,c)

"""
634074578 336470888 481199252 167959139

335918278

题目：http://codeforces.com/contest/740/problem/A
输入：n a b c
输出：再买k本需要耗费的钱  要求(n+k)%4==0
n：现有copybooks
a：买1本的钱
b：买2本的钱
c：买3本的钱

注意，缺1本时，不一定是a，还可能是b+c，还可能是c*3
依此类推
"""