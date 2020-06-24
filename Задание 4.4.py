zadanie = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
reshenie = [el for el in zadanie if zadanie.count(el) < 2]
print(reshenie)