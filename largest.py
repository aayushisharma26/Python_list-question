a=[2,312,123,3,12,23,12,12]
largest=a[0]
i=0
while i<len(a):
    if a[i]>largest:
        largest=a[i]
        i=i+1
print(largest)