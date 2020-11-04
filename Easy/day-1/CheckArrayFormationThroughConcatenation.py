arr = [91,4,64,78]
pieces =  [[78],[4,64],[91]]
res =[]
mp ={}
for p in pieces:
    mp[p[0]] = p

for i in arr:
    res +=mp.get(i,[])

print(res)
