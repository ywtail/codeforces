#coding=utf-8

n,a,b=map(int,raw_input().split())
ans=a+(n+b)%n
if ans>n:
	ans=ans%n
print ans

#找规律，注意ans有可能>n

"""
input
3 2 -100
output
1

input
3 3 -100
output
2
"""