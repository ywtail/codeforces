n=int(raw_input())
participants={}
for i in xrange(0,n):
	temp=raw_input().split()
	participants[temp[1]]=temp[2]

def func():
	for key in participants:
		if int(key)>=2400 and int(key)<int(participants[key]):
			print "YES"
			return
	print "NO"

func()