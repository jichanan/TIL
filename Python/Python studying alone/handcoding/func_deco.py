def test(func):
    def wrapper():
        print("인사가 시작되었습니다.")
        func()
        print("인사가 종료되었습니다.")
    return wrapper

@test
def hello():
    print("hello")

hello()

