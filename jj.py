y=int(input())
t=list(map(int,input().split()))
w=[]
for i in range(y):
    ls=l[i:]
    m=max(ls)
    if(t[i] == m):
        w.append(t[i])
print(*w)
print(max(w))
