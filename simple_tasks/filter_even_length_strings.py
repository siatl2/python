from typing import List

def filter_even_length_strings(input_strs : List[str]) -> List[str]:
    '''
    Определите функцию filter_even_length_strings, принимающую один
    параметр

    Функция должна возвращать новый список, в котором оставле-
    ны только строки, содержащие четное число символов.

    :param input_strs: Список слов
    :return: Список слов с четным к-вом символов
    '''

    return [word for word in input_strs if len(word) % 2 == 0]

'''
Кейсы:
Вход: ["cat", "dog", "fish", "elephant"]
Выход: ["fish", "elephant"]
Вход: ["q", "w", "e", "r", "t", "y"]
Выход: []
Вход: ["qq", "ww", "ee", "rr", "tt", "yy"]
Выход: ["qq", "ww", "ee", "rr", "tt", "yy"]
'''
list_itog = filter_even_length_strings(["cat", "dog", "fish", "elephant"])
assert list_itog == ["fish", "elephant"]

list_itog = filter_even_length_strings(["q", "w", "e", "r", "t", "y"])
assert list_itog == []

list_itog = filter_even_length_strings(["qq", "ww", "ee", "rr", "tt", "yy"])
assert list_itog == ["qq", "ww", "ee", "rr", "tt", "yy"]

print('Done')