u= int(input())
f= list(map(int,input().split()))
for i in range(0,v-2):
  for j in range(i+1,u-1):
    for k in range(j+1,u):
      if f[i]+f[j] == f[k]:
        print(f[i],f[j],f[k])
