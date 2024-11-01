def transform_number(number):
    if not (100 <= number < 1000):
        raise ValueError("Ввод должен быть трёхзначным числом.")
    return (number % 100) * 10 + number // 100

def main():
    try:
        user_input = int(input("Введите трехзначное число: "))
        result = transform_number(user_input)
        print(f"Преобразованное число: {result}")
    except ValueError as e:
        print(f"Ошибка: {e}")

if __name__ == "__main__":
    main()
