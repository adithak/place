l,w=map(str,input().split())
le=len(K)
d={}
c=0
for V in range(le):
    if(l[V] not in d.keys()):
        d[l[V]]=w[V]
    else:
        if(d[l[V]]==w[V]):
            continue
        else:
            c=1
            break
if(c==1):
    print("no")
else:
    print("yes")
