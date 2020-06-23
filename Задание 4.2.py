spisok = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
for i in range(len(spisok) - 1):
    a = [spisok[i]]
    i += 1
    b = [spisok[i]]
    if b > a:
        a = b
        print(b, end="")
