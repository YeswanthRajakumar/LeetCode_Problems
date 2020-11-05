n = 4421
l = list(str(n))
sum_of_digits = 0
product_of_digits = 1

for i in l:
    sum_of_digits+=int(i)
    product_of_digits*=int(i)

print(product_of_digits ,sum_of_digits)