# 3). Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом. Найдите в массиве медиану.
# Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы, которые не меньше медианы, в другой — не больше медианы.
# Примечание: задачу можно решить без сортировки исходного массива. Но если это слишком сложно, используйте метод сортировки,
# который не рассматривался на уроках (сортировка слиянием также недопустима).

import random

MAX_1 = 10
MIN_1 = 2
MAX_2 = 1000
MIN_2 = 0
m = random.randint(MIN_1, MAX_1)
SIZE = 2 * m + 1
array = [random.randint(MIN_2, MAX_2) for _ in range(SIZE)]
print(array, " - исходный массив")

# Для сортировки массива буду использовать свой метод, на ноухау не претендую, возможно уже есть такой
# Суть метода - сравниваем первый элемент массива с последним, если первый больше последнего то меняем местами, меньшее - оставляем,
# далее берем следующий и сравниваем с последним и так далее пока не пройдем весь
# массив и получим максимальное значение в его конце, далее проделываем все тоже самое с предпоследним элементом (очень напоминает метод пузырька и сложность та же)
# P.S. Задачу с медианой мог бы решить без сортировки, но я поленился

def my_sort(array):
    n = 0
    LENGTH = len(array)
    while n < LENGTH:
        for i in range(len(array) - n):
            if array[i] > array[LENGTH - 1 - n]:
                array[i], array[LENGTH - 1 - n] = array[LENGTH - 1 - n], array[i]
        n += 1
        # print(array)
    return array

print(my_sort(array), " - отсортированный массив")

# Ищем серидину и получаем медиану

middle = len(array) // 2
print(array[middle], " - медиана")
