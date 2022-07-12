input_size = int(input())

for star_length in range(1, input_size + 1):
    if star_length % 2 == 0:
        print('')
    else:
        print('*' * star_length)
