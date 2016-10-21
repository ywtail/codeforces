#coding=utf-8

letters=["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
a=letters.index(raw_input())
b=letters.index(raw_input())
if a==b or (a+2)%7==b or (a+3)%7==b:
	print "YES"
else:
	print "NO"