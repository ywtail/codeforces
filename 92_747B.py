# coding=utf-8
# 747B. Mammoth's Genome Decoding 猛犸基因组解码

from collections import Counter

def function():
	n=int(raw_input())
	s=raw_input()
	if n%4!=0:
		print "==="
	else:
		t=n/4
		counter=Counter(s)
		alphabet=['A','G','C','T']
		for key in counter:
			if key!="?":
				if counter[key]>t:
					print "==="
					return
				else:
					s=s.replace("?",key,t-counter[key])
					alphabet.remove(key)
		for a in alphabet:
			s=s.replace("?",a,t)
		print s

function()

"""
input
8
AG?C??CT
output
AGACGTCT

input
4
AGCT
output
AGCT

input
6
????G?
output
===

input
4
AA??
output
===

http://codeforces.com/problemset/problem/747/B
给定字符串长度n及字符串s，s由'A', 'C', 'G', 'T' and '?'组成
要求A G C T出现的次数相等

根据n可以确定这4个字符每个应该出现n/4次，
使用Counter统计计数，然后将?替换成需要的字符
"""