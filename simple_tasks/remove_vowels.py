def remove_vowels(input_str : str) -> str:
    '''
    Определите функцию remove_vowels, принимающую один
    параметр input_str

    Функция должна возвращать новую строку, из которой
    удалены все гласные.

    :param input_str: входящая стока
    :return: строка, из уоторой удалены все гласные

    Гласные это один из символов "aeiouAEIOU"
    '''
    return (''
            .join([x for x in input_str if x not in 'aeiouAEIOU']))

'''
Кейсы:
Вход: "Hello, World!"
Выход: "Hll, Wrld!"
Вход: "aeiouAEIOU"
Выход: ""
Вход: "zzxxxccvvvbbnnmmmLLKKJJHH"
Выход: "zzxxxccvvvbbnnmmmLLKKJJHH"
'''
result : str = remove_vowels("Hello, World!")
assert result == "Hll, Wrld!"

result : str = remove_vowels("aeiouAEIOU")
assert result == ""

result : str = remove_vowels("zzxxxccvvvbbnnmmmLLKKJJHH")
assert result == "zzxxxccvvvbbnnmmmLLKKJJHH"

print("Done")