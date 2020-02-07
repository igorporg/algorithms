# Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
# заданный случайными числами на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.

import random

SIZE = 10
MAX_ITEM = 49
MIN_ITEM = 0
array = [random.uniform(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)


def merge(array):
    if len(array) <= 1:
        return array

    def sort(left_arr, right_arr):
        result = []
        idx_left = idx_right = 0

        for _ in range(len(left_arr) + len(right_arr)):
            if idx_left < len(left_arr) and idx_right < len(right_arr):

                if left_arr[idx_left] <= right_arr[idx_right]:
                    result.append(left_arr[idx_left])
                    idx_left += 1

                else:
                    result.append(right_arr[idx_right])
                    idx_right += 1

            elif idx_left == len(left_arr):
                result.append(right_arr[idx_right])
                idx_right += 1

            elif idx_right == len(right_arr):
                result.append(left_arr[idx_left])
                idx_left += 1

        return result

    middle = len(array) // 2
    left_arr = merge(array[:middle])
    right_arr = merge(array[middle:])

    return sort(left_arr, right_arr)


print(merge(array))
