n=int(input('enter the num:'))
a=0
b=1
if n==0:
    print('none')
elif n==1:
    print(a)
elif n>=2:
    print(a,b,sep='\n')
    for i in range(n-2):
        c=a+b
        a=b
        b=c
        print(c)        
