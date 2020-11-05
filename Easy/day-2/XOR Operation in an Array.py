n = 5
start = 0
nums = [start + 2*i for i in range(5)]
xor = 0
for i in nums:
    xor = xor^i
print(xor)