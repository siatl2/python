from typing import List

def reverse_elements(input_nums : List[int]) -> List[int]:
    '''
    Определите функцию reverse_elements, принимающую один пара-
    метр.

    Функция должна возвращать новый список, в котором порядок
    элементов исходного списка изменен на противоположный.

    :param input_nums: Список чисел
    :return: Список чисел, порядок изменен на противоположный
    '''

    return [input_nums[i] for i in range(len(input_nums) - 1, -1, -1)]

'''
Кейсы:
Вход: [1, 2, 3, 4, 5]
Выход: [5, 4, 3, 2, 1]
Вход: []
Выход: []
Вход: [20, 15, 25, 10, 30, 5, 0]
Выход: [0, 5, 30, 10, 25, 15, 20]
'''
reverse_array : List[int] = reverse_elements([1, 2, 3, 4, 5])
assert reverse_array == [5, 4, 3, 2, 1]

reverse_array : List[int] = reverse_elements([])
assert reverse_array == []

reverse_array : List[int] = reverse_elements([20, 15, 25, 10, 30, 5, 0])
assert reverse_array == [0, 5, 30, 10, 25, 15, 20]

print("Done")