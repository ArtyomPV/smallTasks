# ==================================================================
# Задача 2: Найдите сумму цифр трехзначного числа.
# *Пример:*
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) |х
# number = int(input('Введите трехзначное число:\n '))
# sum = 0
# if 100 <= number < 1000:
#     while number != 0:
#         sum += number % 10
#         number //= 10
#     print(sum)
# else:
#     print("Введеное число не является трехзначным")


# ==================================================================
# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов.
# Вместе они сделали S журавликов. Сколько журавликов сделал каждый ребенок,
# если известно, что Петя и Сережа сделали одинаковое количество журавликов,
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
# *Пример:*
# 6 -> 1  4  1
# 24 -> 4  16  4
# 60 -> 10  40  10

# number_Crane_bird = int(input('Введите количество журавликов: \n'))
# Petya = None
# Sereja = None
# Katya = None
#
# Sereja = number_Crane_bird//6
# Petya = Sereja
# Katya = 2*(Petya + Sereja)

# print(Petya, Katya, Sereja)

# ==================================================================
# Задача 6: Вы пользуетесь общественным транспортом? Вероятно,
# вы расплачивались за проезд и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером,
# где сумма первых трех цифр равна сумме последних трех.
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
# Вам требуется написать программу, которая проверяет счастливость билета.
#
# *Пример:*
#
# 385916 -> yes
# 123456 -> no

# bilet_Number = int(input("Введите номер билета; \n"))
# num1 = bilet_Number//1000
# num2 = bilet_Number%1000
# sum1, sum2 = 0, 0
#
# while num1 != 0 and num2 != 0:
#     sum1 += num1 % 10
#     num1 //= 10
#     sum2 += num2 % 10
#     num2 //= 10
#
# if sum != sum:
#     print("no")
# else:
#     print("yes")

# ==================================================================
# Задача 8: Требуется определить, можно ли от шоколадки размером n × m
# долек отломить k долек, если разрешается сделать один разлом по прямой
# между дольками (то есть разломить шоколадку на два прямоугольника).
#
# *Пример:*
#
# 3 2 4 -> yes
# 3 2 1 -> no

length = int(input('введите количество рядов: \n'))
width = int(input('введите количество колонок: \n'))
amount = int(input('введите частей шоколадки: \n'))
print((length*width)%amount)

if amount % length == 0 or amount % width == 0:
    print('Yes')
else:
    print('No')
