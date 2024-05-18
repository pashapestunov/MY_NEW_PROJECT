class Person:
    def say(self, message):
        print(message)

    def say_hello(self):
        self.say('Hello work')


tom = Person()
tom.say_hello()
print()


class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def funsun_my(self):
        print(f'name: {self.name} age: {self.age}')


tom = Person(name='tom', age=12)
tom.funsun_my()

pavel = Person(name='pasha', age=26)
pavel.funsun_my()
print('')


class Car:
    car_count = 0

    def __init__(self, name, make, model):
        self.name = name
        self.make = make
        self.model = model
        Car.car_count += 1

    def start(self):
        print('Двигатель заведен.')


car_a = Car(model='camry', name='toyota', make=2007)
car_a.start()
print(car_a.name)
print(car_a.car_count)

car_b = Car(model='civic', name='honda', make=2012)
car_b.start()
print(car_b.name)
print(car_b.car_count)
print('')


class SomeClass(object):

    def __new__(cls):
        print('new')
        return super(SomeClass, cls).__new__(cls)

    def __init__(self):
        print('init')


obj = SomeClass()
print('')


class SomeClass(object):

    def __init__(self, name):
        self.name = name
        print(f'проинициализирован объект {self.name} класса SomeClass')

    def __del__(self):
        print(f'удаляется объект {self.name} класса SomeClass')


obj = SomeClass('John')
del obj
print()


class Multiplier:

    def __call__(self, x, y):
        return x * y


myltiply = Multiplier()
print(myltiply(19, 19))
print(myltiply.__call__(10, 19))  # the same
print()


class SomeClass:

    def __init__(self, value):
        self.value = value

    def __mul__(self, number):
        return self.value * number


obj = SomeClass(42)
num = 100
print(obj * num)
print()


class Computer:
    def __init__(self):
        self.__price = 900

    def get_price(self):
        print(f'Цена продажи {self.__price}')

    def set_price(self, price):
        self.__price = price


c = Computer()
c.get_price()

c.set_price(1000)
c.get_price()
print()


class Figure:

    def __init__(self, height=2, width=2):
        self.__height = height
        self.__width = width

    def get_height(self):
        return self.__height

    def set_height(self, height):
        if height >= 0:
            self.__height = height
            print(f"Вы ввели {self.__height}")
        else:
            raise Exception("Value can't be < 0")

    def get_width(self):
        return self.__width

    def set_width(self, width):
        if width >= 0:
            self.__width = width
            print(f"Вы ввели {self.__width}")
        else:
            raise Exception("Value can't be <0")


square = Figure()
square.__height = 3
square.set_height(5)
square.set_width(6)
print()


class Mine():

    def __init__(self):
        self._x = None

    def get_x(self):
        return self._x

    def set_x(self, value):
        self._x = value

    def del_x(self):
        self._x = 'No more'

    x = property(get_x, set_x, del_x, 'property x')


print(type(Mine.x))
mine = Mine()
print(mine.x)
mine.x = 3
print(mine.x)

del mine.x
print(mine.x)
print()


class Mine():

    def __init__(self):
        self._x = 'some value'

    @property
    def prop(self):
        return self._x


mine = Mine()
print(mine.prop)
#mine.prop = 'other value'
#del mine.prop
print()


class Persson:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        print('Gatting name')
        return self._name

    @name.setter
    def name(self, value):
        print('Setting name to ' + value)
        self._name = value

    @name.deleter
    def name(self):
        print('Deleting name')
        del self._name


p = Persson('Adam')
print('The name is', p.name)
p.name = 'John'
del p.name
print()


class Bird:
    def __init__(self):
        print('Птица готова')

    def who_is_this(self):
        print('Птица')

    def swim(self):
        print('Плывет быстрее')


class Penguin(Bird):
    def __init__(self):
        super().__init__()   # обращаемся к классу-родителю(class Bird)
        print('Пингвин готов')

    def who_is_this(self):
        print('Пингвин')

    def run(self):
        print('Бежит быстрее')


peggy = Penguin()
peggy.who_is_this()
peggy.swim()
peggy.run()
print()


from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius


class Rectangle(Shape):
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def area(self):
        return self.height * self.width


circle = Circle(5)
rectangle = Rectangle(4, 6)

print('Прощадь круга', circle.area())
print('Прощадь прямоугольник', rectangle.area())
print()


class Parent1:
    def method1(self):
        print('Метод из Parent1')


class Parent2:
    def method2(self):
        print('Метод из Paernt2')


class Child(Parent1, Parent2):
    def child_method(self):
        print('Использует из Child')

child = Child()

child.method1()
child.method2()
child.child_method()
print()


class Parent:
    def earn_money(self):
        print('Родитель зарабатывает')


class Child(Parent):
    def play(self):
        print('Редёнок играет')


child = Child()
child.play()
child.earn_money()
print()
print(Parent.mro())  # Показывает иерархию классов, от последнего до класса-подителя по-порядку

