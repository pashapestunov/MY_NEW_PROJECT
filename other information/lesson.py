
print("hi", 1, 4, sep="") # sep=""  убирает пробел, в скобках "" можем поствить что-то вместо пробела!

print("hi", 1, 4, end="") # end="" печатает этот принт с нижней стракой
print("hi")

print("hello \" wurld") # через \ мы используем кавычки как элеент строки

print("h\ne\nl\nl\no\n") # \n перекидывает далтнейшие значения на следующую строку

print("hel \t lo") # \t табуляция

print("hi \\ wr") # двойным \\ выводим один \

print(abs(-12)) # abs находит число по модулю(положительное)

print(pow(5, 3)) # pow возводи в степень как и (**)

print(round(5 / 3)) # round округляет деление в олижайшую сторону

number = 7
print(number)
del number # удаляет перенную, но, print сработает, так как удаление было после

boolean = True # Булевый тип данных (тру ор фолс)

"""
5 - integer (int)
4.32 - float 
hello - string (str)
False - bool
"""

num = 2.324
st = "hi"
num_2 = "5"
print(st, num)
print(st + str(num)) # изменив тип данных в переменной получилось соединить строку и число
print(st + str(num + int(num_2)))

data = input()
number = 5 if data == "five" else 0 # Тернарный оператор, принцип if - else но в сокращенном виде
print(number)

num = [1, 2, 3, 4, 5, 6, 7, 8, 9,]
num.reverse()   #Изменяет последовательность элементов на обратную


