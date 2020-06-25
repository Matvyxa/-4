from functools import reduce


def func(el1, el2):
    return el1 * el2


new = [el for el in range(100, 1001, 2)]

print(f"list\n{new}\nПроизведения всех четных элементов списка: \n{reduce(func, new)}")
