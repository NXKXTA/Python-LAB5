import re

s = input("Введите строку: ")

flag = re.match(r"[a-zA-Z]{2}\d{3}[a-zA-Z]", s)

if flag:
    print(f"Строку {s} можно считать номером автомобиля")
else:
    print(f"Строка {s} не является номером автомобиля")
