""" ======= """
"""  Циклы  """
""" ======= """

""" === Цикл пока - while === """
""" Цикл со счетчиком на цикле while """
# a = 10
# while a > 0:      # Пока выполняется условие - выполнять шаг цикла
#     print(a)
#     a -= 1        # Не забывайте изменять переменную в условии, иначе ваш цикл никогда не завершится!

""" === Цикл для-каждого - for === """
""" Цикл со счетчиком на цикле for """
# for a in range(10):
#     print(a)

""" В каждом шаге цикла в переменную i помещается следующее значение из коллекции """
# l = [10, 20, 30, 40]
# for i in l:
#     print(i)

""" Цикл for может использоваться с любым итерируемым объектом (т.е. с коллекциями, как строки, тоже) """
# st = "Hello! World!"
# for c in st:
#     if c != '!':  # В цикле можно вкладывать if блоки или другие циклы
#         print(c, end="")
# print()


""" Управлением ходом цикла: break и continue """
# st = "Hello! World!"
# for c in st:
#     if c == '!':
#         break             # break завершает выполнение цикла
#     print(c, end="")
# print()
#
# first = st.split('!', 1)[0]
# print(first)

# st = "Hello! World!"
# for c in st:
#     if c == '!':
#         print("?", end="")
#         continue          # continue завершает выполнение текущего шага цикла и переводит к следующему
#     print(c, end="")
# print()

""" Определить является ли число простым (самый очевидный способ) """
n = 17
for i in range(2, n):
    if n % i == 0:
        print(n, "делится на", i, "=> не является простым")
        break
else:   # У циклов тоже есть else ветки - они вызываются при обычном завершении цикла (т.е. непрерванном через break)
    print(n, "является простым числом")
