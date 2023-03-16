# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. Определите минимальное
# число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть

sum_resh = 0
sum_orel = 0
num_coins = int(input('Num coin--> '))
for i in range(num_coins):
    side = int(input(f'Coin_{i}--> '))
    if side > 0:
        sum_orel += 1
    else:
        sum_resh += 1
   
    res = sum_orel if sum_orel < sum_resh else sum_resh  

print(res)

# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по 
# математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого 
# Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать 
# задуманные Петей числа.

sum_numbers = int(input("Sum numbers--> "))
product_numbers = int(input("Product numbers--> "))
number_x = int((sum_numbers**2 -4*product_numbers)**0.5/2 + sum_numbers/2) 

if 1 <= number_x <= 1000:
    number_y = sum_numbers - number_x  
    if 1 <= number_y <= 1000:  
        print(number_x, number_y)

# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

number = int(input("Введите целое число: "))
k = 0
result = 1
while result <= number:
    result = 2**k
    
    if result <= number:
        print (result, end = " ")
        k += 1



        
    
  


