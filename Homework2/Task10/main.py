
# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой,
# а некоторые – гербом. Определите минимальное число монеток,
# которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть


from random import randint

n = int(input ('Введите количество монет: '))
current_n = 0
index_0 = 0
index_1 = 0


for current_n in range(n):
    current_n = randint(0, 1)
    print(current_n, end=' ')
    if current_n == 0:
        index_0=+1
        if current_n ==1:
            index_1+=1

if index_0>index_1:
    print(index_1)  
else:
    print(index_0)




