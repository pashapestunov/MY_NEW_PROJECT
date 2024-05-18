class Pizza:
    def __init__(self, ingredients):
        self.ingreditnts = ingredients

    def __str__(self):
        return f'Pizza with {self.ingreditnts}'

    @classmethod
    def margherita(cls):
        return cls(['tomats', 'mocharella'])

    @classmethod
    def meetpizza(cls):
        return cls(['tomats', 'mocharella', 'ham'])


print(Pizza.margherita())
print(Pizza.meetpizza())
print()


class Employee:
    dept = 'Information technology'

    def __init__(self, name, id):
        self.name = name
        self.id = id


emp1 = Employee('Pasha', 'E105')
emp2 = Employee('Tanya', 'E101')

print(emp1.dept, end=':')
print(emp1.name, end='-')
print(emp1.id)
print(emp2.dept, end=': ')
print(emp2.name, end='-')
print(emp2.id)
Employee.dept = 'Hello'
print(emp1.dept, end=': ')
print(emp1.name, end='-')
print(emp1.id)
emp1.dept = 'You are Free'
print(emp1.dept, end=': ')
print(emp1.name, end='-')
print(emp1.id)
print(emp2.dept, end=': ')
print(emp2.name, end='-')
print(emp2.id)
print()


class Calculator:
    @staticmethod
    def sum(a, b):
        return a + b

    @staticmethod
    def sub(a, b):
        return a - b

    @staticmethod
    def mul(a, b):
        return a * b

    @staticmethod
    def div(a, b):
        return a / b


cal = Calculator
print('Enter your two numbers')
x = int(input())
y = int(input())

print(f'Sum of two numbers entered {x} + {y} =', cal.sum(x, y))
print(f'Difference  of two numbers entered {x} - {y} =', cal.sub(x, y))
print(f'Multiplication  of two numbers entered {x} * {y} =', cal.mul(x, y))
print(f'Diversion  of two numbers entered {x} / {y} =', cal.div(x, y))
print()

from dataclasses import dataclass

@dataclass(order=True)
class Comparete:
    height: float
    width: float


bell_1 = Comparete(height=50.5, width=7.5)
bell_2 = Comparete(height=50.5, width=8.0)
bell_3 = Comparete(height=60.0, width=10.0)

print('Is bell_1 less then bell_2', bell_1 < bell_2)
print('Is bell_2 less then bell_3', bell_2 < bell_3)



@dataclass(frozen=True)
class UmutableBell:
    meel: float
    weel: float


umun = UmutableBell(20, 5)
#umun.weel = 8   # frozer не даст изменить данные


@dataclass
class Base:
    hugo: float

@dataclass
class Boss(Base):
    wogo: float


answer = Boss(hugo=20, wogo=5)


from dataclasses import dataclass, field

@dataclass
class CorrectBill:
    costs_by_dish: list = field(default_factory=list)


bil0 = CorrectBill()
bil0.costs_by_dish.append(5)
bil1 = CorrectBill()
bil1.costs_by_dish.append(7)

print('Bil 0 costs:', bil0.costs_by_dish)
print('Bil 1 costs:', bil1.costs_by_dish)

bil0.costs_by_dish is bil1.costs_by_dish
print()


@dataclass
class Book:
    title: str
    author: str
    desc: str = None

    def __post_init__(self):
        self.desc = self.desc or f"'{self.title}' by {self.author}"


print(Book("Fareneshit 481", "Bradbyre",))
print(Book("Fareneshit 481", "Bradbyre", "desk i make"))
print()


class English:
    def greeting(self):
        print('Hello')


class French:
    def greeting(self):
        print('Bonju')


def intro(language):
        language.greeting()


john = English()
grek = French()

intro(john)
intro(grek)
print()


class Item:
    def __init__(self, arg):
        self.arg = arg

    def __str__(self):
        return str(self.arg)


class Container:
    def __init__(self, *args):
        self.items_list = list()

        for i in args:
            self.items_list.append(Item(i))

    def __getitem__(self, i):
        return self.items_list[i]


group = Container(5, 10, 'abc')
print(group.items_list[1])
print(group[0])
print(group[2])
print()


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f'({self.x}, {self.y})'

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Point(x, y)


pi_1 = Point(2, 4)
pi_2 = Point(4, 4)
print(pi_1 + pi_2)


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f'({self.x}, {self.y})'

    def __lt__(self, other):
        first = (self.x ** 2) + (self.y ** 2)
        second = (other.x ** 2) + (other.y ** 2)
        return first < second


pi_1 = Point(1, 1)
pi_2 = Point(-2, -3)
pi_3 = Point(1, -1)
print(pi_1 < pi_2)
print(pi_2 < pi_3)
print(pi_1 < pi_3)
print()


def choose_class(name):
    if name == 'foo':
        class Foo(object):
            pass
        return Foo
    else:
        class Bar(object):
            pass
        return Bar


some_class = choose_class('foo')
print(some_class)
print(some_class())
print()


def upper_attr(future_class_name, future_class_parents, future_class_attr):
    """
    Return a class object, with the list of its attribute turned into uppercase.
    """

    uppercase_attr = {}
    for name, val in future_class_attr.item():
        if not name.startwith('__'):
            uppercase_attr[name.upper()] = val
        else:
            uppercase_attr[name] = val

        return type(future_class_name, future_class_parents, future_class_attr)


__metaclass__ = upper_attr


class Foo():
    bar = 'bip'


print(hasattr(Foo, 'bar'))
print(hasattr(Foo, 'BAR'))

f = Foo()
#print(f.BAR)
print()


class UpperAttrMetaclass(type):

    def __new__(cls, clsname, bases, dct):

        uppercase_attr = {}
        for name, val in dct.items():
            if not name.startswiith('__'):
                uppercase_attr[name.upper()] = val
            else:
                uppercase_attr[name] = val

        return super(UpperAttrMetaclass, cls).__new__(cls, clsname, bases, uppercase_attr)


class MyException(Exception):   #создание собственных исключений
    pass


class HostNotFound(Exception):
    def __init__(self, host):
        self.host = host
        Exception.__init__(self, f'Host not found exception: missing {host}')


try:
    raise HostNotFound('tariover.net')
except HostNotFound as exc:
    print(exc)
    print(exc.host)
    print()