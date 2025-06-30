def multiply_threes(nested_list):
    return [list(map(lambda x: x * 3 if x % 3 == 0 else x, sublist)) 
            for sublist in nested_list]

# Пример использования:
original_list = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

result = multiply_threes(original_list)
print(result)
