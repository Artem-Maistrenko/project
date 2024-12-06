# Составить программу, в которой функция генерирует четырехзначное число и
# определяет, есть ли в числе одинаковые цифры.
import random


def check_duplicates_in_number():
    try:
        # Генерация случайного четырёхзначного числа
        number = random.randint(1000, 9999)

        # Извлекаем цифры числа
        digits = [number // 1000, (number // 100) % 10, (number // 10) % 10, number % 10]

        # Проверяем, есть ли одинаковые цифры
        for i in range(4):
            for j in range(i + 1, 4):
                if digits[i] == digits[j]:
                    return number, True  # Одинаковые цифры есть

        return number, False  # Одинаковых цифр нет

    except Exception as e:
        return f"Произошла ошибка: {e}"

# Пример вызова функции
number, has_duplicates = check_duplicates_in_number()
print(f"Сгенерированное число: {number}")
print(f"Есть одинаковые цифры: {has_duplicates}")

