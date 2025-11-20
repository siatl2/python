from functools import reduce
from typing import List

def sum_even(input_nums: List[int]) -> int:
    '''
    Определите функцию sum_even, принимающую один параметр список int.
    Функция должна возвращать сумму всех четных чисел в списке.

    :param input_nums: List[int] - список чисел
    :return: int - сумма четных числе списка
    '''
    return reduce(lambda x, y: x + y,
                  filter(lambda x: x % 2 == 0, input_nums),
                  0)

'''
кейсы:
Вход: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Выход: 30
Вход: [10, 20, 30, 40, 50]
Выход: 150
Вход: [9, 7, 5, 3, 1]
Выход: 0
'''
print(sum_even([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

print(sum_even([10, 20, 30, 40, 50]))

print(sum_even([9, 7, 5, 3, 1]))