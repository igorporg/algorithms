# Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран. Например, если введено число 3486, надо вывести 6843.

d = int(input("Введите многозначное натуральное число: "))
r = ""
while d > 0:
    last = d % 10
    r += str(last)
    d = d // 10

print(f'обратный порядок числа - {r}')
