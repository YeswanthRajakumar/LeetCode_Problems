s = "LLLLRRRR"
count = 0
total = 0
for i in s:
    if i == 'L':
        count+=1
    else:
        count-=1
    if count == 0:
        total+=1
print(total)