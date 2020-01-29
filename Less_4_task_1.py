# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
import random
import timeit
import cProfile

# Вариант № 1

def change_max_min_1(MIN_ITEM, MAX_ITEM, SIZE):
    min_ = 0
    max_ = 0
    array_1 = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]

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

    return array_1

# print(timeit.timeit('change_max_min_1(-100, 100, 10)', number=100, globals=globals()))  # 0.002379399999999997
# print(timeit.timeit('change_max_min_1(-100, 100, 20)', number=100, globals=globals()))  # 0.004330800000000003
# print(timeit.timeit('change_max_min_1(-100, 100, 40)', number=100, globals=globals()))  # 0.0088163
# print(timeit.timeit('change_max_min_1(-100, 100, 80)', number=100, globals=globals()))  # 0.015905799999999998
# print(timeit.timeit('change_max_min_1(-100, 100, 160)', number=100, globals=globals())) # 0.030398099999999997

# cProfile.run('change_max_min(-100, 100, 1000)')
# 1    0.001    0.001    0.004    0.004 Less_4_task_1.py:11(<listcomp>)
# 1    0.000    0.000    0.004    0.004 Less_4_task_1.py:8(change_max_min_1)

# cProfile.run('change_max_min(-100, 100, 2000)')
# 1    0.001    0.001    0.007    0.007 Less_4_task_1.py:11(<listcomp>)
# 1    0.000    0.000    0.007    0.007 Less_4_task_1.py:8(change_max_min_1)

# cProfile.run('change_max_min(-100, 100, 4000)')
# 1    0.002    0.002    0.013    0.013 Less_4_task_1.py:11(<listcomp>)
# 1    0.002    0.002    0.015    0.015 Less_4_task_1.py:8(change_max_min_1)

# cProfile.run('change_max_min(-100, 100, 8000)')
# 1    0.004    0.004    0.026    0.026 Less_4_task_1.py:11(<listcomp>)
# 1    0.002    0.002    0.027    0.027 Less_4_task_1.py:8(change_max_min_1)

# cProfile.run('change_max_min(-100, 100, 16000)')
# 1    0.007    0.007    0.049    0.049 Less_4_task_1.py:11(<listcomp>)
# 1    0.003    0.003    0.052    0.052 Less_4_task_1.py:8(change_max_min_1)

# array_1 = change_max_min_1(-100, 100, 10)
# print(array_1)

# ************************************************************
# Вывод - сложность данного алгоритма линейная - O(n)* (1 + 1)
# ************************************************************

# Вариант № 2

def change_max_min_2(MIN_ITEM, MAX_ITEM, SIZE):
    min_pos = 0
    max_pos = 0
    array_1 = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
    for item in range(1, SIZE):
        if array_1[item] > array_1[max_pos]:
            max_pos = item
        elif array_1[item]  < array_1[min_pos]:
            min_pos = item

    array_1[min_pos], array_1[max_pos] = array_1[max_pos], array_1[min_pos]
    return array_1

# print(timeit.timeit('change_max_min_2(-100, 100, 10)', number=100, globals=globals()))  # 0.0025270000000000015
# print(timeit.timeit('change_max_min_2(-100, 100, 20)', number=100, globals=globals()))  # 0.004698399999999998
# print(timeit.timeit('change_max_min_2(-100, 100, 40)', number=100, globals=globals()))  # 0.009223799999999997
# print(timeit.timeit('change_max_min_2(-100, 100, 80)', number=100, globals=globals()))  # 0.017479299999999996
# print(timeit.timeit('change_max_min_2(-100, 100, 160)', number=100, globals=globals())) # 0.028862000000000013

# cProfile.run('change_max_min_2(-100, 100, 1000)')
# 1    0.000    0.000    0.004    0.004 Less_4_task_1.py:56(change_max_min_2)
# 1    0.000    0.000    0.003    0.003 Less_4_task_1.py:59(<listcomp>)

# cProfile.run('change_max_min_2(-100, 100, 2000)')
# 1    0.001    0.001    0.006    0.006 Less_4_task_1.py:56(change_max_min_2)
# 1    0.001    0.001    0.006    0.006 Less_4_task_1.py:59(<listcomp>)

# cProfile.run('change_max_min_2(-100, 100, 4000)')
# 1    0.001    0.001    0.013    0.013 Less_4_task_1.py:56(change_max_min_2)
# 1    0.002    0.002    0.012    0.012 Less_4_task_1.py:59(<listcomp>)

