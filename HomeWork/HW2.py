# На низком уровне у человека будет 12 попыток,  на среднем - 9, на высоком - только 6.
# Если человек вводит слишком большое число, ему говорится, что “нужно поменьше”, если маленькое - пишет “ нужно побольше”.
# Если человек угадал, тогда ему нужно написать, что он победил. Если проиграл, утешить.

# from random
import random

level_chance = {1:12, 2:9, 3:6}


print('Супер игра "Угадайка"')
print('Попруй победить машину\n')
print('У нас есть 3 вида уровня:\n 1- легкий(12 попыток);\n 2- средний(9 попыток);\n 3- сложный(3 попытки).')
print('Выбирите уровень в виде цифры:\n')

# Над этим я бился 6 вечеров и не смог понять как это победить =(((
# пытался написать элемент что бы он ввёл правильное число

# level_dif = 0
# while level_dif not in range(1,3):
#     level_dif = int(input())
#     if level_dif == 0 or level_dif > 4:
#         print('такого сложного уровня нет =) , нужно выбрать от 1 до 3 \n Выбирите уровень в виде цифры:\n')
#     elif (0 > level_dif < 4):
#         print('Здорово!')

level = int(input())

if (level == 1):
    print('У вас 12 попыток')
elif (level == 2):
    print('У вас 9 попыток')
elif (level == 3):
    print('У вас 6 попыток')


print('Давайте начнём, как вы думаете, какое число задумала машина от 1 до 100:\n')


chance = level_chance[level]

machine_value = random.randint(0,100)
player_number = int(input('Ваш вариант: '))

chance_left = 1
while chance_left != chance:
    if player_number == machine_value:
        break
    elif player_number < machine_value:
        print('Число машины выше')
    elif player_number > machine_value:
        print('Число машины ниже')
    player_number = int(input('У вас есть ещё попытка:\n '))
    chance_left += 1

if player_number == machine_value:
    print('Вы победили!')
if player_number != machine_value:
    print('Вы проиграли!')

