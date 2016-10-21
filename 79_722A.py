#coding=utf-8

n=int(raw_input())
time=raw_input().split(':')
h=int(time[0])
m=int(time[1])

if m>=60:
	time[1]='0'+time[1][1]

if n==24:
	if h>23:
		time[0]='0'+time[0][1]
else:
	if h==0:
		time[0]='10'
	elif h>12:
		if time[0][1]=='0':
			time[0]='10'
		else:
			time[0]='0'+time[0][1]

print time[0]+':'+time[1]
