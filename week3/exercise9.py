input_size = int(input())

if input_size % 2 != 0:
    for star_length in range(1, input_size, 2):
        print(' ' * ((input_size - star_length) // 2) + '*' * star_length)
    print('*' * input_size)
    for star_length in range(input_size - 2, 0, -2):
        print(' ' * ((input_size - star_length) // 2) + '*' * star_length)
else:
    print('ERROR!')
