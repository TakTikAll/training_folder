# cars = ['mazda', 'volvo', 'bmw']

# cars.append('jigul')
# del cars[-1]
# print(cars[-1].title())


# ---


# cars = ['mazda', 'volvo', 'bmw']

# cars.append('jigul')
# cars.remove('jigul')
# print(cars[-1].title())


#---


# cars = ['mazda', 'volvo', 'bmw']

# cars.append('jigul')
# cars.sort()
# cars.reverse()
# print(cars)


# ---

names = []
salarys= []

amount = 0
amount_of_members = input('Введите количество членов семьи: ')
aom = int(amount_of_members)

for i in range(aom):
	names.append(input('Имя ' + str(i+1) + ' человека:\n'))

for i in range(aom):
	salarys.append(input("Доход "+ str(i+1) + ' человека:\n'))

credit = input('введите сумму кредита :')
how_long = input('на какой срок кредит в месяцах :')
procent = input('введите процент :')

pay_per_mounth = (int(credit) / int(how_long)) + ((int(credit) / 100 * int(procent)) / 12)

print('Месячный платеж', pay_per_mounth)

for salary in salarys:
	amount += int(salary)

# amount -= pay_per_mounth

mean = (amount - pay_per_mounth) / aom
mean = str(mean)
for name in names:
	print(name.title() + " может потратить" + mean)



