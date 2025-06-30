def average_last_two_columns(matrix):
    # Получаем последние два столбца для каждой строки
    last_two_columns = [row[-2:] for row in matrix]
    
    # Преобразуем в плоский список всех элементов последних двух столбцов
    flattened = [item for sublist in last_two_columns for item in sublist]
    
    # Вычисляем среднее арифметическое
    return sum(flattened) / len(flattened) if flattened else 0

# Пример использования:
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

result = average_last_two_columns(matrix)
print(result)  # Выведет: (2+3+5+6+8+9)/6 = 33/6 = 5.5
