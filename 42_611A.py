s=raw_input().split()

week={5:53,6:53,7:52}
for i in xrange(1,5):
	week[i]=52

month={30:11,31:7}
for j in xrange(1,30):
	month[j]=12

if "week" in s:
	print week[int(s[0])]
else:
	print month[int(s[0])]
	