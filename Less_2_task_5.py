#  Вывести на экран коды и символы таблицы ASCII, начиная с символа под номером 32 и заканчивая 127-м включительно.
#  Вывод выполнить в табличной форме: по десять пар "код-символ" в каждой строке.
start = 32
end = 127


def show10sym(start):
    stroka = "|"
    if start - end > 0:
        return ""
    for i in range(start, end + 1 if start + 10 > end else start + 10):
        stroka += (f' {i} - "{chr(i)}" | ')
    print(stroka)
    return show10sym(start + 10)


print(show10sym(start))
