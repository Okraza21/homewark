def plus():
    a = int(input('Введите первое число: '))
    b = int(input('Введите второе число: '))
    return a + b
def minus():
    a = int(input('Введите первое число: '))
    b = int(input('Введите второе число: '))
    return a - b
def umnoj():
    a = int(input('Введите первое число: '))
    b = int(input('Введите второе число: '))
    return a * b
def delenie():
    while True:
        try:
            a = int(input('Введите первое число: '))
            b = int(input('Введите второе число: '))
            return a / b
        except ZeroDivisionError:
            print('На ноль делить нельзя! Введите другое значение!')
        if b != 0:
            break
def stepen():
    a = int(input('Введите первое число: '))
    b = int(input('Введите второе число: '))
    return a ** b
def exit():
    print('Конец программы!')

while True:
    my = (input('''Введите операцию, которую хотите выполнить:
'+', '-', '*', '/', '^'
Выход из программы '0'
Ввод: '''))
    if my == '-' or my == '+' or my == '/' or my == '^' or my == '*':
        if my == '+':
            print('Ответ:', plus())
        elif my == '-':
            print('Ответ:', minus())
        elif my == '*':
            print('Ответ:', umnoj())
        elif my == '/':
            print('Ответ:', delenie())
        elif my == '^':
            print('Ответ:', stepen())
    elif my == '0':
        exit()
        break
    else:
        print('Вы выбрали неверную операцию!')
        continue
print(1)

        


































# homewark
