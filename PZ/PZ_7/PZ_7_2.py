# Дана строка, состоящая из русских слов, разделенных пробелами (одним или несколькими).
# Вывести строку, содержащую эти же слова, разделенные одним пробелом и расположенные в обратном порядке.

input_s = "ТРАМВАЙ   САМОЛЁТ   ВЕЛОСИПЕД   АВТОМОБИЛЬ"
words = input_s.split()
words_sort = sorted(words) # Сортировка слов в алфавитном порядке
output_s = ' '.join(words_sort) # Объединение слов с одним пробелом между ними
print(output_s)
