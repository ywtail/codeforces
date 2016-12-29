# coding=utf-8
# 733B. Parade 阅兵式

n=int(raw_input())
minus=[]
for i in range(n):
	l,r=map(int,raw_input().split())
	minus.append(l-r)
mi=min(minus)
mi_index=minus.index(mi)+1
ma=max(minus)
ma_index=minus.index(ma)+1
if ma<=0 or mi>=0:
	print 0
else:
	print [mi_index,ma_index][abs(sum(minus)-2*mi)<abs(sum(minus)-2*ma)]

"""
input
3
5 6
8 9
10 3
output
3

input
2
6 5
5 6
output
1

input
6
5 9
1 3
4 8
4 5
23 54
12 32
output
0

http://codeforces.com/problemset/problem/733/B
n
l r
l是伸左腿的人数，r伸右腿
行数编号1-n
可以选一行纠正伸腿，问选哪一行使beauty =|sum(l)-sum(r)|最大

每行求差
只选一行，要么选负数里绝对值最大的（即min），要么选正数里最大的max
两个对比即得到答案
"""