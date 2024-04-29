import re

some_text = "суд приговорил суд"
result = re.match(r"суд", some_text)   #метод "match" ищет только в начале строки
result.group(0)
print(result)

some_text_2 = "суд приговорил суд"
result_2 = re.search(r"приговор", some_text_2)   #метод "search" ищет по всей срочке, но, до первого совпаденя
result_2.group(0)
print(result_2)

some_text_3 = "суд приговорил суд"
result_3 = re.findall(r"суд", some_text_3)   #метод "findall" ищет все совпаденя
print(result_3)

                              # Операторы регулярных выражений
some_text_4 = "2 судья номер 2 Иванова"
pattern = r"\w"      # оператор \w находит любую цифру или букву
find_pattern = re.findall(pattern, some_text_4)
print(find_pattern)

some_text_5 = "2 судья номер 2 Иванова АА.А. вчера вынес обвинительный приговор"
pattern_5 = r"[А-ЯЁа-яё]+\s[А-ЯЁа-яё]{2}\.\s*[А-ЯЁа-яё]{1}\." # оператор \w+ находит слова целком
find_pattern_5 = re.findall(pattern_5, some_text_5)        # \s любой пробельный символ "\s*" * говорит о том, что
print(find_pattern_5)                                      # пробела может и не быть
                                                           # [А-ЯЁа-яё] показывает, что там нужны только буквы
                                                           # {1} сколько раз должен исполькозатся паттерн
                                                           # \. показывает, что после инициалаа у нас точка, \ нужен для
                                                           # того, что-то показать, что это не оператор, а точка

"""
(.+) какие-то симолы
месяц*\w+ - говорит о том, что окончание может изменяться
"""
s = "назначить наказание в виде лишения сободы сроком 10 (десять) лет  и 6 (шесть) месяцев"
pattern = r"сроком(.+)(лет)*((.+)месяц*\w+)*"
find = re.search(pattern, s)
print(find)


def find_prison_term(text):
    return re.sub("сроком", '', re.search(r"сроком*\s(.+)\s*(лет)*((.+)месяц*\w+)*",
                                                                                text)[0]).strip()

some_text = "назначить наказание в виде лишения сободы сроком 10 (десять) лет  и 6 (шесть) месяцев"
result = find_prison_term(some_text)
print(result)

mail = "Напишите мне на почту pestunov.pasha9999@gmai.com"

pattern = r"(([a-z0-9._%-]+)@([a-z0-9._-]+\.[a-z]{2,}))"

find_pat = re.search(pattern, mail)

print(find_pat)




