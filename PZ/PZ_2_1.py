def transform_number(number):
    """
    Функция принимает трехзначное число,
    зачёркивает первую цифру и приписывает её справа.

    :param number: трёхзначное целое число
    :return: преобразованное число
    """
    # Преобразуем число в строку для работы с цифрами
    number_str = str(number)

    # Проверяем, что число является трехзначным
    if len(number_str) != 3 or not number_str.isdigit():
        raise ValueError("Ввод должен быть трёхзначным числом.")

    # Извлекаем первую цифру и оставшиеся две
    first_digit = number_str[0]
    remaining_digits = number_str[1:]

    # Формируем новое число
    new_number_str = remaining_digits + first_digit

    return int(new_number_str)


def main():
    try:
        # Запрашиваем у пользователя ввод трёхзначного числа
        user_input = int(input("Введите трехзначное число: "))

        # Вызываем функцию для преобразования числа
        result = transform_number(user_input)

        # Выводим результат
        print(f"Преобразованное число: {result}")

    except ValueError as e:
        print(f"Ошибка: {e}")


if __name__ == "__main__":
    main()

