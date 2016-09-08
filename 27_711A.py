n=int(raw_input())
inputList=[]
for i in xrange(0,n):
	inputList.append(raw_input())

def dete():
	for j in xrange(0,n):
		if inputList[j].find("OO")!=-1:
			print "YES"
			inputList[j]=inputList[j].replace("OO","++",1)
			outputList="\n".join(inputList)
			print outputList
			return
	print "NO"
	return

dete()