n,d=map(int,raw_input().split())
s=0
record=[]
for i in xrange(0,d):
	lines=list(set(list(raw_input())))
	line="".join(lines)
	if(line=='1'):
		record.append(s)
		s=0
	else:
		s+=1
record.append(s)
print sorted(record)[-1]
