"""Замена имён в судебном решении. Написать программу, которая заменит в тексте ФИО подсудимого на N.
Каждое слово в ФИО начинается с заглавной буквы, фамилия может быть двойная."""

import re

text = """Подсудимая Эверт-Колокольцева Елизавета Александровна в судебном заседании вину инкриминируемого 
правонарушения признала в полном объёме и суду показала, что 14 сентября 1876 года, будучи в состоянии алкогольного
опьянения от безысходности, в связи с состоянием здоровья позвонила со своего стационарного телефона в полицию,
сообщив о том, что у неё в квартире якобы заложена бомба. После чего приехали сотрудники полиции, скорая
и пожарные, которым она сообщила, что бомба — это она"""

pattern = r"([А-ЯЁ][а-яё]+(?:-[А-ЯЁ][а-яё]+)?)\s+([А-ЯЁ][а-яё]+)\s+([А-ЯЁ][а-яё]+)"
pattern1 = re.findall(pattern, text)
change = "Пестунов-Пестунов Павел Олегович"
result = f"Подсудимая"
result2 = re.match(result, text)
change2 = "Подcудимый"

new_text = re.sub(pattern, change, text)
next = re.sub(result, change2, new_text)

print(next)

