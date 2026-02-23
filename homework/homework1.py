# Уровень 1.1
length = input("Введите длинну: ")
length = int(length)
width = input("Введите ширину: ")
width = int(width)
area = length * width
perimeter = 2 * (length + width)
print("Площадь прямоугольника:", area)
print("Периметр прямоугольника:", perimeter)

# Уровень 1.2
Celsius = input("Введите температуру в Цельсиях: ")
Celsius = int(Celsius)
Fahrenheit = (Celsius * 9 / 5) + 32
print("Температура в Фаренгейтах:", Fahrenheit)
Fahrenheit = input("Введите температуру в Фаренгейтах: ")
Fahrenheit = int(Fahrenheit)
Celsius = (Fahrenheit - 32) * 5 / 9
print("Температура в Цельсия:", Celsius)

# Уровень 1.3
birth = input("Введите год рождения: ")
birth = int(birth)
age = 2026 - birth
print("Ваш возраст:", age)

# Уровень 2.1
x = int(input("Введите число: "))
if x % 2 == 0:
    print(x, "- четное число")
else:
    print(x, "- нечетное число")

# Уровень 2.2
year = int(input("Введите год: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("year, год - високосный")
else:
    print("year, год - не високосный")

# Уровень 2.3
number = int(input("Введите числовую оценку: "))
if number >= 90:
    print(number, "- A")
elif number >= 75:
    print(number, "- B")
elif number >= 60:
    print(number, "- C")
elif number >= 50:
    print(number, "- D")
else:
    print(number, "- F")

# Уровень 3.1
n = int(input("Введите число: "))
for x in range(1, 11):
    print(n, "*", x, "=", n * x)

# Уровень 3.2
n = int(input("Введите число: "))
total = 0
for x in range(1, n + 1):
    total += x
print(f"Сумма чисел от 1 до {n} = {total}")
print(f"Среднее арифметическое {total / n}")

# Уровень 3.3
def factorial(n):
    if n < 0:
        return "Ошибка! Факториал из отрицательного числа не определяется"
    if n == 0:
        return 1
    resultat = 1
    for i in range(1, n + 1):
        resultat *= i
    return resultat
n = int(input("Введите число для вычисления факториала: "))
print(factorial(n))

# Уровень 3.4
def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b
n = int(input("Введите количество чисел N: "))
fibonacci(n)

# Уровень 4.1
import random
numbers = []
for _ in range(10):
    numbers.append(random.randint(1, 1000))
print(f"Сгенерированный список: {numbers}")
maximum = numbers[0]  # Предполагаем, что первый элемент - максимальный
minimum = numbers[0]  # Предполагаем, что первый элемент - минимальный
for num in numbers:
    if num > maximum:
        maximum = num
    if num < minimum:
        minimum = num
print(f"Максимальное значение: {maximum}")
print(f"Минимальное значение: {minimum}")

# Уровень 4.2
my_list = [1, 12, 33, 44, 54, 76, 87, 98, 99, 106]
print(f"Исходный список: {my_list}")
left = 0
right = len(my_list) - 1
while left < right:
    temp = my_list[left]
    my_list[left] = my_list[right]
    my_list[right] = temp
    left += 1
    right -= 1
print(f"Перевернутый список: {my_list}")

# Уровень 4.3
numbers = [1, 12, 33, 44, 54, 76, 87, 99, 99, 106]
print(f"Исходный список: {numbers}")
unique_set = set(numbers) # Преобразуем в множество (автоматически удаляет дубликаты)
unique_numbers = list(unique_set) # Преобразуем обратно в список
print(f"После удаления дубликатов: {unique_numbers}")
print(f"Количество уникальных элементов: {len(unique_numbers)}")

# Уровень 5.1
text = input("Введите строку: ")
vowels = "аеёиоуыэюяaeiouyАЕЁИОУЫЭЮЯAEIOUY"
consonants = "бвгджзйклмнпрстфхцчшщbcdfghjklmnpqrstvwxzБВГДЖЗЙКЛМНПРСТФХЦЧШЩBCDFGHJKLMNPQRSTVWXZ"
v = 0  # счетчик гласных
c = 0  # счетчик согласных
# Перебираем каждый символ
for char in text:
    if char in vowels:
        v += 1
    elif char in consonants:
        c += 1
print(f"Гласных: {v}")
print(f"Согласных: {c}")

# Уровень 5.2
word = input("Введите слово для проверки: ")
word = word.lower().replace(" ", "")
if word == word[::-1]:
    print(f"Слово '{word}' - это палиндром!")
else:
    print(f"Слово '{word}' - не палиндром.")

# Уровень 5.3
def are_anagrams(word1, word2):
    return sorted(word1.lower().replace(" ", "")) == sorted(word2.lower().replace(" ", ""))
word1 = input("Введите первое слово: ")
word2 = input("Введите второе слово: ")
if are_anagrams(word1, word2):
    print(f"[ДА] '{word1}' и '{word2}' - анаграммы!")
else:
    print(f"[НЕТ] '{word1}' и '{word2}' - не анаграммы.")

# Уровень 6.1
import math
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True
n = int(input("Введите число: "))
if is_prime(n):
    print(f"{n} - простое число")
else:
    print(f"{n} - составное число")

# Уровень 6.2
def add(a, b):
    return a + b
def sub(a, b):
    return a - b
def mul(a, b):
    return a * b
def div(a, b):
    return a / b if b != 0 else "Ошибка"
def calculator():
    print("Калькулятор")
    print("Операции: +, -, *, /")
    a = float(input("Число 1: "))
    op = input("Операция (+, -, *, /): ")
    b = float(input("Число 2: "))
    if op == '+':
        result = add(a, b)
    elif op == '-':
        result = sub(a, b)
    elif op == '*':
        result = mul(a, b)
    elif op == '/':
        result = div(a, b)
    else:
        result = "Неизвестная операция"
    print(f"Результат: {result}")
calculator()

# Уровень 6.3
import random
import string
def generate_password(length=12):
    chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(chars) for _ in range(length))
length = int(input("Длина пароля: "))
print(f"Ваш пароль: {generate_password(length)}")

# Уровень 7.1
book = {}
while True:
    print("\n1. Добавить  2. Удалить  3. Найти  4. Все  5. Выход")
    choice = input("Выберите: ")
    if choice == '1':
        name = input("Имя: ")
        phone = input("Телефон: ")
        book[name] = phone
        print("OK")
    elif choice == '2':
        name = input("Имя: ")
        if name in book:
            del book[name]
            print("Удалено")
        else:
            print("Не найдено")
    elif choice == '3':
        name = input("Имя: ")
        if name in book:
            print(f"{name}: {book[name]}")
        else:
            print("Не найдено")
    elif choice == '4':
        if book:
            for name, phone in book.items():
                print(f"{name}: {phone}")
        else:
            print("Книга пуста")
    elif choice == '5':
        break
    else:
        print("Неверный выбор")

# Уровень 7.2
from collections import Counter
def word_frequency(text):
    words = text.lower().split()
    return Counter(words)
text = input("Введите текст: ")
freq = word_frequency(text)
print("\nЧастота слов:")
for word, count in freq.most_common():
    if count > 1:  # Показываем только слова, которые встречаются больше 1 раза
        print(f"{word}: {count}")

# Уровень 7.3
inventory = {}
def add_item(item, count=1):
    if item in inventory:
        inventory[item] += count
    else:
        inventory[item] = count
    print(f"Добавлено: {item} x{count}")
def remove_item(item, count=1):
    if item in inventory and inventory[item] >= count:
        inventory[item] -= count
        if inventory[item] == 0:
            del inventory[item]
        print(f"Удалено: {item} x{count}")
    else:
        print(f"Недостаточно {item}")
def show_inventory():
    if not inventory:
        print("Инвентарь пуст")
    else:
        print("\nИНВЕНТАРЬ:")
        for item, count in inventory.items():
            print(f"  {item}: {count}")
add_item("зелье", 3)
add_item("меч", 1)
show_inventory()
remove_item("зелье", 1)
show_inventory()
