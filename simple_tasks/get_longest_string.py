from typing import List

def get_longest_string(input_strs : List[str]) -> str :
    '''
    Определите функцию get_longest_string, принимающую один
    параметр.

    Функция должна возвращать самую длинную строку в списке.
    Если таких несколько, то должна быть возвращена та, что
    встречается в списке первой.

    :param input_strs: массив строк
    :return: самая длинная строка
    '''
    longest_string : str = ''
    long_string : int = 0

    for input_str in input_strs:
        if len(input_str) > long_string:
            long_string = len(input_str)
            longest_string = input_str

    return longest_string
'''
Кейсы:
Вход: ["cat", "dog", "bird", "lizard"]
Выход: "lizard"
Вход: ["cat", "dog", "bird", "wolf"]
Выход: "bird"
Вход: ["a", "b", "c", "d"]
Выход: "a"
'''
longest_string = get_longest_string(["cat", "dog", "bird", "lizard"])
assert longest_string == "lizard"

longest_string = get_longest_string(["cat", "dog", "bird", "wolf"])
assert longest_string == "bird"

longest_string = get_longest_string(["a", "b", "c", "d"])
assert longest_string == "a"

print('Done')
