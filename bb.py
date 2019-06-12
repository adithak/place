q,w = map(int,input().split())
a1=list(map(int,input().split()))
a2=list(map(int,input().split()))
if (all(x in a1 for x in a2)):
	print("YES",end="")
else :
	print("NO",end="")
