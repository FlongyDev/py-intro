""" ====================================== """
""" Модули: модуль с функциями для импорта """
""" ====================================== """


def func():
    print("Hello, world!")


def fib(x):
    if x == 0:
        return 0
    if x == 1:
        return 1
    if x == 2:
        return 1
    return fib(x - 2) + fib(x - 1)


""" Если файл импортируется, то нижний код не выполняется! """
if __name__ == "__main__":
    print("Hello from the part7 module!")
