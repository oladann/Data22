def print_something(print_string):
    print(print_string)


def greeting(name: str) -> str:
    print("Hello, my name is "+name)


def addition(int1, int2=2):
    x = int1+int2
    y = x*2
    return y


def multi_args(*multiargs):
    print(type(multiargs))
    for arg in multiargs:
        print(arg)


def division(denom: int, num: int) -> float:
    return denom / num


print(division(3, 2))


def subtraction(int1: int=5, int2 =2) -> int:
    return int1 - int2

print(subtraction(10))