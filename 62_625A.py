#coding=utf-8

n=int(raw_input())
a=int(raw_input())
b=int(raw_input())
c=int(raw_input())

temp=b-c
num=0

if n>a and a<=temp:
	num+=n/a
else:
	if n>b:  #防止超时
		t=(n-b)/temp
		num+=t
		n-=t*temp
	while n>=b:
		num+=1
		n-=temp
	if n>=a:
		num+=n/a

print num