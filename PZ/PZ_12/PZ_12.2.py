# Составить генератор (yield), который преобразует все буквенные символы в 
# заглавные
def uppercase_generator(iterable):
    for char in iterable:
        yield char.upper() if char.isalpha() else char

text = "Hello, World! 123"
gen = uppercase_generator(text)
print(list(gen))  
