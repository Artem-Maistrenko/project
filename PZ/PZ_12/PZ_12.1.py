# В последовательности на n целых элементов найти произведение элементов 
# средней трети. 
from math import prod
from typing import List

def middle_third_product(arr: List[int]) -> int:
    n = len(arr)
    third = n // 3
    start = (n - third) // 2 
    middle = arr[start : start + third]
    return prod(middle)  

print(middle_third_product([1, 2, 3, 4, 5, 6, 7, 8, 9]))  
print(middle_third_product([1, 2, 3, 4, 5, 6, 7]))        
