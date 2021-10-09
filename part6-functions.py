""" ========= """
"""  Функции  """
""" ========= """


# Определение пользовательской функции
def func():
    print("Hello, world!")


# Можно задавать аргументы у функций! А также они могут возвращать некоторое значение
def area(side1, side2):
    return side1 * side2


def peri(side1, side2):
    return 2*side1 + 2*side2


# Значение аргумента по умолчанию, как альтернативный способ перегрузки функций
#                                  (использования функции с одним именем, но разным телом)
def area_peri(side1, side2=None):
    if side2 is None:
        side2 = side1
    return area(side1, side2), peri(side1, side2)


# sq1 = 4
# print(sq1, *area_peri(sq1))   # * - распаковать коллекцию в этом месте
#
# sq2 = 5
# print(sq2, *area_peri(sq2))
#
# rect_x = 3
# rect_y = 4
# print(rect_x, rect_y, *area_peri(rect_x, rect_y))     # Функция работает и с одним и с двумя аргументами!


""" Рекурсивная функция """
# 0 1 1 2 3 5 8 13
def fib(x):
    # Не забывайте задавать начальное значение!
    # Иначе рекурсивная функция будет бесконечно вызываться (1000 - лимит глубины рекурсии в Python)
    if x == 0:
        return 0
    if x == 1:
        return 1
    if x == 2:
        return 1
    return fib(x - 2) + fib(x - 1)


# my_x = 7
# print("fib", my_x, "=", fib(my_x))


""" Коллекции передаваемые в качестве аргумента функции передаются по ссылке """
# def mutator(lst):
#     lst.pop()
#     lst.append(123)


# abc = [42, 69, 228, 420]
# mutator(abc)
# print(abc)


""" Функции могут возвращать различные типы. 
    Но если не все ветки что-либо возвращают - тогда автоматически используется None """
def strange_func(num: int):
    if num > 0:
        return "Yay!"
    if num < 0:
        return 42


# print(strange_func(69))
# print(strange_func(-15))
# print(strange_func(0))
