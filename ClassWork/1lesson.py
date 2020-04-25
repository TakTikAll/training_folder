# Hi = 'Mother clean rama'
# a = 14
# b = input("Введите степень числа 5:\n ")
# print(a ** int(b))


# ---


# print('Привет, пользователь!')
# name = input('Назовите ваше имя:\n')
# print('Здравствуйте, ' + name.title())


# ---


print('Доброго времени суток! Я программа по подсчёту общих затрат:\n')
name1 = input('Данные первого человека: ')
name2 = input('Данные второго человека: ')
name3 = input('Данные третьего человека: ')

salary1 = input('Доход первого человека: ')
salary2 = input('Доход второго человека: ')
salary3 = input('Доход третьего человека: ')

amount = int(salary1) + int(salary2) + int(salary3)
mean = amount / 3
mean = str(mean)

print("Может тратить, " + name1.title() + ":" + mean)