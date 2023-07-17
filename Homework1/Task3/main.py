
# Проверка на счастливый билет

import math

n = int(input('Введите номер билета'))
number1 = n//1000
number_temp = (n/1000)%1
number2 = int(math.ceil(number_temp*1000))

result1 = 0
result2 = 0
while number1 > 0:
    result1 = result1 + (number1%10)
    number1 = number1//10

while number2 > 0:
    result2 = result2 + (number2%10)
    number2 = number2//10

if result1 == result2:
    print('Yes')
else: print('No')

