import re

str_line = input("Введите строку: ")

if not str_line:
    print("С пустой строкой ничего не сделаешь")
else:
    str_line = re.sub(r"^\s+", "", str_line)
    str_line = re.sub(r"\s+$", "", str_line)

    str_line = str_line.lower()

    flag = re.search(r"[a-z]", str_line)
    if flag:
        str_line = re.sub(r"[a-z]", flag.group(0).upper(), str_line, 1)

    flag = re.search(r"[.!?]$", str_line)
    if flag:
        str_line = re.sub(r"[.!?]+$", "", str_line)

    str_line += "."

    print(f"Преобразованная строка выглядит так:\n{str_line}")
