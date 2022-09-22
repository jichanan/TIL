def mul(*values):
    변수 = 1
    for value in values:
        변수 *= value
    return 변수


print(mul(5,7,9,10))