n = [19, 17, 12, 17, 17, 18, 10, 17, 14, 12, 19, 17, 12, 13, 11]
i=[]
a=0
while a< len(n):
    if n[a] not in i:
        i.append(n[a])
    a+=1
print(i)