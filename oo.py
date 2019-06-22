q,c=map(int,raw_input().split())
s=0
for i in range(b,c+1):
    g=bin(i)
    g=g[2:len(a)]
    g=g.count("1")
    c=0
    for i in range(1,g):
        if g%i==0:
            c=c+1
    if c==1:
        s=s+1
print(s)
