num =14
count= 0
while True :
    if num == 0:
        break

    if num %2==0:
        num =num//2
        count+=1

    else:
        num-=1
        count+=1

print(count)