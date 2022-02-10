a = int(input('Введите сумму вклада:  '))
b = int(input('Введите процентную ставку:  '))
s = int(input('Введите количество недель:  '))
y = 100
g = b / y
count = a
for i in range(s):
    count += count * g
print('Сумма за', s, 'недель(ли) составляет___', count)
print(345)
print(987)
