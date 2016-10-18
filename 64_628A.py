#coding=utf-8

n,b,p=map(int,raw_input().split())
towels=n*p
num=0
while n>1:
	num+=n/2
	n=n/2+n%2
print num*(2*b+1),towels