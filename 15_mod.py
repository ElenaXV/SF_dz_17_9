# myfile = open('helllo.txt','r')
# file = myfile.read()
# print(file)
# myfile.close()

# работа с файлами и исключениями
# try:
#     somefile = open('hello1.txt','w')
#     try:
#         somefile.write('hello word')
#     except Exception as e:
#         print(e)
#     finally:
#         somefile.close()
# except Exception as ex:
#     print(ex)

# with
# with open(file,mode) as file_obj:
#     инструкции

# with open('hello1.txt','w') as somefile:
#     somefile.write('goodbay world')

# чтение файлов
# r
# readline() считывает одну строку из файла
# read() считывает все содержимое в одну строку
# readlines() считывает все строки файла в список


# f = open("test.txt",'r')
# file_data = f.read()
# line_1 = f.readline()
# line_2 = f.readline(2)
# lines = f.readlines()
# print(line_1)
# print(line_2)
# print(lines)
# f.close() // при такой рабое с функцией нужно всегда закрывать файл с помощью функции close.

# функция with
# with open("test.txt",'r') as f:
#     line_1 = f.readline()
#     line_2 = f.readline(2)
#     lines = f.readlines()
#     print(line_1)
#     print(line_2)
#     print(lines)

# f_try = open("test.txt",'r')
# try:
#     print(f_try.read())
# finally:
#     f_try.close()


# f_try = open("test",'r')
# try:
#     lines = f_try.readlines()
#     for line and lines:
#     print(f'Helen {line})
# finally:
#     f_try.close()

# МОДУЛЬ 17

# s = input()
# t = input()
# if t == s[::-1]:
#     print('YES')
# else:
#     print('NO')

# a = int(input())
# text = 'Even' if a % 2 == 0 else 'Odd'
# print(text)

# a = int(input())
# b = int(input())
# minimum = a if a < b else b
# maximum = b if b > a else a
# print(minimum, maximum)
#
# N_max = int(input("Определите размер очереди:"))
#
# queue = [0 for _ in range(N_max)]  # инициализируем список с нулевыми элементами
# order = 0  # будем хранить сквозной номер задачи
# head = 0  # указатель на начало очереди
# tail = 0  # указатель на элемент следующий за концом очереди

# def is_empty(): # очередь пуста?
#     # да, если указатели совпадают и в них содержится ноль
#     return head == tail and queue[head] == 0
#
# def size(): # получаем размер очереди
#     if is_empty(): # если она пуста
#         return 0 # возвращаем ноль
#     elif head == tail: # иначе, если очередь не пуста, но указатели совпадают
#         return N_max # значит очередь заполнена
#     elif head > tail: # если хвост очереди сместился в начало списка
#         return N_max - head + tail
#     else: # или если хвост стоит правее начала
#         return tail - head
#
# задание 17.4
# def add():  # добавляем задачу в очередь
#     global tail, order
#     order += 1  # увеличиваем порядковый номер задачи
#     queue[tail] = order  # добавляем его в очередь
#     print("Задача №%d добавлена" % (queue[tail]))
#
#     # увеличиваем указатель на 1 по модулю максимального числа элементов
#     # для зацикливания очереди в списке
#     tail = (tail + 1) % N_max
#
# def do():  # выполняем приоритетную задачу
#     global head
#     print("Задача №%d выполнена" % (queue[head]))
#     queue[head] = 0  # после выполнения зануляем элемент по указателю
#     head = (head + 1) % N_max  # и циклично перемещаем указатель
#
# while True:
#     cmd = input("Введите команду:")
#     if cmd == "empty":
#         if is_empty():
#             print("Очередь пустая")
#         else:
#             print("В очереди есть задачи")
#     elif cmd == "size":
#         print("Количество задач в очереди:", size())
#     elif cmd == "add":
#         if size() != N_max:
#             add()
#         else:
#             print("Очередь переполнена")
#     elif cmd == "show":
#         if is_empty():
#             print("Очередь пустая")
#         else:
#             show()
#     elif cmd == "do":
#         if is_empty():
#             print("Очередь пустая")
#         else:
#             do()
#     elif cmd == "exit":
#         for _ in range(size()):
#             do()
#         print("Очередь пустая. Завершение работы")
#         break
#     else:
#         print("Введена неверная команда")


