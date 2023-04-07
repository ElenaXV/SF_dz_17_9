numbers_list = list(map(int, input('Введите последовательность чисел через пробел:').split()))
element = int(input("Введите любое число: "))

def sort_list(numbers_list):
    for i in range(1, len(numbers_list)):
        x = numbers_list[i]
        idx = i
        while idx > 0 and numbers_list[idx - 1] > x:
            numbers_list[idx] = numbers_list[idx - 1]
            idx -= 1
        numbers_list[idx] = x
    return numbers_list
sequence_sorted = sort_list(numbers_list)

print("Сортировка списка по возрастанию в нем элементов: ", sequence_sorted)

def binary_search(numbers_list, element, left, right):
    if left > right:  # если левая граница превысила правую,
        return False  # значит элемент отсутствует

    middle = (right + left) // 2  # находимо середину
    if numbers_list[middle] == element:  # если элемент в середине,
        return middle  # возвращаем этот индекс
    elif element < numbers_list[middle]:  # если элемент меньше элемента в середине
        # рекурсивно ищем в левой половине
        return binary_search(numbers_list, element, left, middle - 1)
    else:  # иначе в правой
        return binary_search(numbers_list, element, middle + 1, right)

print(binary_search(numbers_list, element, 0,  len(numbers_list)))


