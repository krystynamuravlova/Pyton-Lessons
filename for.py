from random import randint

x = [randint(1, 10) for i in range(9)]
print(x)
y = input('Рахуємо цифру:')

counter_y = 0
for i in x:
    counter_y += str(i).count(y)
print('Цифра', y, 'зустрічається у списку', counter_y, 'разів.')
if counter_y == 0:
    print('Такої цифри немає в списку.')