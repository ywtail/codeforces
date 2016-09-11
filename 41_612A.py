n,p,q=map(int,raw_input().split())
s=raw_input()

def func(x):
	print n/x
	for k in xrange(0,n/x):
		print s[(x*k):(x*(k+1))]

mi,ma=sorted([p,q])

def function():
	for i in xrange(1,n/ma+1):
		if (n-ma*i)%mi==0:
			temp=(n-ma*i)/mi
			print i+temp
			for j in xrange(0,i):
				print s[(ma*j):(ma*(j+1))]
			for l in xrange(0,temp):
				print s[(ma*(j+1)):][(mi*l):(mi*(l+1))]
			return
	print "-1"
	return

if p+q==n:
	print "2"
	print s[:p]
	print s[p:]
elif n%p==0:
	func(p)
elif n%q==0:
	func(q)
else:
	function()