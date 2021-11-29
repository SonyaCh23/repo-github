earning = int(input('Выручка: '))
costs = int(input('Издержки: '))
if earning < costs:
    print('Убыток')
elif earning > costs:
    print('Прибыль')
    profitability = (earning - costs) / earning
    print(f'Рентабельность: {profitability} ')
    a = int(input('Количество сотрудников: '))
    b = (earning - costs) / a
    print(f'Прибыль фирмы из расчета на одного сотрудника: {b}')
