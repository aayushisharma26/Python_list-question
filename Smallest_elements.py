a=[2,312,123,3,12,23,12,12]
smallest=a[1]
i=0
while i<len(a):
    if a[i]<smallest:
        smallest=a[i]
    i=i+1
print(smallest)        
