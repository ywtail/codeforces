#coding=utf-8
import math

n=int(raw_input())
ai=map(int,raw_input().split())
k=0
head=0
tail=n-1

def gcd(x,y):
	while y:
		t=y
		y=x%y
		x=t
	return x

def minsert(mvalue):
	global head,k,tail
	head+=1
	ai.insert(head,mvalue)
	k+=1
	head+=1
	tail+=1

while head<tail:
	a=ai[head]
	b=ai[head+1]
	if a==1:
		head+=1
	elif a%2==0 and b%2==0:
		minsert(1)
	elif b%a==0:
		minsert(1)
	else:
		flag=1
		if gcd(b,a)!=1:
			flag=0
			if gcd(b,a+1)==1:
				minsert(1)
			else:
				minsert(1)
		if flag:
			head+=1

print k
for k in ai:
	print k,

#插入任意正整数，所以插入1也可以