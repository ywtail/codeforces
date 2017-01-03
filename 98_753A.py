# coding=utf-8
# 753A. Santa Claus and Candies

n=int(raw_input())
k=0
ans=[]
for i in range(1,n+1):
	if n-i>=0:
		n=n-i
		ans.append(i)
		k+=1
	else:
		ans[-1]=ans[-1]+n
		break
print k
for x in ans:
	print x,

"""
input
5
output
2
2 3

input
9
output
3
3 5 1

input
2
output
1
2 

http://codeforces.com/problemset/problem/753/A
将n分成不同的整数的和。
"""