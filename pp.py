mq,k=map(int,input().split())
s=[]
l1=[]
for i in range(mq):
    l=[int(s) for s in input().split()]
    s.append(l)
    if 0 in l:
        m=l.index(0)
        l1.append(m)
for i in range(len(s)):
    if 0 in s[i]:
        for j in range(k):
            s[i][j]=0
for i in l1:
    for j in range(mq):
        s[j][i]=0
for i in s:
print(*i)
