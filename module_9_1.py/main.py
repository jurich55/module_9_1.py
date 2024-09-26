
def apply_all_func(int_list, *functions):
    results = {}                                 # Задаем словарь как тип выходных данных
    for nm_fnc in functions:                           # Перебираем список functions
        results[nm_fnc.__name__] = str(nm_fnc(int_list))    # Добавляем в словарь имя функции                                                  # а значение - результат функции
    return results              # Возвращаем словарь {'имя функции': 'результат функции'}


print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))
