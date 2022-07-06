def call_10_times(func):
    for i in range(10):
        func(i)

call_10_times(lambda number: print("안녕", number))