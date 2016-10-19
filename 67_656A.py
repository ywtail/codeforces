#coding=utf-8

n=int(raw_input())
x=8092
if n<13:
	print 2**n
else:
	print 2**(n-13)*x

#并不是求2的阶乘
#Da Vinci在计算2的13次方时，使用4096*2=8192,少进了一位，变成8092，后面的直接乘以2就都是错的
"""
input
3
output
8

input
10
output
1024

input
35
output
33940307968
"""