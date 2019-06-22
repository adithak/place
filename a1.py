n12=int(input())
l12=list(map(int,input().split()))
a12=l12
c12=[]
while(len(a1)!=1):
	for i12 in range(len(a12)):
		if i12%2!=0:
			c12.append(a1[i12])
	a12=c12
	c12=[]
print(l12.index(a12[0]))
