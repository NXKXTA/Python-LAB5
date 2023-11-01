import re

str_line = input("Введите строку: ")  # Ввод строки

if not str_line:
    print("С пустой строкой ничего не сделаешь")
else:
    str_line = re.sub(r"^\s+", "", str_line)  # Убрать пробелы и табуляции в начале
    str_line = re.sub(r"\s+$", "", str_line)  # Убрать пробелы и табуляции в конце

    str_line = str_line.lower()  # Переводим символы всей строки в нижний регистр

    flag = re.search(r"[a-z]", str_line)  # Ищем буквы в нижнем регистре в диапазоне a-z
    if flag:
        str_line = re.sub(
            r"[a-z]", flag.group(0).upper(), str_line, 1
        )  # group(0) - Строка, которая соответствует всему шаблону. Первый символ ставим в верхний регистр

    flag = re.search(r"[.!?]$", str_line)  # Ищем на конце строки ".!?"
    if flag:
        str_line = re.sub(r"[.!?]+$", "", str_line)  # Меняем ".!?" на пустую строку

    str_line += "."  # В конец строки ставим точку

    print(
        f"Преобразованная строка выглядит так:\n{str_line}"
    )  # Вывод полученной строки
