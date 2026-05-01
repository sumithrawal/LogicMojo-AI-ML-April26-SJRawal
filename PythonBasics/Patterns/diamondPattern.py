n = int(input("Enter the Diamond Size: "))
for i in range(1,n+1):
    print(' ' * (n-i)+'*' *i+ '*'* (i-1))
for i in range(n-1,-1,-1):
    print(' ' * (n-i)+'*' *i+ '*'* (i-1))