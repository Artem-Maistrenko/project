# Даны три числа. Найти среднее из них (то есть число, расположенное между
# наименьшим и наибольшим).

# Обработка ввода чисел
try:
    num1 = float(input("Введите первое число: "))
    num2 = float(input("Введите второе число: "))
    num3 = float(input("Введите третье число: "))

    # Вычисление среднего числа
    smallest = min(num1, num2, num3)
    largest = max(num1, num2, num3)
    average = (num1 + num2 + num3) - smallest - largest

    # Вывод результата
    print(f"Число, расположенное между наименьшим и наибольшим: {average}")

# Обработка ошибок ввода
except ValueError as e:
    print("Ошибка")