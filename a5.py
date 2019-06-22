z1=list(input())
ca=0
for i in range(len(z1)):
    li=z1.copy()
    li.remove(li[i])
    li1=li[::-1]
    if li==li1:
        ca=1
        break
if ca==1:
    print("YES")
else:
print("NO")
