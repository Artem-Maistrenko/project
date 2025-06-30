# в двумерном списке элементы кратные 3 увеличить в 3 раза
def multiply_threes(nested_list):
    return [list(map(lambda x: x * 3 if x % 3 == 0 else x, sublist)) 
            for sublist in nested_list]

original_list = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

result = multiply_threes(original_list)
print(result)
