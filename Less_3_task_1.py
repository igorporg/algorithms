# В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.

MAX_ITEM_1 = 99
MIN_ITEM_1 = 2
MAX_ITEM_2 = 9
MIN_ITEM_2 = 2

array_1 = [i for i in range(MIN_ITEM_1, MAX_ITEM_1 + 1)]
array_2 = [i for i in range(MIN_ITEM_2, MAX_ITEM_2 + 1)]

for i in array_2:
    multiple = 0
    for j in array_1:
        if j % i == 0:
            multiple += 1
    print(f'{i} = {multiple}')
