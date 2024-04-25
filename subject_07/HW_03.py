"""
3.Дан список строк. С помощью filter() получить список
тех строк из исходного списка, которые являются
палиндромами (читаются в обе стороны одинаково, например,
’abcсba’)
"""

some_list = ["ada", "sdds", "abccba", "sfsd"]

result = (list(filter(lambda x: x == x[::-1], some_list)))
print(result)