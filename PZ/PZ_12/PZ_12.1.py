# В последовательности на n целых элементов найти произведение элементов 
# средней трети. 
from functools import reduce
from operator import mul


def product_of_middle_third(arr):
    n = len(arr)
    third = n // 3
    start = third
    end = 2 * third if n % 3 == 0 else n - third

    middle_part = arr[start:end]
    return reduce(mul, middle_part, 1)  # 1 — начальное значение для умножения

sequence = [1, 2, 3, 4, 5, 6, 7]
result = product_of_middle_third(sequence)
print(result)