# array = [2, 3, 1, 4, 6, 5, 9, 8, 7]
# count = 0
# for i in range(len(array)):  # проходим по всему массиву
#
#     idx_min = i  # сохраняем индекс предположительно минимального элемента
#     for j in range(i, len(array)):
#         if array[j] < array[idx_min]:
#             idx_min = j
#         count += 1
#     if i != idx_min:  # если индекс не совпадает с минимальным, меняем
#
#         array[i], array[idx_min] = array[idx_min], array[i]
#
# print(array)
# print(count)

# array = [2, 3, 1, 4, 6, 5, 9, 8, 7]
# count = 0
# for i in range(len(array)):  # проходим по всему массиву
#
#     for i in range(1, len(array)):
#         x = array[i]
#         idx = i
#         while idx > 0 and array[idx - 1] > x:
#             count += 1
#             array[idx] = array[idx - 1]
#             idx -= 1
# #         array[idx] = x
# print(array)
# print(count)
#
# G = {"Адмиралтейская" :
#          {"Садовая" : 4},
#      "Садовая" :
#          {"Сенная площадь" : 3,
#           "Спасская" : 3,
#           "Адмиралтейская" : 4,
#           "Звенигородская" : 5},
#      "Сенная площадь" :
#          {"Садовая" : 3,
#           "Спасская" : 3},
#      "Спасская" :
#          {"Садовая" : 3,
#           "Сенная площадь" : 3,
#           "Достоевская" : 4},
#      "Звенигородская" :
#          {"Пушкинская" : 3,
#           "Садовая" : 5},
#      "Пушкинская" :
#          {"Звенигородская" : 3,
#           "Владимирская" : 4},
#      "Владимирская" :
#          {"Достоевская" : 3,
#           "Пушкинская" : 4},
#      "Достоевская" :
#          {"Владимирская" : 3,
#           "Спасская" : 4}}
#
#
# D = {k : 100 for k in G.keys()} # расстояния
# start_k = 'Адмиралтейская' # стартовая вершина
# D[start_k] = 0 # расстояние от нее до самой себя равно нулю
# U = {k : False for k in G.keys()} # флаги просмотра вершин
# P = {k : None for k in G.keys()} # предки
#
# for _ in range(len(D)):
#     # выбираем среди непросмотренных наименьшее по расстоянию
#     min_k = min([k for k in U.keys() if not U[k]], key = lambda x: D[x])
#
#     for v in G[min_k].keys(): # проходимся по всем смежным вершинам
#          if D[v] > D[min_k] + G[min_k][v]: # если расстояние от текущей вершины меньше
#             D[v] = D[min_k] + G[min_k][v] # то фиксируем его
#             P[v] = min_k # и записываем как предок
#     U[min_k] = True # просмотренную вершину помечаем
#
# pointer = 'Владимирская' # куда должны прийти
# while pointer is not None: # перемещаемся, пока не придём в стартовую точку
#     print(pointer)
#     pointer = P[pointer]
#
# print(P)





class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None

    def insert_left(self, next_value):
        if self.left_child is None:
            self.left_child = BinaryTree(next_value)
        else:
            new_child = BinaryTree(next_value)
            new_child.left_child = self.left_child
            self.left_child = new_child
        return self

    def insert_right(self, next_value):
        if self.right_child is None:
            self.right_child = BinaryTree(next_value)
        else:
            new_child = BinaryTree(next_value)
            new_child.right_child = self.right_child
            self.right_child = new_child
        return self

    def post_order(self):
        if self.left_child is not None:  # если левый потомок существует
            self.left_child.post_order()  # рекурсивно вызываем функцию

        if self.right_child is not None:  # если правый потомок существует
            self.right_child.post_order()  # рекурсивно вызываем функцию
        print(self.value)  # процедура обработки

A_node = BinaryTree('2').insert_left('7').insert_right('5')
node_root = BinaryTree(2).insert_left(7).insert_right(5)
node_7 = node_root.left_child.insert_left(2).insert_right(6)
node_6 = node_7.right_child.insert_left(5).insert_right(11)
node_5 = node_root.right_child.insert_right(9)
node_9 = node_5.right_child.insert_left(4)

node_root.post_order()