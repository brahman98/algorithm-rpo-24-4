# ЦИКЛЫ WHILE, FOR

# while
# count = 2
# while count <= 50:
#     print(count)
#     # count = count + 1
#     count += 2

# for
# for i in range(2, 51, 2):
#     print(i)

# вывод чисел от 100 до 10 - 100, 90 и тд
# вывод чисел в диапазоне от 1 до 100 кратно 3

# for i in range(100, 0, -10):
#     print(i)
# for i in range(3, 101, 3):
#     print(i)

# break and continue
# while True:
#     number = int(input('Введите число: '))
#     if number == 0:
#         print('Вы ввели:', number)
#         break
#     print('Вы ввели:', number)

# for i in range(1, 11):
#     if i == 5:
#         continue
#     print(i)

# мини-игра - угадай число (while True)
# если загаданное число больше - сказать об этом
# если загаданное число меньше - сказать об этом
# если угадал - поздравить с победой


# САМОСТОЯТЕЛЬНАЯ РАБОТА
# ЗАДАНИЕ 1 - СУММА ЧИСЕЛ
# Пользователь вводит число N.
# Найти сумму чисел от 1 до N через цикл.


# random
import random

# number = random.randint(1, 10)
# print(number)

# one = 0
# for i in range(100):
#     dice = random.randint(1, 10)
#     # print('Выпало: ', dice)
#     if dice == 1:
#         one += 1
# print("значение 1 выпало", one, "раз")

# choice = random.choice(["камень", "ножницы", "бумага"])
# print(choice)



# мини-игра - орел и решка
# wins = 0
# for i in range(5):
#     player = input("орел или решка? ")
#     computer = random.choice(['орел', 'решка'])
#     print('Выпало: ', computer)
#     if player == computer:
#         print('угадал')
#         wins += 1
#     else:
#         print('не угадал')
# print('Правильных ответов: ', wins)


# в цикле сгенерировать 1000 случайных чисел в диапазоне от 1 до 10
# сделать 10 переменных-счетчиков для каждого числа (от 1 до 10)
# каждый раз после генерации увеличить значение соответствующей переменной-счетчика на 1
# вывести в терминале сколько раз выпало каждое из чисел
# *написать процент для каждого числа по отношению к общему количеству генераций



nums = [9, 8, 7, 6, 5, 4, 3, 2, 1]

# print(len(nums))
# print(sum(nums))
# print(min(nums))
# print(max(nums))
# print()

count = 0
for i in nums:
    count += 1
print(count)

total = 0
for i in nums:
    total += i
print(total)

min = nums[0]
for i in nums:
    if min > i:
        min = i
print(min)

max = nums[0]
for i in nums:
    if max < i:
        max = i
print(max)