n = int(input('Введите число '))
answ = []
d = 2
while d * d <= n:
    if n % d == 0:
        answ.append(d)
        n //= d
    else:
        d += 1
if n > 1:
    answ.append(n)
print(answ)
