# 함수를 선언합니다.
def fibonacci(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
# 함수를 호출합니다.
print(fibonacci(6))