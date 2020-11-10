'''
1. change input to string
2. iterate through string
3.change 6 to 9 (or)  9 to 6
4. store to max(output,curr val)
5 finally,return the output
''' 
num = 9669
output = num
str_num = str(num)

for i in range(len(str_num)):  #'9 6 6 9 '
    check_num = list(str(num))
    if check_num[i] == '6':
        check_num[i] = '9'
        # print(i,check_num)
    else:
        check_num[i] = '6'
        # print(i,check_num)
    
    curr_val = int(''.join(check_num))
    if curr_val > output:
        output = curr_val

print(output)