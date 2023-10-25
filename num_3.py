import re

s1 = input("введите строку 1: ")
s2 = input("введите строку 2: ")

flag = re.findall(s2, s1)

if not flag:
    print("Вхождений нет")
else:
    result = re.sub(s2, "", s1, len(flag) - 1)
    print(f"Ваша измененная строка выглядит так: {result}")
