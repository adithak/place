n12=int(input())
l1=list(map(int,input().split()))
p=[]
for i1 in range(n12-1):
	for j1 in range(i1,n12):
		c1=l1[i1:j1+1]
		p1.append(sum(c1))
print(max(p))
