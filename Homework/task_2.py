number_of_seconds = int(input('Введите время в секундах: '))
hh = number_of_seconds//(3600)
mm = (number_of_seconds - hh*3600)//60
ss = number_of_seconds - hh*3600 - mm*60
print(f"{hh:02}:{mm:02}:{ss:02}")
