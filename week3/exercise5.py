input_num = int(input())

divisors = []

for i in range(1, input_num + 1):
    if input_num % i == 0:
        print(i, end=' ')