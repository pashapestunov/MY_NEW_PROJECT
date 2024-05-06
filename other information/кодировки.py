import string

print(string.ascii_letters)     # все англ буквы в верхнем и нижнем регистре
print(string.digits)            # все цифры
print(string.punctuation)       # все знаки из списка

some_string = 'привет'
in_code = some_string.encode()  # по стандарту в скобках ('utf-8)
print(in_code)

uncode = in_code.decode()
print(uncode)

"""
Декодирование байтовых данных в строки лучше
производить сразу после их получения, а кодирование в
байты – только перед отправкой. В коде лучше работать с
привычными типами данных, а не с байтами
"""

"""
decode(),
encode() кодируют/декодируют строку в нужной кодировке

ascii() представляет строку в формате ASCII. Все не-ascii символы будут экранированы

chr() позволяет увидеть юникод символ, соответствующий введённому числовому значению

ord() позволяет увидеть соответствующее введённому символу число

"""

print(ascii("cat"))
print(ascii("кошка"))
print(bytes("python", "utf-16"))
print(bytes("python", "utf-32"))
print(chr(63))
print(ord("?"))