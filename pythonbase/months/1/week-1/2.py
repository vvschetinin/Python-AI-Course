# Задача 1.
# Напиши программу, которая запрашивает у пользователя два числа и выводит их сумму, разность, произведение и частное.

# Начальный уровень

userNumberOne = int(input("Введите целое число А: "))
userNumberTwo = int(input("Введите целое число B: "))

print(f"Сумма: {userNumberOne + userNumberTwo}")
print(f"Разность: {userNumberOne - userNumberTwo}")
print(f"Произведение: {userNumberOne * userNumberTwo}")
print(f"Частное: {userNumberOne / userNumberTwo}")

# Через функцию

# Эта программа выполняет следующие действия:

# Определяет функцию calculate_operations, которая принимает два числа и выполняет все необходимые вычисления.
# Запрашивает у пользователя ввод двух чисел, используя функцию input(). Введенные значения преобразуются в тип float, чтобы можно было работать с дробными числами.
# Вызывает функцию calculate_operations с введенными пользователем числами.
# Выводит результаты вычислений на экран, используя форматированные строки.


def calculation(num1, num2):
    calcsum = num1 + num2
    calcsub = num1 - num2
    calcmul = num1 * num2
    calcdiv = None
    if num2 != 0:
        calcdiv = num1 / num2
    else:
        print("Делить на ноль нельзя")

    return calcsum, calcsub, calcmul, calcdiv


num1 = float(input("Введите число А: "))
num2 = float(input("Введите число B: "))

# Вычисление результата

result = calculation(num1, num2)

# Вывод результатов

print(f"Сумма: {result[0]}")
print(f"Разность: {result[1]}")
print(f"Произведение: {result[2]}")
print(f"Частное: {result[3]}")
