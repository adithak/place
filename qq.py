n=int(input())
l1=list(map(int,input().split()))
em=1
l=[]
for i in l1:
  em=em*i
for i in l1:
  l.append(em//i)
print(*l)
