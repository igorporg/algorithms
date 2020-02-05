# Отсортируйте по убыванию методом пузырька одномерный целочисленный массив, заданный случайными числами на промежутке [-100; 100).
# Выведите на экран исходный и отсортированный массивы.
# Примечания:
# ● алгоритм сортировки должен быть в виде функции, которая принимает на вход массив данных,
# ● постарайтесь сделать алгоритм умнее, но помните, что у вас должна остаться сортировка пузырьком.
# Улучшенные версии сортировки, например, расчёской, шейкерная и другие в зачёт не идут.

import random

SIZE = 10
MAX_ITEM = 99
MIN_ITEM = -100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print("Исходный массив:                ", array)


def sort_puz(array, sort_to):
    n = 1
    while n < len(array):
        for i in range(len(array) - n):
            if sort_to == 'MIN' and array[i] < array[i + 1] or sort_to == 'MAX' and array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
        n += 1
        # print(array)
    return array


print("Отсортированный по убыванию:    ", sort_puz(array, 'MIN'))
print("Отсортированный по возрастанию: ", sort_puz(array, 'MAX'))
