print("Здраствуйте! Программа по подсчету общих трат")

name1 = input("Данные первого человека: ")
name2 = input("Данные второго человека: ")
name3 = input("Данные третьего человека: ")

salary1 = input("Доход первого человека: ")
salary2 = input("Доход второго человека: ")
salary3 = input("Доход третьего человека: ")

amount = int(salary1) + int(salary2) + int(salary3)

mean = amount/3
mean = str(mean)

print(name1.title() + " Может потратить: " + mean)
print(name2.title() + " Может потратить: " + mean)
print(name3.title() + " Может потратить: " + mean)
