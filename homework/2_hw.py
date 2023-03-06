"""3.	задача 1
a.	создайте функцию task_1(), в теле функции:
i.	создайте 5 разных переменных с произвольным названием.
ii.	у каждой укажите тип, типы следующие
1.	int, float, str, list, bool
iii.	заполните переменные произвольными значениями, с соответствующим для каждой типом
iv.	выведите тип данных каждой в консоль.
b.	в функцию добавьте аннотацию возвращаемых данных
c.	добавьте вызов функции.

4.	задача 2
a.	создайте функцию task_2(), в теле функции:
i.	есть список a = [1, 2, 3, 5, 8, 13, 21]
ii.	выведите в консоль первые 3 значения списка
b.	в функцию добавьте аннотацию возвращаемых данных
c.	добавьте вызов функции.
d.	* - скажите как называется эта последовательность чисел

5.	задача 3
a.	напишите функцию task_3(), которая принимает число и возвращает квадрат этого числа.
b.	пропишите аннотации для функции и аргумента
c.	распечатайте в консоль вызов функции
"""

import random
import string


def task_1():
    a: int = int(random.getrandbits(64))
    b: float = float(random.getrandbits(64))
    c: str = ''.join(random.choice(string.ascii_letters) for cnt in range(random.randint(1, 50)))
    d: list = [random.randint(1, 100) for cnt in range(random.randint(1, 50))]
    e: bool = bool(random.getrandbits(1))

    print(type(a), type(b), type(c), type(d), type(e), sep='\n')
    print (a, b, c, d, e, sep='\n')


task_1()