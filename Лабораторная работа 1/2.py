# TODO Найдите количество книг, которое можно разместить на дискете

load = 1.44*pow(2, 20)
pages = 100
rows = 50
syms_per_row = 25
sym = 4

one_book = sym*syms_per_row*rows*pages

quantity = int(load//one_book)

print("Количество книг, помещающихся на дискету:", quantity)
