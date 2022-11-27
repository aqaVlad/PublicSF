# Вводится последовательность чисел через пробел.
# У пользователя запрашивается число.
# ? Выполнить проверку соответствия указанному в условии ввода данных?
# ! Есть числа, которые могут не соответствовать условиям - вывести уведомление!

# Алгоритм:
# Преобразовать введённую последовательность в список.
# Сортировать список по возрастанию элементов (через функцию).
# Установить номера позиции элементов, между которыми будет введенное число (функцией через двоичный поиск).

array = list(map(int, input('Введите через пробел последовательность из нескольких чисел:  ').split()))
# 9 1 8 4 13 17 0 23 48 5 21 90 121
element = int(input('Введите число для поиска:  '))  # 22
L = array.append(element)

# Сортировка вставками
def ranking(array):
    for i in range(1, len(array)):
        x = array[i]
        idx = i
        while idx > 0 and array[idx-1] > x:
            array[idx] = array[idx-1]
            idx -= 1
        array[idx] = x
    return array

print('Сортированный список с новым элементом:  ', ranking(array))

if element <= ranking(array)[0]:
    print('Вы ввели наименьший элемент последовательности')

elif element >= ranking(array)[-1]:
    def bi_search(element, array):
        left, right = 0, len(array)
        while left < right:
            middle = (left + right) // 2
            if array[middle] < element:
                left = middle+1
            else:
                right = middle
        return left-1
    print('Вы ввели наибольший элемент последовательности.',
          'Порядковый номер позиции числа, после которого расположен новый элемент: ', bi_search(element, array))

else:
# бинарный поиск
    def bi_search(element, array):
        left, right = 0, len(array)
        while left < right:
            middle = (left + right) // 2
            if array[middle] < element:
                left = middle+1
            else:
                right = middle
        return left-1, left+1
    print('Порядковые номера позиций чисел, между которыми расположен новый элемент: ', bi_search(element, array))
