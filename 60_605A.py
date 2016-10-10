# coding=utf-8
n=int(raw_input())
ps=map(int,raw_input().split())

book=[0 for i in range(n+1)]
length=[1 for i in range(n+1)]

for i in range(n):
	temp=ps[i]
	book[temp]=1
	if book[temp-1]==1:
		length[temp]+=length[temp-1]

print n-max(length)