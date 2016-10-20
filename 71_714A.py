#coding=utf-8

l1,r1,l2,r2,k=map(int,raw_input().split())

if l2>r1 or r2<l1:
	print 0
else:
	if r2<=r1:
		temp=max(l1,l2)
		ans=r2-temp+1
		if k>=temp and k<=r2:
			ans-=1
	else:
		temp=max(l1,l2)
		ans=r1-temp+1
		if k>=temp and k<=r1:
			ans-=1
	print ans