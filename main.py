# name= 'Ivan'
# # Camel case
# userName = 'Tom'
# user_name = 'Kate'
import math

# Date Types
# типизация: динамическая и статич

#Числа
# целые и дробные (цисла с плавающей точкой)
# a = 5.5 + 5
# print(a)
#
# a = 5 / 2
#
# b = 5 // 2
# b_1 = 5*2
# b_2 = 5**2
# #целочисленное деление, это не оругление!
# print(a)
# print(b)

# % - статок от деления
# a = 8 % 3
# print(a)

# False/True
# a = 8 == 3
# print(a)


# Округление 2 знака после запятой
# a = round(10/3.0, 2)
# a = 10/3.0
# print(a)

# функция преобразования - int() целочисленное преобразование
# a = 10/3.0
# b = int (a)
# print(b)

# float() - вещественное, дробное преобразование

# Строка

# name = 'Ivan Ivanovich'
# по индексу
# print(name[1])
# print(name[-1])

# срез стороки [start:stop:step]
# print(name[1:6:2])

# concat (объединение 2 строк в одну - пенконтинация строк)
# name = 'Ivan '
# fullname = 'Ivanovich'
# res = name + fullname +' hello!'
# print(res)


# Методы строк
# string = 'Hello'
# # нижний регистр
# res = string.lower()
# print(res)
# # верхний регистр
# res = string.upper()
# print(res)


# name = input('Введите ваше имя ')
# name_start = name[0].upper()
# name_end = name[1:].lower()
# res = name_start + name_end
# print(res)

# проверка на входжение
# in и not in
# a = 'hello'
# b = 'hello world'
# print (a in b)


# len() длинна строки
# split() разбивает строки по разделителю
# jone() собирает строку из списка
# string = 'hello'
# print(len(string)) #5

# \n переход на новую строку
# print('hello\nword')

# Форматирование
# format
# порядок с позиционированныйми аргументами
# string = "{1},{0},{2}".format('Петя', 'Ваня', 'Катя')
# print(string)

# порядок по ключевым словам
# string = "{s},{b},{j}".format(j='Петя', b='Ваня', s='Катя')
# print(string)

# f - строки. передача переменной
# a = 'Ivan'
# res = f'{a}, hello'
# print(res)

# List - [] список
# numbers = [1,2,3,4, 'hello',True]
# numbers_1 = list()
# print(numbers)
# print(numbers[-1])


# Methods List - методы списка
# append(item) добавляет элемент в список

# people = ['Ivan','Tom', 'Kate']
# new_person = people.append('Bob')
# # insert(item) - добавляет элемент в список по индексу
# print(people.insert(1, 'Bill'))
# print(people)
# # remove(item)
# print(people.remove('Bill'))
# print(people)

# count() кол-во элементов в списке
# people = ['Иван','Алексей','Марк','Марк']
# people_count = people.count('Марк')
# print(people_count)
#
# # сортировка
# a = [4,3,2,1]
# print(sorted(a))

# Вложенный список
# people = [
#     ['Ivan',29],
#     ['Kate',27],
#     ['Bob',32]
# ]
# print(people[0][1])
# #29
#
# # Tuple () Кортеж
#
# tom = ('Tom','Bob')
# users = {1:'Tom', 2:'Bob', 3:'Kate'}

# Словари {keys:values}

# users = {1:'Tom', 2:'Bob', 3:'Kate'}
# users_1 = users.get(3)
# print(users_1 )

# items()
# users = {1:'Tom', 2:'Bob', 3:'Kate'}
# for key, value in users.items():
#     print(key, value)

# множества set()
# users = {'Tom', 'Bob', 'Kate'}
# users.add('Sam')
# print(users)

# num = int(input('введите число'))
# if num % 2 == 0:
#     print('четное число', num)
# else:
#     print('не четное число')

# letter = input('ввести текст ')
# if letter == 'a' or letter == 'e' or letter == 'o' or letter == 'u':
#     print('гласная буква')
# elif letter == 'x':
#     print('гласная и согласная')
# else:
#     print('согласная')

# num = int(input('Ввести числа')) # Выводить числа пока не встретитс 0, так как число не должно быть  !=.
# # в конце сортировка
# data = []
# while num != 0:
#     data.append(num)
#     num = int(input())
# data.sort()
# print(data)

