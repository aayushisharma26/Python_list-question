a=[[0,2,6],[1,2,7]]
i=0
while i<len(a):
    m=a[i]
    j=0
    sum=0
    while j<len(a[i]):
        n=a[i][j]
        sum=sum+n
        j=j+1
    print(sum)
    i=i+1

