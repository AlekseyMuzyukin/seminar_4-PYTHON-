k = 1
x = 0
a = int(input('Введите количество циклов '))
for k in range(1, a):
    x = x+4*((-1)**(k+1))/(2*k-1)
print(f'{round(x, 5)} Нужно больше циклов для точности вычесления')