import re

while True:
    str_line = input("Введите строку: ")

    if not str_line:
        print("Конец программы")
        break
    else:
        if re.match(r"[^\\<>/|?*\"]+\.(txt|doc|docx|odt|rtf)", str_line):
            print(str_line, " - является названием файла")
        else:
            print(str_line, " - не является названием файла")