# print(list(str(123456789)))
# print(list(map(int, ['1', '2', '3', '4', '5', '6', '7', '8', '9'])))
# list_digit = list(map(int, list(str(123456789))))
# print(3 and 7 in list_digit)

# try:
#     i = int(input('Введите число:\t'))
# except ValueError as e:
#     print('Вы ввели неправильное число')
# else:
#     print(f'Вы ввели {i}')
# finally:
#     print('Выход из программы')

# num = int(input('введите целое число '))
# if num %2 == 0:
#     print(num, 'четное число')
# else:
#     print('нечетное число', num)

# S = 0  # заводим переменную-счетчик, в которой мы будем считать сумму
# N = 5

# заводим цикл for, в котором мы будем проходить по всем числам от одного до N
# for i in range(1, N + 1):  # равносильно выражению for i in [1, 2, 3, ... , N -1, N]:
#     print("Значение суммы на предыдущем шаге: ", S)
#     print("Текущее число: ", i)
#     S = S + i  # cуммируем текущее число i и перезаписываем значение суммы
#     print("Значение суммы после сложения: ", S)
#     print("---")
# print("Конец цикла")
# print()
# print("Ответ: сумма равна = ", S)

# P = 1  # заводим переменную-счетчик, в которой мы будем считать произведение
# N = 5
#
# # запишите цикл for для подсчета произведения
# for i in range(1, N+1):
#     print("Значение суммы на предыдущем шаге: ", P)
#     print("Текущее число: ", i)
#     P *= i
#     print("Значение суммы после сложения: ", P)
#     print("---")
# print("Конец цикла")
# print()
# print("Ответ: сумма равна = ", P)
#
# print(P)

# S = 0  # заводим переменную-счетчик, в которой мы будем считать сумму
# n = 1  # текущее натуральное число

# заводим цикл while, который будет работать, пока сумма не превысит 500
# while S < 500:  # делай пока ...
#     S += n  # увеличиваем сумму, равносильно S = S + n
#     n += 1  # так как сумма ещё не достигла нужного значения, то увеличиваем переменную-счетчик
#     print("Ещё считаю ...")
#
# print("Сумма равна: ", S)
# print("Количество чисел: ", n)
#
# random_matrix = [
#     [9, 2, 1],
#     [2, 5, 3],
#     [4, 8, 5]
# ]
#
# min_value_rows = []  # здесь будут храниться минимальные значения для каждой строки
# min_index_rows = []  # здесь будут храниться индексы минимальных значений для каждой строки
# max_value_rows = []  # здесь будут храниться максимальные значения для каждой строки
# max_index_rows = []  # здесь будут храниться индексы максимальных значений для каждой строки
#
# for row in random_matrix:  # здесь мы целиком берем каждую сроку
#     min_index = 0  # в качестве минимального значения возьмем первый элемент строки
#     max_index = 0
#     min_value = row[min_index]  # начальное минимальное значение для каждой строки будет новое
#     max_value = row[max_index]  # для максимального значения тоже самое
#     for index_col in range(len(row)):
#         if row[index_col] < min_value:
#             min_value = row[index_col]
#             min_index = index_col
#         if row[index_col] > max_value:
#             max_value = row[index_col]
#             max_index = index_col
#     min_value_rows.append(min_value)
#     min_index_rows.append(min_index)
#     max_value_rows.append(max_value)
#     max_index_rows.append(max_index)
#
# print(min_value_rows)
# print(min_index_rows)
# print(max_value_rows)
# print(max_index_rows)

# x = int(input('введите год'))
# if x % 400 == 0 or x % 4 == 0 and x != 0:
#     print('весокосный год')
# else:
#     print('не весокосный')


# x = int(input('введите год'))
# print((x % 400 == 0) or (( x % 4 == 0) and ( x % 100 != 0)))

# def get_wind_class(speed): #объявление функции
#     if 1 <= speed <= 4: #только аргумент
#         return "weak [1]"
#     elif 5 <= speed <= 10:
#         return "moderate [2]"
#     elif 11 <= speed <= 18:
#         return "strong [3]"
#     elif speed >= 19:
#         return "hurricane [4]"
# print(get_wind_class(5))


