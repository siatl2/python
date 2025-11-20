from typing import Optional

def sum_if_less_than_fifty(num_one: int, num_two: int) -> Optional[int]:
    '''
    Определите функцию sum_if_less_than_fifty, принимающую два па-
    раметра int.
    Функция должна возвращать:
    - сумму двух чисел, если эта сумма меньше 50;
    - None, если сумма двух чисел больше или равна 50.

    :param num_one: int - первое число
    :param num_two: int - второе число
    :return:Optional[int] - результат операции
    '''
    return num_one + num_two if (num_one + num_two < 50) else None

'''
кейсы:
Входы:
- num_one = 20
- num_two = 20
Выход: 40
Входы:
- num_one = 20 
- num_two = 100
Выход: None
'''
print(sum_if_less_than_fifty(20, 20))
print(sum_if_less_than_fifty(20, 100))