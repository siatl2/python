def format_number_with_commas(input_num : int) -> str:
    '''
    Определите функцию format_number_with_commas, принимающую
    один параметр

    Функция должна возвращать строковое представление числа,
    в котором группы по 3 разряда (начиная справа) разделены за-
    пятыми.

    :param input_num: число
    :return: строка с разделителями
    '''
    str_with_commas : str = ''
    str_input_num : str = str(input_num)
    len_input_num : int = len(str_input_num)

    for i in range(0, len_input_num):
        str_with_commas += str_input_num[i]
        need_comma : bool = ((len_input_num - i - 1) / 3).is_integer() \
                            and i != (len_input_num - 1)
        if need_comma:
            str_with_commas += ','

    return str_with_commas

'''
Кейсы:
Вход: 1000000
Выход: "1,000,000"
Вход: 12345
Выход: "12,345"
Вход: -99999999
Выход: "-99,999,999"
'''
str_itog : str = format_number_with_commas(1000000)
assert str_itog == "1,000,000"

str_itog : str = format_number_with_commas(12345)
assert str_itog == "12,345"

str_itog : str = format_number_with_commas(-99999999)
assert str_itog == "-99,999,999"

print("done")