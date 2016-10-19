#coding=utf-8

n,k,q=map(int,raw_input().split())
ti=map(int,raw_input().split())

online={} #保存显示的id和t
num=0
for i in range(q):
	typei,idi=map(int,raw_input().split())
	if typei==1:
		t=ti[idi-1]
		if num<k:
			online[idi]=t
			num+=1
			sort_online=sorted(online.iteritems(),key=lambda d:d[1])
		else:
			if t>sort_online[0][1]:
				del online[sort_online[0][0]] #每次删除t最小的，并重新排序选出t最小的
				online[idi]=t
				sort_online=sorted(online.iteritems(),key=lambda d:d[1])
	else:
		#print online
		if idi in online:
			print "YES"
		else:
			print "NO"

"""
input:
4 2 8
300 950 500 200
1 3
2 4
2 3
1 1
1 2
2 1
2 2
2 3

output:
NO
YES
NO
YES
YES

#########################
input:
6 3 9
50 20 51 17 99 24
1 3
1 4
1 5
1 2
2 4
2 2
1 1
2 4
2 3

output:
NO
YES
NO
YES
"""