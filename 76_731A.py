#coding=utf-8

s='a'+raw_input()
ans=0
for i in range(1,len(s)):
	temp=abs(ord(s[i])-ord(s[i-1]))
	if temp>13:
		temp=26-temp
	ans+=temp
print ans