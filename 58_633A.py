a,b,c=map(int,raw_input().split())

def func(a,b,c):
	if c%a==0 or c%b==0:
		print "Yes"
	else:
		if a>b:
			a,b=b,a
		for i in range(1,c/b+1):
			if (c-i*b)%a==0:
				print "Yes"
				return
		print "No"

func(a,b,c)