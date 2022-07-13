def print_factorial_value(num):
    result = 1
    for i in range(1, num + 1):
        result *= i
    print(result)

input_num = int(input())
print_factorial_value(input_num)