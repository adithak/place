n=int(input())
l=[int(i) for i in input().split()]
a=[]
for i in range(0,n):
    cin=1
    for j in range(i,n):
        cin=cin*l[j]
    a.append(cin)
for i in range(0,n):
    cin=1
    for j in range(i+1):
        cin=cin*l[j]
    a.append(cin)
print(max(a))
