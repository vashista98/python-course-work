n=int(input('enter the num:'))
a=0
b=1
print(a,b,end=' ')
for i in range(10):
    c=a+b
    a=b
    b=c
    print(c,end=' ')