n,c=map(int,raw_input().split())
ps=map(int,raw_input().split())
ts=map(int,raw_input().split())

def func():
	ltime=0
	lpoints=0
	for i in range(n):
		ltime+=ts[i]
		lpoints+=max(ps[i]-c*ltime,0)

	rtime=0
	rpoints=0
	for i in range(n)[::-1]:
		rtime+=ts[i]
		rpoints+=max(ps[i]-c*rtime,0)
		if rpoints>lpoints:
			print "Radewoosh"
			return
	if lpoints>rpoints:
		print "Limak"
	else:
		print "Tie"

func()