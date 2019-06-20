m,t=map(int,input().split())
a=list(map(int,input().split()))
x=[]
e=[]
r=[]
s=0
for i in range(0,m):
    if a[i]!=k and abs(a[i]-t):
        w.append(abs(a[i]-t))
        e.append(a.index(a[i]))
for i in range(0,3):
    s=w.index(min(x))
    r.append(a[e[s]])
    w.pop(x.index(min(x)))
    e.pop(s)
print(*r)
