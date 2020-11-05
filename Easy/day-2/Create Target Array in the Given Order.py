nums = [0,1,2,3,4]
index = [0,1,2,2,1]

target =[]
l = len(index)
for i in range(l):
    # print(nums[i],index[i])
    target.insert(index[i],nums[i]) 

print(target)


