# def print_2_add_2():
#     result = 2 + 2
#     print(result)
#
# print_2_add_2()

# def hello_world():
#     print('hello word')
# hello_world()

# def pow_func(base, n=2):
#     print(base ** n)
# pow_func(3)
# pow_func(5 , 3)

# def reverse_stair(n):
#     for i in range(n, 0, -1):
#         print('*'* i)
#
# reverse_stair(5)

# функцию, которая будет возвращать количество делителей числа а.
# def get_multipliers(a):
#    count = 0
#    for n in range(1, a + 1):
#        if a % n == 0:
#            count += 1
#
#    return count
#
# get_multipliers(5)

# def check_palindrome(str_):
#    str_ = str_.lower()
#    str_ = str_.replace(" ", "")
#    if str_ == str_[::-1]:
#        return True
#    else:
#        return False
#
# check_palindrome("test")
# check_palindrome("Кит на море не романтик")


# def my_func():
#     a = 5
#     b = 10
#     print(a + b)
# my_func()

# def my_fuck(a, b):
#     print(a + b)
# my_fuck(5, 10)

# def my_fuck(a, b):
#     result = a + b
#     return result
#
# c = my_fuck(5, 10)
# print(c)

# PI = 3.14 # глобальная переменная

# def area_circle(r):
#     global PI
#     print('число выведенное из локальной области видимости до изменения', PI)
#     PI = 3.1415 # изменение глобальной переменной
#     print('число выведенное из локальной области видимости после изменения', PI)
#     return PI * (r ** 2)
#
# print('число выведенное из глобальной области видимости до вызова функции', PI)
# print(area_circle(10))
# print('число выведенное из глобальной области видимости после вызова функции', PI)

# def adder(*nums):
#     sum_ = 0
#     for n in nums:
#         sum_ += n
#
#     return sum_
#
# print(adder())
# print(adder(1))
# print(adder(1,2))
# print(adder(1,2,3))


# def adder(*nums):
#     a = 1
#     for n in nums:
#         a *= n
#
#     return a
#
# print(adder())
# print(adder(1))
# print(adder(1,2))
# print(adder(1,2,3))

# def rec_sum(n):
#    if n == 1:  # терминальный случай
#        return 1
#    return n + rec_sum(n - 1)
#
# rec_sum(10)

# def count(start=1, step=1):
#     counter = start
#     while true:
#         yield counter
#         counter += step


# Создайте генератор цикла, то есть в функцию на входе будет передаваться массив, например,
# [1, 2, 3], генератор будет вечно работать возвращая 1 2 3 1 2 3… и так далее.
# def repeat_list(list_):
#    list_values = list_.copy()
#    while True:
#        value = list_values.pop(0)
#        list_values.append(value)
#        yield value
#
# for i in repeat_list([1, 2, 3]):
#    print(i)

# def linear_solve(a, b):
#     if a:
#         return b/a
#     elif not a and not b:
#         return "нет корней"
#     else:
#         return "нет корней"
# print(linear_solve(0, 1))

# def D(a,b,c):
#     return b ** 2 - 4 * a * c
# def quadratic_solve(a,b,c):
#     if D(a,b,c) < 0:
#         return "Нет вещественных корней"
#     elif D(a,b,c) == 0:
#         return -b/(2*a)
#     else:
#         return (-b - D ** 0.5) / (2 * a), (-b + D**0.5)/(2*a)

# iter_obj = iter("Hello!")
#
# print(next(iter_obj))
# print(next(iter_obj))
# print(next(iter_obj))
# print(next(iter_obj))
# print(next(iter_obj))
# print(next(iter_obj))
# print(next(iter_obj))

# синтаксис функции
# def имя_функции(аргементы):
#     инструкции
#     return список выражений
# имя_функции()

# def greet(name):
#     print('привет ' + name + '.Доброе утро!')
# greet('Джон')


# возвращаемое значение - return

# def absolute_value(num):
#     if num >= 0:
#         return num
#     else:
#         return -num
# print(absolute_value(2))
# print(absolute_value(-4))

# Область видимости (scope) и время жизни переменной

# def my_func():
#     х = 10
#     print('значение внутри функции', х)
# х = 20
# my_func()
# print('значение вне функции', х)

# аргументы функции
# фиксированное кол-во аргументов
# def greet(name, age):
#     print('привет ' + name + '.Доброе утро!' + 'мне ' + age + 'лет')
# greet('Джон', '23')

# аргументы по умолчанию
# def greet(name, age ='23'):
#     print('привет ' + name + '.Доброе утро!' + 'мне ' + age + 'лет')
# greet('Джон')

# именованный аргумент
# def greet(name, age):
#     print('привет ' + name + '.Доброе утро!' + 'мне ' + age + 'лет')
# greet(name = 'Джон', age ='23')
# greet(age ='53',name = 'Том')

# Произольный список аргументов
# * - передает значения всех параметов
# def greet(*names):
#     for name in names:
#         print('hello', name)
# greet('kate','mark','nik')

# Глобальные переманные
# х = 'глобальная переменная'
# def foo():
#     x = x * 2
#     print(x)
# foo()

# Локальные переменные

# def foo():
# y = 'Локальные переменные'
#     print(y)
# foo()


# x = 'global variable'
# def foo():
#     global x
#     y = 'local variable'
#     x = x * 2
#     print(x)
#     print(y)
# foo()

# x = 5
# def foo():
#     x = 10
#     print('local variable:', x)
# foo()
# print('global variable x:', x)

# нелокальные переменные nonlocal

# def outer():
#     x = 'локальная переменная'
#     def inner():
#         nonlocal x
#         x = 'нелокальная переменная'
#         print('вложенная функция:', х)
#     inner()
#     print('внешная функция:', x)
# outer()


# Замыкание это вложенная функция, которая ссылается на одну или более переменных из обеляющей области видимости.

# def say():
#     greeting = 'привет' #/
#     def display():
#         print(greeting) #/ Эта часть кода называется замыканием.
#     display()
# say()

# Вернуть функцию из функции


# декораторы
# def net_price(price, tax):
#     return price * (1 + tax)
# # $100
# def currency(fn):
#     def wrapper(*args,**kwargs):
#         result = fn(*args,**kwargs)
#         return f'${result}'
#     return wrapper
# net_price = currency(net_price)
# print(net_price(100, 0.05))

# Декоратор синтаксис
# функция = декоратор (функция)

# @декоратор
#    def функция():
#    тело функции

#
# def currency(fn):
#     def wrapper(*args, **kwargs):
#         result = fn(*args, **kwargs)
#         return f'${result}'
#     return wrapper
#
# @currency
# def net_price(price, tax):
#     return price * (1 + tax)
# # $100

#  lambda аргументы: выражения
# double = lambda x: x * 2
# print(double(5))

# filter(), map()

# my_list = [2, 5, 56, 74, 7, 8]
# new_list = list(map(lambda x: x * 2, my_list))
# print(new_list)

