a=raw_input().lstrip("0")
b=raw_input().lstrip("0")

def compare(a,b):
	for i in xrange(0,len(a)):
		if a[i]<b[i]:
			print "<"
			return
		if a[i]>b[i]:
			print ">"
			return
	print "="
	return

if len(a)<len(b):
	print "<"
elif len(a)>len(b):
	print ">"
else:
	compare(a,b)
