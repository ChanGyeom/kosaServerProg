######################################33
# 파이썬 함수 사용의 예


# 파라미터도 없고 리턴값도 없음
def hello():
    print("Hello World")


hello()


# 파라미터와 리턴값이 있음
def add(x, y):
    print(x)
    print(y)
    return x + y


val_x = 1
val_y = 2
val_sum = add(val_x, val_y)
print(val_sum)


# 호출할 때 매개변수(인자)의 이름을 지정할 수 있음
print(add(y = val_y, x = val_x))


# default value (매개변수에 초기값)을 이용하는 함수
def add(x, y = 10):
    print(x)
    print(y)
    return x + y


print(add(1, 2))
print(add(1))


# 매개변수의 개수가 가변적인 함수
def sum(*values):
    result = 0
    for one in values:
        result = result + one
    return result


result = sum(1, 2, 3)
print(result)


# 여러개의 값을 반환하는 함수
def calc(a, b):
    return a + b, a - b


result = calc(1,3)
print(result)


x, y = calc(1,3)
print(x)
print(y)