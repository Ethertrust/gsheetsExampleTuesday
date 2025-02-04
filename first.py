a = 5
a = 6
# Операторы:
#   Бинарные:
#      присвоения (операнд)=(операнд)
#   Унарные: -, +
#   Тернарные:
#
# Типы данных:
#   Неизменяемые/immutable:
#       int - целочисленный тип данных
#       float - вещественные числа
#       str - строковый тип данных
#       bool - логический тип данных: True/False
# Базовые функции:
#   print()
#   type()
print(a,7,8,9,10) # () -> входные данные/ параметры/ аргументы функции
print(7,8,a,9+11,10,sep = ';')
print(a, type(a))
b = 5.678
print(b, type(b))
print(a+b, type(a+b))
name = "Hello world!"
print(name, type(name))
name = """Привет\n         мир!"""
print(name, type(name))
# a = 6 #000000000110
# name = '6' #1010101010110011001010110101011
# инструкция и блок инструкция
print(name[0], type(name)) # индексация строк
print(name[-3], type(name)) # обратная индексация строк
print(name[-4:-1], type(name))
print(name[-4:], type(name))
print(name[:-4], type(name))
#bool : True/False 1/0 Истина/Ложь
print(True, type(True))
print(False, type(False))
c = True
print(c, type(c))
c = 7
print(c, type(c))

# d = input("Введите имя:")
# print("Ваше имя", d)
# ctrl + / -> #
# математические операторы
c = a + b
print(c, type(c))
c = a - b
print(c, type(c))
c = a * b
print(c, type(c))
c = a / b
print(c, type(c))
c = a / 1
print(c, type(c))
c = a // 1
print(c, type(c))
c = 17 / 6 #-> 17/6 = 2 5/6 = 2.8(3)
print(c, type(c))
c = 17 // 6
print(c, type(c))
c = 17 % 6
print(c, type(c))
c = 17 ** 6 # 17^6 = 24137569
print(c, type(c))
c = 17. ** 6 # 17^6 = 24137569.0
print(c, type(c))
c = 17.0 ** 6 # 17^6 = 24137569.0
print(c, type(c))
c = -17.0
print(c, type(c))
c = +17.0
print(c, type(c))
# c = c ** 6
# print(c, type(c))
c **= 6 # 17^6 = 24137569.0
print(c, type(c))
c = 17.0
c -= 6
print(c, type(c))
a = 6
b = 5
print('a==b',a==b)
c = a==b
print(a, b, c, type(c))
print('a!=b',a!=b)
c = a!=b
print(a, b, c, type(c))
print('a>=b',a>=b)
c = a>=b
print(a, b, c, type(c))
d = 'Привет!'
e = 'Привет!'
print('a==b',d==e)
c = d==e
print(d, e, c, type(c))
d = 'Привет!'
e = 'Привет'
print('a==b',d==e)
c = d==e
print(d, e, c, type(c))
d = 'Привет!'
e = 'Привет'
print('a>b',d>e)
c = d>e
print(d, e, c, type(c))
d = '2024.09.15'
e = '2024.10.14'
print('a>b',d>e)
c = d>e
print(d, e, c, type(c))
d = '15.09.2024'# а-я А-Я 0-9
e = '14.10.2024'
print('a>b',d>e)
c = d>e
print(d, e, c, type(c))
print('.'>'а')
print('а'>'a')
print('А'>'а')