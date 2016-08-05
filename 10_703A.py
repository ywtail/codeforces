n=int(raw_input())
game=[]
mishka=0
chris=0
for i in xrange(0,n):
	game.append(raw_input().split(" "))
	game[i]=map(int,game[i])
	if game[i][0]>game[i][1]:
		mishka+=1
	elif game[i][0]<game[i][1]:
		chris+=1
	else:
		continue

if mishka>chris:
	print "Mishka"
elif mishka<chris:
	print "Chris"
else:
	print "Friendship is magic!^^"