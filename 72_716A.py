#coding=utf-8

n,c=map(int,raw_input().split())
ti=map(int,raw_input().split())
num=1

for i in range(1,n):
	if ti[i]-ti[i-1]>c:
		num=1
	else:
		num+=1
print num