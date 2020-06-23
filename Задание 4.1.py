from sys import argv

[scr_name, vb_hour, st_hour, premia] = argv
print("Имя скрипта:", scr_name)
print("Выборка в часах:", vb_hour)
print("Ставка в час:", st_hour)
print("Премия:", premia)
zarplata = (int(vb_hour) * int(st_hour)) + int(premia)
print("Зарплата:", zarplata)
