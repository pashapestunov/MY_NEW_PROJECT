

def find_imt(width, height):
    index = width / ((height / 100) ** 2)
    return index


def how_ind(find_imt):
    if find_imt <= 20:
        return "Вы очень худой"
    elif 20 <= find_imt <= 30:
        return "Вы стройный"
    elif 30 <= find_imt <= 40:
        return "Вам нужно немного скинуть"
    else:
        return "Таких данных не может быть или у вас большие проблемы!"


try:
    width = float(input('Введите вес в кг: '))
    height = int(input('Введите рост в см: '))
    if width == 0 or height == 0:
        raise ZeroDivisionError
    ind = find_imt(width, height)
    result = how_ind(ind)

    print(f'Ваш индекс массы тила: {ind:.2f}')
    print(f'итерация: {result}')
except ValueError as e:
    print('Сведение об ошибке ', e)
except ZeroDivisionError as z:
    print('0 is not correct', z)