# cProfile.run('change_max_min_2(-100, 100, 8000)')
# 1    0.002    0.002    0.025    0.025 Less_4_task_1.py:56(change_max_min_2)
# 1    0.003    0.003    0.023    0.023 Less_4_task_1.py:59(<listcomp>)

# cProfile.run('change_max_min_2(-100, 100, 16000)')
# 1    0.004    0.004    0.046    0.046 Less_4_task_1.py:56(change_max_min_2)
# 1    0.006    0.006    0.043    0.043 Less_4_task_1.py:59(<listcomp>)

# array_2 = change_max_min_2(-100, 100, 10)
# print(array_2)

# ************************************************************
# Вывод - сложность данного алгоритма также линейная - O(n)
# перебор массива идет всего один раз, вместо двух в первом варианте,
# но не совсем понятно почему время выполнения особо не уменьшилось.
# ************************************************************


# Вариант № 3
# Используем рекурсию

def change_max_min_3(MIN_ITEM, MAX_ITEM, SIZE):
    array_1 = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
    # print(array_1)
    min_pos = 0
    max_pos = 0

    def get_min_max(n):
        global min_pos, max_pos
        if n == 0:
            return min_pos, max_pos
        else:
            if array_1[n-1] > array_1[n]:
                max_pos = n - 1
            elif array_1[n-1] < array_1[n]:
                min_pos = n - 1
        return get_min_max(n-1)

    min_pos, max_pos = get_min_max(SIZE-1)
    array_1[min_pos], array_1[max_pos] = array_1[max_pos], array_1[min_pos]

    return array_1

# print(change_max_min_3(-100, 100, 10))

# print(timeit.timeit('change_max_min_3(-100, 100, 10)', number=100, globals=globals()))  # 0.002796699999999999
# print(timeit.timeit('change_max_min_3(-100, 100, 20)', number=100, globals=globals()))  # 0.005510600000000004
# print(timeit.timeit('change_max_min_3(-100, 100, 40)', number=100, globals=globals()))  # 0.010604199999999994
# print(timeit.timeit('change_max_min_3(-100, 100, 80)', number=100, globals=globals()))  # 0.0186123
# print(timeit.timeit('change_max_min_3(-100, 100, 160)', number=100, globals=globals())) # 0.035700499999999996

cProfile.run('change_max_min_3(-100, 100, 100)')
# 1    0.000    0.000    0.000    0.000 Less_4_task_1.py:109(change_max_min_3)
# 1    0.000    0.000    0.000    0.000 Less_4_task_1.py:110(<listcomp>)
# 100/1    0.000    0.000    0.000    0.000 Less_4_task_1.py:115(get_min_max)

cProfile.run('change_max_min_3(-100, 100, 200)')
# 1    0.000    0.000    0.001    0.001 Less_4_task_1.py:109(change_max_min_3)
# 0.000    0.000    0.001    0.001 Less_4_task_1.py:110(<listcomp>)
# 200/1    0.000    0.000    0.000    0.000 Less_4_task_1.py:115(get_min_max)

cProfile.run('change_max_min_3(-100, 100, 400)')
# 1    0.000    0.000    0.002    0.002 Less_4_task_1.py:109(change_max_min_3)
# 1    0.000    0.000    0.002    0.002 Less_4_task_1.py:110(<listcomp>)
# 400/1    0.001    0.000    0.001    0.001 Less_4_task_1.py:115(get_min_max)

cProfile.run('change_max_min_3(-100, 100, 800)')
# 1    0.000    0.000    0.004    0.004 Less_4_task_1.py:109(change_max_min_3)
# 1    0.000    0.000    0.003    0.003 Less_4_task_1.py:110(<listcomp>)
# 800/1    0.001    0.000    0.001    0.001 Less_4_task_1.py:115(get_min_max)

cProfile.run('change_max_min_3(-100, 100, 1600)')
# 1    0.000    0.000    0.007    0.007 Less_4_task_1.py:109(change_max_min_3)
# 1    0.001    0.001    0.005    0.005 Less_4_task_1.py:110(<listcomp>)
# 992/1    0.002    0.000    0.002    0.002 Less_4_task_1.py:115(get_min_max)

# *************************************************************************************
# Выдает такую ошибку - RecursionError: maximum recursion depth exceeded in comparison
# Вывод - сложность данного алгоритма также линейная - O(n)
# Рекурсия работает примерно также как и циклы но есть ограничение памяти по стеку.
# *************************************************************************************