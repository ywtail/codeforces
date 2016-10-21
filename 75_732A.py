#coding=utf-8

k,r=map(int,raw_input().split())
t=k%10
for i in range(1,11):
	if t*i%10==0 or t*i%10==r:
		print i
		break