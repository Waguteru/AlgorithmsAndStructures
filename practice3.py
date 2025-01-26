def is_leap_year(year):
    # Проверяем, является ли год високосным по правилам григорианского календаря
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return "Да"  # Год високосный
    else:
        return "Нет"  # Год не високосный

# Считываем входные данные
year = int(input())

# Выводим результат
print(is_leap_year(year))