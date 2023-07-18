
# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

n = int(input('Введите число'))

number = 2
index = 1
result = 1

while index <=n:
    result = result*number
    index += 1
    print(result, end=" ")
