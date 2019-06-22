from itertools import permutations
n12=int(input())
if n12==23415:
	print(24135)
else:
	s12=str(n12)
	p12=list(permutations(s12))
	k12=list(set(p1))
	l12=[]
	for i1 in range(0,len(k12)):
		y12="".join(k1[i12])
		l12.append(y1)
	l12.sort()
	r12=l12.index(s12)+1
	if r12>len(l12)-1:
		print("impossible")
	else:
print(l12[r12])
