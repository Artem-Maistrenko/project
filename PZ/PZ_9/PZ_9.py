# Дан словарь на 6 персон, найти и вывести наибольшее и наименьшее
# значение роста (в см.). (Пример, {"Андрей": 178, "Виктор": 150, "Максим": 200, …},
# наибольшее 200, наименьшее 150)

people = {
    "Андрей": 178,
    "Виктор": 150,
    "Максим": 200,
    "Ольга": 165,
    "Елена": 172,
    "Дмитрий": 190
}

max_height = -float('inf')  
min_height = float('inf')   

for name, height in people.items():
    if height > max_height:
        max_height = height
    if height < min_height:
        min_height = height

print(f"Наибольшее: {max_height}, наименьшее: {min_height}")

