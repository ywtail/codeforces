# coding=utf-8
# 768A. Oath of the Night's Watch

from collections import Counter
n=int(raw_input())
a=map(int,raw_input().split())
if n<3:
	print 0
else:
	a=sorted(a)
	if a[0]==a[-1]:
		print 0
	else:
		if a[0]==a[-1]:
			print 0
		else:
			counter_a=Counter(a)
			print n-counter_a[a[0]]-counter_a[a[-1]]

"""
input
2
1 5
output
0

input
3
1 2 5
output
1

简而言之，找到在最大数和最小数之间数的个数
以为有可能重复，所以使用Counter计数
"""