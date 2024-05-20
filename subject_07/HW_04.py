"""
4. Сделать декоратор, который измеряет время,
затраченное на выполнение декорируемой функции.
"""

import time


def timeit(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Время выполнения функции {func.__name__}: {end_time - start_time} секунд")
        return result
    return wrapper


# Пример использования
@timeit
def example_function():
    time.sleep(1)  # имитация долгой работы
    print("Функция выполнена")


example_function()
