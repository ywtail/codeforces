# coding=utf-8
# 734A. Anton and Danik

n=int(raw_input())
s=sorted(raw_input())
if n%2==1:
	if s[n/2]=='A':
		print "Anton"
	else:
		print "Danik"
else:
	if s[n/2]!=s[n/2-1]:
		print "Friendship"
	elif s[n/2]=='A':
		print "Anton"
	else:
		print "Danik"

"""
6
ADAAAA

7
DDDAADA

6
DADADA

题目：
http://codeforces.com/problemset/problem/734/A
求字符串中A和B谁多。

排序后看中间是哪个字符。
"""