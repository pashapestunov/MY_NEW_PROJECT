import math

a = float(input('Введите значение а: '))
b = float(input('Введите значение b: '))

y = ((a**2 / 3) + (a**2 + 4) / b + math.sqrt(a**2 + 4) / 4 + math.sqrt(a**2 + 4)**3 /4)

result = round(y, 2)
print('Значение по формуле', result)
print()

a = float(input('Введите значение x для cos(): '))
b = float(input('Введите значение x для sin(): '))

y = math.cos(a) + math.sin(b)

result = round(y, 2)
print('Значение по формуле', result)
print()

x = float(input('Введите значение x для: '))

y_2 = (math.cos(x**2)**2 + math.sin(2 * x - 1)**2)
y_3 = math.pow(y_2, 1/3)

result = round(y_3, 2)
print('Значение по формуле', result)
print()


x = float(input('Введите значение x для: '))

y = 5 * x + 3 * x**2 * math.sqrt(1 + math.sin(x)**2)

result = round(y, 2)
print('Значение по формуле', result)
print()


