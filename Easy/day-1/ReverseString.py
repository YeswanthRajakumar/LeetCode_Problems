a = ["H","a","n","n","a","h"]
j = len(a)-1
i = 0
while i<j:
    print(i,j)
    temp = a[i]
    a[i] = a[j]
    a[j] = temp
    i+=1
    j-=1

print(a)