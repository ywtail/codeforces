# coding=utf-8
# 776A. A Serial Killer

a,b=raw_input().split()
n=int(raw_input())
print a,b

for i in range(n):
	temp=raw_input().split()
	if a==temp[0]:
		a=temp[1]
	if b==temp[0]:
		b=temp[1]
	print a,b

'''
input
ross rachel
4
ross joey
rachel phoebe
phoebe monica
monica chandler
output
ross rachel
joey rachel
joey phoebe
joey monica
joey chandler

input
icm codeforces
1
codeforces technex
output
icm codeforces
icm technex

题目地址：http://codeforces.com/problemset/problem/776/A
题目大意：第一行初始值，从第三行开始，将空格前面的字符串替换为后面的。
之前用replace做的，报错了。原因：假设现在有abk k，要将k替换成a，就会变成aba k，而不是替换单个字符k。
'''