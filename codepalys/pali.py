n=int(input('enter the range:'))
temp=n
if str(n)==str(n)[::-1]:
    print('PD')
else:
    print('NPD')

rev=0
while n>0:
    rev=rev*10+(n%10)
    n=n//10
    print(rev)
if rev==temp:
    print('PD')
else:
    print('NPD')        
