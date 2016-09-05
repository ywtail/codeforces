s=raw_input()
newList=s.split('a')
string=""


if len(s.replace('a',''))==0:
		print (len(s)-1)*'a'+'z'
else:
	for i in xrange(0,len(newList)):
		if newList[i]!='':
			newString=newList[i]
			break

	for j in xrange(0,len(newString)):
		string+=chr(ord(newString[j])-1)

	temp=s.index(newString)
	print s[:temp]+string+s[temp+len(newString):]