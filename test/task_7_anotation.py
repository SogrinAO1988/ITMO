a: int = 5
b: str = 'строка'
c: list = [1, 2]

def indent(s: str, width: int) -> str:
    return " " * (max(0, width - len(s))) + s

print(indent('123', 123))

def zxc(s: str='') -> int:
    return len(s)
print(zxc())


def add2(my_list: list) -> int:
    result = 0
    for elem in my_list:
        result = result + elem
        return result
print(add2([1, 2, 3]))

