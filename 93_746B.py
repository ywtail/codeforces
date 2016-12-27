# coding=utf-8
# 746B. Decoding 解码

n=int(raw_input())
s=raw_input()

ans=""
if n%2==1:
	for i in range(n):
		if i%2==0:
			ans=ans+s[i]
		else:
			ans=s[i]+ans
else:
	for i in range(n):
		if i%2==1:
			ans=ans+s[i]
		else:
			ans=s[i]+ans
print ans

"""
input
5
logva
output
volga

input
2
no
output
no

input
4
abba
output
baba

http://codeforces.com/problemset/problem/746/B
编码规则：每次将中间字母取出，如果长度是偶数，取靠左的数

解码即每次将字符写在现有字符串左边或者右边，找规律
"""