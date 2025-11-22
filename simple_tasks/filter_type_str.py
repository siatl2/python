from typing import List, Union

def filter_type_str(input_list: List[Union[str, int]]) -> List[str]:
    '''
    Определите функцию filter_type_str, принимающую один параметр

    Функция должна возвращать новый список, содержащий только
    строки из оригинального списка.

    :param input_list: Список строк и чисел
    :return: Список строк из входящего параметра
    '''
    return [elem for elem in input_list if type(elem) == str]

'''
Кейсы:
Вход: ["hello", 1, 2, "www"]
Выход: ["hello", "www"]
Вход: []
Выход: []
Вход: [1, 2, 3, 4, 5]
Выход: []
'''
list_str : List[str] = filter_type_str(["hello", 1, 2, "www"])
assert list_str == ["hello", "www"]

list_str : List[str] = filter_type_str([])
assert list_str == []

list_str : List[str] = filter_type_str([1, 2, 3, 4, 5])
assert list_str == []

print("Done")
