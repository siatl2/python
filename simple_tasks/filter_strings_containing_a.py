from typing import List

def filter_strings_containing_a(input_strs: List[str]) -> List[str]:
    '''
    Функция должна возвращать новый список, содержащий только
    строки, содержащие букву «a»

    :param input_strs: input_strs list[str] - входящий список
    :return:list[str] - новый список, содержащий строки с буквой  «a»
    '''
    return [n for n in input_strs if 'a' in n]
'''
кейсы:
Вход: ["apple", "banana", "cherry", "date"]
Выход: ["apple", "banana", "date"]

Вход: []
Выход: []

Вход: ["bbbb", "cccc"]
Выход: []
'''
input_list : List[str] = ['apple', 'banana', 'cherry', 'date']
result : List[str] = filter_strings_containing_a(input_list)
assert result == ['apple', 'banana', 'date']

input_list : List[str] = []
result : List[str] = filter_strings_containing_a(input_list)
assert result == []

input_list : List[str] = ['bbbb', 'cccc']
result : List[str] = filter_strings_containing_a(input_list)
assert result == []

print('Done')
