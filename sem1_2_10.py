# Найти расстояние между двумя точками пространства

x1 = int(input('X1 ='))
y1 = int(input('Y1 ='))
z1 = int(input('Z1 ='))
x2 = int(input('X2 ='))
y2 = int(input('Y2 ='))
z2 = int(input('Z2 ='))

value = ((x2 - x1)**2) + ((y2 - y1)**2) + ((z2 - z1)**2)
x = value ** (0.5)
print(f'AB = \u221a{value} = {x}')

#A(-1, 3, 3) и B(6, 2, -2)
#AB = √(xb - xa)2 + (yb - ya)2 + (zb - za)2 =
#= √(6 - (-1))2 + (2 - 3)2 + (-2 - 3)2 = √72 + 12 + 52 = √75 = 5√3