# O(N2) solution

def minCount(arr,n):
    count=0
    for j in arr:
        if j<n:
            count+=1
    return count 

nums = [8,1,2,2,3]
count_arr =[]

for i in nums:
    c = minCount(nums,i)
    count_arr.append(c)        

print(count_arr)

