q,w=map(int,input().split())
for i in range(q+1,w):
    e=0
    d=i
    while(d>0):
        c=d%10
        d=d//10
        f=c**3
        e=e+f
    if(i==e):
print(e,end=' ')
