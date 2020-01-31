# Написать два алгоритма нахождения i-го по счёту простого числа.
# Функция нахождения простого числа должна принимать на вход натуральное
# и возвращать соответствующее простое число. Проанализировать скорость и сложность алгоритмов.

# Первый — с помощью алгоритма «Решето Эратосфена».
# Примечание. Алгоритм «Решето Эратосфена» разбирался на одном из прошлых уроков.
# Используйте этот код и попробуйте его улучшить/оптимизировать под задачу.
# Второй — без использования «Решета Эратосфена».


# Первый — с помощью алгоритма «Решето Эратосфена».
# на мой взгляд сложновато и запутанно получилось
#
# number = int(input('Введите порядковый номер искомого простого числа: '))
# STEP = 100  # Шаг поиска
# sieve = [i for i in range(STEP)]  # Первоначальный массив
# sieve[1] = 0
# res = []  # Результирующий массив простых чисел
#
#
# def simple_digit(number):
#     global res, sieve
#     if len(res) > number:
#         return res[number - 1]  # -1 чтобы убрать 0 из подсчета
#
#     for i in range(2, len(sieve)):
#         if sieve[i] != 0:
#             j = i + i
#             while j < len(sieve):
#                 sieve[j] = 0
#                 j += i
#
#     res = [i for i in sieve if i != 0]
#     sieve += [i for i in range(len(sieve), len(sieve) + STEP)]
#
#     return simple_digit(number)
#
#
# simple = simple_digit(number)
# print(res)
# print(f'Простое число с порядковым номером {number} = {simple}')

# Второй — без использования «Решета Эратосфена».

number = int(input('Введите порядковый номер искомого простого числа: '))
STEP = 100  # Шаг поиска
sieve = [i for i in range(2, STEP)]  # Первоначальный массив
res = []  # Результирующий массив простых чисел


def simple_digit(number):
    global res, sieve
    if len(res) > number:
        return res[number - 1]  # -1 чтобы убрать 0 из подсчета

    res = []
    for i in sieve:
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            res.append(i)

    sieve += [i for i in range(len(sieve), len(sieve) + STEP)]
    return simple_digit(number)


simple = simple_digit(number)
print(res)
print(f'Простое число с порядковым номером {number} = {simple}')
