#coding=utf-8

def func():
	n=int(raw_input())
	ai=map(int,raw_input().split())
	bi=map(int,raw_input().split())
	del ai[ai.index(0)]
	del bi[bi.index(0)]
	temp=ai.index(bi[0])
	ai=ai[temp:]+ai[:temp]
	for i in range(n-1):
		if ai[i]!=bi[i]:
			print "NO"
			return
	print "YES"
	return

func()