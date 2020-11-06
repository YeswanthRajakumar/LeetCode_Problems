arr = [3,0,1,1,9,7]
a = 7
b = 2
c = 3
count=0

# 0 <= i < j < k < arr.length
# |arr[i] - arr[j]| <= a
# |arr[j] - arr[k]| <= b
# |arr[i] - arr[k]| <= c

for i in range(0,len(arr)-2):
    for j in range(i,len(arr)-1):
        for k in range(j,len(arr)):
            if 0<=i < j < k:
                if abs(arr[i] - arr[j]) <=a and abs(arr[j] - arr[k]) <=b and abs(arr[i] - arr[k]) <=c:
                    count+=1

print(count)