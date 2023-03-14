a = int(input("Перше число:"))
b = int(input("Друге число:"))
s = 2

while a < b:
 a += s
 print("Перше число збільшлось і дорівнює:", a)

if a >= b:
    print("Кінець!")