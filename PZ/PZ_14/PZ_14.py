# Из исходного текстового файла (expansion.txt) выбрать имена файлов,
# соответствующие типам: .xls, .xml, .html, .css, .py. Посчитать количество полученных
# элементов.
import re

with open('expansion.txt', 'r') as file:
    content = file.read()

pattern = r'\b\w+\.(?:xls|xml|html|css|py)\b'
matches = re.findall(pattern, content, flags=re.IGNORECASE)

count = len(matches)

print("Найденные файлы:", matches)
print("Количество файлов:", count)