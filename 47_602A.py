xn,xb=map(int,raw_input().split())
x=map(int,raw_input().split())[::-1]
yn,yb=map(int,raw_input().split())
y=map(int,raw_input().split())[::-1]

xtemp=0
ytemp=0

for i in xrange(0,xn):
	xtemp+=x[i]*(xb**i)
for j in xrange(0,yn):
	ytemp+=y[j]*(yb**j)

if xtemp<ytemp:
	print "<"
elif xtemp==ytemp:
	print "="
else:
	print ">"