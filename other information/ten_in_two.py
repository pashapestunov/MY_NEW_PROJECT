num = int(input("Введите число для перевода в двоичную: "))

tw = []

while num > 0:
    tw.append(num % 2)
    num //= 2
tw.reverse()

for i in tw:
    print(i, end="")
