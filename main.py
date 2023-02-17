'''Найдите сумму цифр трехзначного числа.
Пример:
123 -> 6 (1 + 2 + 3)
100 -> 1 (1 + 0 + 0)'''
#Решение
print('Введите трёхзначное число: ')
three_digit_number = int(input())
print(f'Число для вычисления суммы цифр: {three_digit_number}') 
summa_digits = 0
first_digit  = three_digit_number//100
second_digit = (three_digit_number - first_digit*100)//10
third_digit = three_digit_number%10  
print(f"Сумма цифр {three_digit_number} равна {first_digit + second_digit + third_digit}")