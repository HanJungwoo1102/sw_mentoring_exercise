input_num_1, input_num_2 = list(map(int, input().split()))

for i in range(min(input_num_1, input_num_2), 0, -1):
    if input_num_1 % i == 0 and input_num_2 % i == 0:
        print(i)
        break
