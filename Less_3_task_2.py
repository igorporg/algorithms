# Во втором массиве сохранить индексы четных элементов первого массива.
# Например, если дан массив со значениями 8, 3, 15, 6, 4, 2,
# второй массив надо заполнить значениями 0, 3, 4, 5, (индексация начинается с нуля),
# т.к. именно в этих позициях первого массива стоят четные числа.
import random

SIZE = 100
MAX_ITEM = 100
MIN_ITEM = 1
array_1 = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
array_2 = []

for pos, item in enumerate(array_1):
    if item % 2 == 0:
        array_2 += [pos]

print(array_1)
print(array_2)
