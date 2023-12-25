print ('Решаем уравнение a*x^2+b*x+c=0')
a = input('a: ')
b = input('b: ')
c = input('c: ')
a = float(a)
b = float(b)
c = float(c)
discriminant = b**2 - 4*a*c
print('D =' + str(discriminant))
if discriminant < 0:
    print('корней нет')
elif discriminant == 0:
    x = -b / (2 * a)
    print('x =' + str(x))
else:
    x1 = (-b + discriminant ** 0.5) / (2 * a)
    x2 = (-b - discriminant ** 0.5) / (2 * a)
    print('x1 =' + str(x1))
    print('x2 =' + str(x2))
