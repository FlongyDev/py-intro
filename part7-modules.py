""" ======== """
"""  Модули  """
""" ======== """
# import part7
# print(part7.fib(7))   # Обращение к функции модуля: имя_модуля.функция()

""" Импорт конкретных частей модуля и переименование импортов """
# from part7 import func as hello, fib


""" Импорт конкретных функций из модулей стандартной библиотеки """
from math import sqrt
from random import randint


""" Для разрешения коллизий в названиях функций можно переименовать импорты через `as` """
def func():
    from math import sin    # Локальный для функции импорт
    print("Different func", sin(randint(0, 5)))


# func()
# hello()
# print(fib(10))

""" Использование импортированных функций подобно вызову локальных функций """
# r = randint(10, 20)
# s = sqrt(r)
# print(r, s)


""" Можно скачивать пользовательские модули! """
# # !pip install numpy - команда для установки стороннего модуля (пишется в терминале, нужен установленный pip)
# import numpy as np    # Импортируются точно также - после установки они автоматически доступны в любой вашей программе
# arr = np.random.random((5, 5))
# print(arr)
