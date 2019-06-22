m,q=map(int,input().split())
l=[]

for i in range(m):
    l.append(list(map(int,input().split())))

r=[]

for i in l[0]:
    for j in range(1,m):
        if i not in l[j]:
            break
    else:
        r.append(i)

r.sort()
q=len(r)-1    
for i in range(q):
    print(r[i],end=" ")
print(r[q])
