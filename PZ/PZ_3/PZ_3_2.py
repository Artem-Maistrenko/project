# Даны три числа. Найти среднее из них (то есть число, расположенное между
# наименьшим и наибольшим).

num1 = float(input("Введите первое число: "))
num2 = float(input("Введите второе число: "))
num3 = float(input("Введите третье число: "))

smallest = min(num1, num2, num3)
largest = max(num1, num2, num3)
average = (num1 + num2 + num3) - smallest - largest

print(f"число, расположенное между наименьшим и наибольшим: {average}")