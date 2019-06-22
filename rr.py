t12,s=map(eval,input().split())
a=[]
for i in range(t12):
  a.append(list(map(eval,input().split())))
pos=[]
out=[]
temp_out=[]
t12=[]
i=0
j=0
out.append(a[i][j])
pos.append([i,j])
while [t12-1,s-1] not in pos:
  i=0
  for x in pos:
    if x[0]+1<t1 and x[1]+1<s:
      temp_out.append(a[x[0]+1][x[1]]+out[i])
      temp_out.append(a[x[0]][x[1]+1]+out[i])
      t1.append([x[0]+1,x[1]])
      t1.append([x[0],x[1]+1])
    elif x[0]+1<t12:
      temp_out.append(a[x[0]+1][x[1]]+out[i])
      t1.append([x[0]+1,x[1]])
    elif x[1]+1<s:
      temp_out.append(a[x[0]][x[1]+1]+out[i])
      t1.append([x[0],x[1]+1])
    i+=1
  pos=t1
  t1=[]
  out=temp_out
  temp_out=[]
print(max(out))
