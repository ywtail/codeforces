#coding=utf-8

n=int(raw_input())
ai=map(int,raw_input().split())
for i in range(n-1):
	print ai[i]+ai[i+1],
print ai[n-1]