# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
import random

SIZE = 10
MAX_ITEM = 1000
MIN_ITEM = -1000
array_1 = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
min_ = 0
max_ = 0
print(array_1)

for item in array_1:
    if item > max_:
        max_ = item
    if item < min_:
        min_ = item

for pos, item in enumerate(array_1):
    if item == min_:
        array_1[pos] = max_
    elif item == max_:
        array_1[pos] = min_

print(f'min = {min_}, max = {max_}')
print(array_1)
