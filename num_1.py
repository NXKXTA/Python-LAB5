import re

while True:
    str_line = input("Введите строку: ")  # Ввод строки

    if not str_line:
        print("Конец программы")
        break
    else:
        if re.match(
                r"[^\\<>/|?*\"]+\.(txt$|doc$|docx$|odt$|rtf$)", str_line
                # Проверяем не присутствуют ли в файле символы <>/|?*\
        ):  # Заканчивается ли в файл расширением
            print(str_line, " - является названием файла")
        else:
            print(str_line, " - не является названием файла")
