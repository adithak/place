aa,bb=map(int,input().split())
l=[int(x) for x in input().split()]
cd=0
for i in range(0,aa):
    for j in range(i+1,aa):
        s=l[i]+l[j]
        if s==b:
            cd+=1
if cd>=1:
    print("YES")
else:
print("NO")
