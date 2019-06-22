nn=int(input())-1
ll=list(map(int,input().split()))
ll=l[::-1]
for i in range(nn):
    print(ll[i],end='->')
print(ll[nn])
