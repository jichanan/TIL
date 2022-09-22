# 함수를 선언합니다.
def factorial(n):
    # n이 0이라면 1을 리턴
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))