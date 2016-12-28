# coding:utf-8
# 743B. Chloe and the sequence; 找规律

n,k=map(int,raw_input().split())
while k!=2**(n-1):
	if k>2**(n-1):
		k=k-2**(n-1) 
	n-=1
print n

"""
input
3 2
output
2

input
4 8
output
4

http://codeforces.com/problemset/problem/743/B
1
1 2 1
1 2 1 3 1 2 1
In the first sample the obtained sequence is [1, 2, 1, 3, 1, 2, 1]. The number on the second position is 2.
In the second sample the obtained sequence is [1, 2, 1, 3, 1, 2, 1, 4, 1, 2, 1, 3, 1, 2, 1]. The number on the eighth position is 4.
"""