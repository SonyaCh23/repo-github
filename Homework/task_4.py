n = int(input("Введите целое положительное число: "))
max_n = 0
while n > 0:
    if n % 10 > max_n:
      max_n = n % 10
      if max_n == 9:
          break
    n //= 10
print (f'Наибольшая цифра числа: {max_n}')
