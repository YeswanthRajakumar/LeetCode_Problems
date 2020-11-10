def distance(a,b):
    return max(abs(a[0]-b[0]),abs(a[1] -b[1]))

points = [[1,1],[3,4],[-1,0]]
d=0
for i in range(len(points)-1): # 0 1 ,1 2
    d +=distance(points[i],points[i+1])

print(d)