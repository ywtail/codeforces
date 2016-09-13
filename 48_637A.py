from collections import Counter

n=int(raw_input())
ais=raw_input().split()
countais=dict(Counter(ais))

sortcount=sorted(countais.iteritems(),key=lambda d:d[1],reverse=True)

maxid=sortcount[0][0]
maxi=ais[::-1].index(maxid)

for i in xrange(1,len(sortcount)):
	if sortcount[i][1]==sortcount[0][1]:
		temp=ais[::-1].index(sortcount[i][0])
		if temp>maxi:
			maxi=temp
			maxid=sortcount[i][0]

print maxid