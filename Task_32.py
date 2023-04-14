# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)def find_indexes(arr, minimum, maximum):

# def find_index(array, minimum, maximum):
#     indexes = []
#     for i in range(len(array)):
#         if minimum <= array[i] <= maximum:
#             indexes.append(i)
#     return indexes

# array = [ 1, 3, 6, 34, 8, 9, 12, 14, 15, 18, 21, 38]
# minimum = int(input("Введите минимальный элемент: "))
# maximum = int(input("Введите максимальный элемент: "))

# indexes = find_index(array, minimum, maximum)
# print(indexes) 



array = [ 1, 3, 6, 34, 8, 9, 12, 14, 15, 18, 21, 38]
minimum = int(input("Введите минимальный элемент: "))
maximum = int(input("Введите максимальный элемент: "))
for i in range(len(array)):
    if minimum <= list_1[i] <= maximum:
        print(i)