import random


def create_initial_file(filename, count):
    with open(filename, 'w', encoding='utf-8') as file:
        numbers = [random.randint(-100, 100) for _ in range(count)]
        file.write(' '.join(map(str, numbers)))


def process_data(input_filename, output_filename):
    with open(input_filename, 'r', encoding='utf-8') as file:
        numbers = list(map(int, file.read().split()))

    count = len(numbers)
    average = sum(numbers) / count if count > 0 else 0

    new_sequence = []
    for i in range(len(numbers)):
        if i == 0:  # Первый элемент
            new_val = (numbers[i] + numbers[i + 1]) ** 2
        elif i == len(numbers) - 1:  # Последний элемент
            new_val = (numbers[i - 1] + numbers[i]) ** 2
        else:  # Средние элементы
            new_val = (numbers[i - 1] + numbers[i + 1]) ** 2
        new_sequence.append(new_val)

    with open(output_filename, 'w', encoding='utf-8') as file:
        file.write(f"Исходные данные: {' '.join(map(str, numbers))}\n")
        file.write(f"Количество элементов: {count}\n")
        file.write(f"Среднее арифметическое элементов: {average:.2f}\n")
        file.write("Последовательность (квадрат суммы соседей):\n")
        file.write(' '.join(map(str, new_sequence)) + '\n')

if __name__ == "__main__":
    input_file = "input_numbers.txt"
    output_file = "processed_numbers.txt"

    create_initial_file(input_file, 10)

    process_data(input_file, output_file)

    print(f"Файл '{input_file}' создан.")
    print(f"Результат сохранён в '{output_file}'.")