a = int(input('Дистанция бега в первый день: '))
b = int(input('Цель: '))
days = 1
while a < b:
    a *= 1.1
    days += 1
print(f'Требуемое количество дней: {days}')
