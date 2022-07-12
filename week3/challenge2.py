decimal_num = int(input())

result = ''

binary_num_str = bin(decimal_num)

for i in range(2, len(binary_num_str)):
    print(binary_num_str[i], end=' ' if (len(binary_num_str) - i - 1) % 4 == 0 else '')
