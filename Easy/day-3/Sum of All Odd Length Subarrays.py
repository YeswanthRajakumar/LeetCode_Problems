arr = [10,11,12]
total = 0
for s in range(0,len(arr)):
    for e in range(1,len(arr)+1):
        sub_arr =[]
        if (s+e)%2 !=0:
            for i in range(s,e):
                sub_arr.append(arr[i])
            if len(sub_arr)%2 != 0:
                total += sum(sub_arr)
        
print(total)