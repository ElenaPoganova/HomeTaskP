# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов.
#  Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество 
# журавликов, а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?

# *Пример:*

# 6 -> 1  4  1
# 24 -> 4  16  4
#     60 -> 10  40  10

print("Введите четное число больше 2: ")
s = int(input())
n = m = s//6 
k = (n + m)*2
print(n,k,m)
