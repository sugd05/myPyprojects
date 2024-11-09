print("Все ли равны?")


first = int(input('Загадайте первое число:'))
second = int(input('Загадайте второе число:'))
third = int(input('Загадайте третье число:'))
if first / second == 1 and second / third == 1:
    print(3)
elif first / second == 1 or second / third == 1 or first / third == 1:
    print(2)
else:
    print(0)