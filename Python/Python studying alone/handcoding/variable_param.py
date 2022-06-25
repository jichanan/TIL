def print_n_times(n, *values):
    for i in range(n):
        for value in values:
            print(value)

print_n_times(3,"하이","즐거운","파이썬")