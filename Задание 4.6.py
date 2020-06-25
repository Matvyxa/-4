from itertools import islice, cycle, count


def func(str_el, st_el, num_str):
    try:
        str_el, st_el, num_str = int(str_el), int(st_el), int(num_str)
        st_list = [el for el in islice(count(), str_el, st_el + 1)]
        new_list = iter(el for el in cycle(st_list))
        repeat_list = [next(new_list) for _ in range(num_str)]
        print(st_list)
        return repeat_list
    except IOError:
        return "IOError"


print(func(input("Ввведите стартовое значение: "), input("Введите значение до:"), input("Введите номер до: ")))
