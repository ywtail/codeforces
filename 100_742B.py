# coding=utf-8
# 742B神奇的异或

n,x=map(int,raw_input().split())
a=map(int,raw_input().split())
ans=0
temp={}
for i in range(n):
	if a[i] in temp:
		ans+=temp[a[i]]
	if a[i]^x in temp:
		temp[a[i]^x]+=1
	else:
		temp[a[i]^x]=1
print ans

"""
input
2 3
1 2
output
1

input
6 1
5 1 2 3 4 1
output
2

http://codeforces.com/contest/742/problem/B
输入n和一个整数x，以及数组a
a中两个数异或=x，要求这两个数的下标i和j符合i<j这一条件
问有多少组这样的数

注意如果x=3,a=[1,2,2]，那么答案是2，因为2出现了两次，相当于有2组数满足条件
"""