a=[1,2,3,8,7,5,10,9]
b=[]
i=0
while i<len(a):
    if a[i]>5:
        b.append(a[i])
        i+=1
print(b)