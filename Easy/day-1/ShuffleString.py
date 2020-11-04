s = ['c','o','d','e','l','e','e','t']
indices = [4,5,6,7,0,2,1,3]
res = [0 for i in range(len(indices))]

for i in range(len(indices)):
    res[indices[i]] = s[i]

print(res)