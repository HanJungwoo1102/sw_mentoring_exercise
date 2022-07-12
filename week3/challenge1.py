input_num = int(input())

count = 0

for num in range(1, input_num + 1):
    num_str = str(num)
    for j in num_str:
        if j == '3' or j == '6' or j == '9': count += 1

print(count)
