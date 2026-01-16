from typing import List

import pandas as pd
from pandas import DataFrame

def analyze_data_store_sales(input : DataFrame) -> List[str]:
    '''
    Проанализировать данные о продажах интернет - магазина

    :param input: Входящий DataFrame
    :return: Список результатов
    '''
    return_lst = []

    # Только электроника
    el =  input[input['Category'] == 'Электроника'][['ProductName']]
    return_lst.append('\nТолько электроника:\n' + str(el))

    #Новый столбец с НДС
    input['PriceWithVAT'] = input['Price'] * 1.22
    vat = input[['ProductName', 'Price', 'PriceWithVAT']]
    return_lst.append('\nДобавлен столбец НДС:\n' + str(vat))

    #Средняя цена по категориям
    avg_price_by_category = input.groupby('Category')['Price'].mean()
    return_lst.append('\nСредняя цена по категориям:\n' + str(avg_price_by_category))

    #Самый дорогой товар
    most_expensive_product = input.loc[input['Price'].idxmax()]
    return_lst.append('\nСамый дорогой товар:\n' + str(most_expensive_product))

    return return_lst

data = {
    'ProductId' : [101, 102, 103, 104, 105],
    'ProductName': ['Ноутбук', 'Мышь', 'Клавиатура', 'Монитор', 'Веб-камера'],
    'Category': ['Электроника', 'Аксессуары', 'Аксессуары', 'Электроника', 'Аксессуары'],
    'Price': [1_200, 150, 500, 2_500, 300]
}

lst = analyze_data_store_sales(pd.DataFrame(data))

for x in lst:
    print(x)