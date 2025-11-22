from typing import List, Optional

def get_second_largest_number(input_nums : List[int]) -> Optional[int]:
    '''
    Определите функцию get_second_largest_number, принимающую
    один параметр

    Функция должна возвращать второе по величине число в списке.
    Если второго по величине числа нет, то функция должна возвра-
    щать None.

    :param input_nums: Список чисел
    :return: Второе по величине число
    '''
    max_first_digit : Optional[int] = None
    max_second_digit : Optional[int] = None

    for num in input_nums:
        if (max_first_digit is None):
            max_first_digit = num
        elif (num > max_first_digit):
            max_second_digit = max_first_digit
            max_first_digit = num
        elif ((num < max_first_digit) \
              and ((max_second_digit is None) \
                   or (num > max_second_digit))):
            max_second_digit = num

    return max_second_digit

'''
Кейсы:
Вход: [1, 2, 3, 4, 5]
Выход: 4
Вход: [3, 45, 345, 435, 345, 43, 56, 34, 234, 34]
Выход: 345
Вход: [1]
Выход: None
'''

calc_num : Optional[int] = get_second_largest_number([1, 2, 3, 4, 5])
assert calc_num == 4

calc_num : Optional[int] = get_second_largest_number([3, 45, 345, 435, 345, 43, 56, 34, 234, 34])
assert calc_num == 345

calc_num : Optional[int] = get_second_largest_number([1])
assert calc_num == None

print('Done')
