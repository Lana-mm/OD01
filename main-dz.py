#Алгоритм палиндром
# 1. Получить строку
# (строка передается в функцию как аргумент s)
# 2. Удалить пробелы и знаки препинания.
# 3. Привести к одному регистру
# 4. Развернуть строку
# 5. Сравнить строки
# 6. Вернуть результат

import math


def is_palindrome(s):
    # 1. Получить строку (строка передается в функцию как аргумент s)

    # 2. Удалить пробелы и знаки препинания
    s_cleaned = ''.join(char for char in s if char.isalnum())

    # 3. Привести к одному регистру
    s_cleaned = s_cleaned.lower()

    # 4. Развернуть строку
    s_reversed = s_cleaned[::-1]

    # 5. Сравнить строки
    # Сравниваем символы с помощью математической операции
    is_palindrome = math.isclose(sum(1 for a, b in zip(s_cleaned, s_reversed) if a == b), len(s_cleaned))

    # 6. Вернуть результат
    return is_palindrome


# Примеры использования
print(is_palindrome("A man, a plan, a canal: Panama"))  # True
print(is_palindrome("race a car"))  # False