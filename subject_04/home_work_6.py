numbers = [2, 15, 3, 5, 9, 1, 7, 12]
numbers.sort()
print(numbers)

index_1 = numbers.index(2)
index_2 = numbers.index(15)
index_3 = numbers.index(3)
index_4 = numbers.index(5)
index_5 = numbers.index(9)
index_6 = numbers.index(1)
index_7 = numbers.index(7)
index_8 = numbers.index(12)

number = int(input("Введите число из списка: "))

if number == 2:
    print("Число", number, "есть в списке под индексом", index_1)
elif number == 15:
    print("Число", number, "есть в списке под индексом", index_2)
elif number == 3:
    print("Число", number, "есть в списке под индексом", index_3)
elif number == 5:
    print("Число", number, "есть в списке под индексом", index_4)
elif number == 9:
    print("Число", number, "есть в списке под индексом", index_5)
elif number == 1:
    print("Число", number, "есть в списке под индексом", index_6)
elif number == 7:
    print("Число", number, "есть в списке под индексом", index_7)
elif number == 12:
    print("Число", number, "есть в списке под индексом", index_8)
else:
    print("Такого числа нет")