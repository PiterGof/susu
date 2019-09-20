"""
Обратный слэш используется для экранирования одинарных или двойных кавычек, 
например 'It\'s me' или "She said \"Hello\"". 
Специальный символ \n используется для перевода курсора на новую строку.
Одинарная кавычка может использоваться в двойных кавычках без экранирования и наоборот.
"""

dont_worry = "Don't worry about apostrophes"

print(dont_worry)

print("\"Sweet\" is an ice-cream")

print('text')

# Выведите в консоль следующий текст с помощью одной строки: The name of this ice-cream is "Sweet'n'Tasty"
print('The name of this ice-cream is "Sweet\'n\'Tasty"')


# Существует множество полезных методов для работы со строками. 
# Вы можете использовать функцию lower() для преобразования всех прописных символов в строке в строчные
# Функция upper() используется для перевода всех строчных символов в строке в прописные
# Чтобы использовать любой строковый метод, поставьте точку в конце строки (или переменной, содержащей строку) и введите название метода после точки, например "John".upper()
# В PyCharm Вы можете изучить все доступные строковые методы используя сочетание клавиш Ctrl+Space после точки

monty_python = "Monty Python"

print(monty_python)

print(monty_python.lower()) 	# Обратите внимание на результат применения метода lower()

# Выведите в консоль строку в верхнем регистре
print(monty_python.upper())
# Оператор %, напечатанный после строки, используется для объединения строки с переменными.
# Оператор % заменит %s в строке строковой переменной, идущей за оператором %.
# Специальный символ %d используется в качестве зарезервированного места в строке для переменной, имеющей числовое или десятичное значение.

name = "John"
print("Hello, PyCharm! My name is %s!" % name) 	# Обратите внимание, что %s расположено внутри строки, а символ % расположен после строки
years = 23
print("I'm %d years old" % years) 		# Выведите в консоль свой возраст