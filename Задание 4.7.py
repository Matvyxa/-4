def fact_n(nom):
    f_num = 1
    for i in range(1, nom):
        f_num *= i
        yield f_num


for i in fact_n(24):
    print(i)


