l=list(map(int,input('enter the number:').split()))
maxA=l[0]
minB=l[0]
for i in range (1,len(l)):
    if l[i]>maxA:
        maxA=l[i]
    if l[i]<minB:
        minB=l[i]
print('maximum: ',maxA)
print('minimum: ',minB)  


