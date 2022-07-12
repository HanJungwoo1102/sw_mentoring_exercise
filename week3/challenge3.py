# 1 0 8 2 4 6 5 3 7 9

input_nums = list(map(int, input().split()))

for start_idx in range(0, len(input_nums) - 1):
    for i in range(start_idx, len(input_nums) - 1):
        if input_nums[i] > input_nums[i + 1]:
            temp = input_nums[i + 1]
            input_nums[i + 1] = input_nums[i]
            input_nums[i] = temp

for num in input_nums: print(num, end=' ')
