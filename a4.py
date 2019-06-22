a=input()
v=0
for i in range(len(a)):
    if a[:i]==a[i+1:]:
        v=0
        break
    else:
        v=1
if v==0:
    print("YES")
else:
print("NO")
