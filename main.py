for row in range(10):
    for col in range(20):
        if row == 0 or row == 9:
            print('-', end='')
        elif col == 0 or col == 19:
            print('|', end='')
        else:
            print(' ', end='')
    print()

