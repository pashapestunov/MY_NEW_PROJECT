import math


def line_year(r, v):
    r_earth = r * (10 ** 9)
    v_earth = v * (10 ** 3)
    l = 2 * r_earth * math.pi / v_earth
    return l


planets = {}
counter = 1

while counter <= 2:
    name = input('Введите имя планеты: ')
    r = float(input('Радиус орбиты планеты(млн.км): '))
    v = float(input('Орбитальная скорость(км/ч): '))

    planet = line_year(r, v)
    days = round(planet / (60 * 60 * 24), 2)
    planets[name] = days
    counter += 1

    print('Длинна года на планете', name, '-', days, 'дней')

names = list(planets.keys())
dayss = list(planets.values())
difference = round(dayss[0] - dayss[1])

if len(planets) >= 1:
    print('Первая планета: ', names[0], '-', dayss[0], 'дней в году')
else:
    print('Словарь пустой')
if len(planets) >= 1:
    print('Вторая планета: ', names[1], '-', dayss[1], 'дней в году')
else:
    print('Словарь содержит только одну пару')
if dayss[0] > dayss[1]:
    print('На первой планете', names[0], 'дней в году больше чем на второй', names[1], 'на', difference)
else:
    print('На первой планете', names[0], 'дней в году меньше чем на второй', names[1], 'на', difference)

