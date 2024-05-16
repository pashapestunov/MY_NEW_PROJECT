from math import pi
from datetime import datetime as date

a, b, c = 1, 2, 3

result = a + b * c
print(result)

d, e, f = 'ABC'
print(d, f)

g, *h = 'ABC'
print(g, h)

i = j = k = 5
print(j, '-', k)

l = 12
m = 5

l, m = m, l
print(l)

n = 5
n += n

print(n)

o = 10
p = 5

o <<= p
print(o)

text = 'Hello, my name is {} i\'m work in {}'  # {0} {1} or {1} {0} or {name} {work} .format(name='pasha', work='paul')
text_new = text.format('Pasha', 'Paul')
print(text_new)

name = 'Pavel'
age = '26'

text_about_me = f'Hello, my name is {name}, i\'m {age}'
print(text_about_me)

print(f'Число pi будет = {pi:.2f}')

now = date.now()

print(f'Текущее время: {now: %d.%m.%Y %H:%M}')


my_cash = 40

while my_cash > 0:
    print(f'you have {my_cash} money')
    my_cash -= 20
    print(f'you have {my_cash} money')
else:
    print('you don\'t have money')


number = int(input('enter your number: '))

for i in range(1, 10):
    value = number * i
    print(f'{number} * {i} = {value}', end=' ')
print()

number = int(input('enter your number: '))


for i in range(0, number, 2):
    print(i, end=' ')


some_litters = 'abc'

for i in some_litters:
    print(f'Current litter is: ', i)

some_dict = {'Минск': 1.2, 'Гомель': 0.8, 'Брест': 0.7}
for key, value in some_dict.items():
    print('Население', key, '-', value)


for i in range(1, 10):
    if i == 3 or i == 4 or i == 5:
        continue
    print(i, end=' ')