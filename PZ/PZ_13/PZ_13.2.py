# В двумерном списке найти среднее арифметическое элементов последних двух 
# столбцов.
def average_last_two_columns(matrix):
    
    last_two_columns = [row[-2:] for row in matrix]
    
    flattened = [item for sublist in last_two_columns for item in sublist]
    
    return sum(flattened) / len(flattened) if flattened else 0

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

result = average_last_two_columns(matrix)
print(result) 
