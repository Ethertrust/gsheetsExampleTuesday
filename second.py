# Цикл - несколько инструкций (набор инструкций), который повторяется несколько раз
# Блок инструкций - набор инструкций
# a = 0
# print(a)
# a += 1
# print(a)
# a += 1
# print(a)
# a += 1
# print(a)
# a += 1
# print(a)
#Идентация
# После двоеточия со следующей строки всегда должен быть отступ, выделяющий блок инструкций
# Состояние программы:
#   Исполняемая строка кода
#   Состояние памяти программы:
#       состояние имен
print('--------------0. Циклы')
# for a in range(5): # [0, 1, 2, 3, 4]
#     print(a)
#     for b in range(3): #[0, 1, 2]
#         print('Итерация вложенного цикла 2го уровня №', b)
#     print('Конец вложенного цикла 2го уровня')
#     print('Конец итерации')
# print('Конец цикла 1го уровня')
#debuger / отладчик
# Типы данных:
#   Неизменяемые/immutable:
#       int - целочисленный тип данных
#       float - вещественные числа
#       str - строковый тип данных
#       bool - логический тип данных: True/False
#       tuple - кортеж / упорядоченный набор элементов / контейнер
#   Изменяемые/mutable:
#       list - список / упорядоченный набор элементов / контейнер
#       dict - словарь/ неупорядоченный набор элементов (индексы => ключи) / контейнер
print('--------------1. Наборы элементов Списки')
a = 5
b = 6
str1 = 'Привет мир!'
list1 = [3,4,5]
print(list1)
print(list1[-1])
print(list1[0:-1])
list1[-1] = 'Мир!'
print(list1)
print('--------------')
list1 = [a, b, str1]
print(list1)
print(list1[-1])
str1 = 'Привет!'
b = 7
print(list1)
list2 = [14, 15, list1]
print('--------------List2')
print(list2)
list1[-1] ='543534'
print(list2)
list1 = [1, 2, 3]
print(list2)
list3 = list2[-1]
list3[-1] = '000000'
print(list2)
print('--------------tuple')
tuple1 = (4, 5, list1)
print(tuple1)
tuple1[-1][-1] = 6
print(tuple1)
print('--------------dict')
dict1 = {'Человек1':'Иванов Иван Иванович','Человек2':'Василий','Человек3':'Игорь', 4:'Марья'}
print(dict1, type(dict1))
print(dict1[4], type(dict1[4]))
# print(dict1['Человек1':'Человек3'], type(dict1['Человек1':'Человек3']))
# print(dict1[-1], type(dict1[-1]))
print('--------------циклы с наборами элементов')
for a in list2:
    print(a)
for a in tuple1:
    print(a)
for a in dict1:
    print(dict1[a])
for a, b in dict1.items():
    print(a, b)
print('--------------2. Условные конструкции')
b = 6
if a>b:
    print('a>b', a, b)
elif a==b:# else if/ иначе если
    print('a==b', a, b)
elif a<b:# else if/ иначе если
    print('a<b', a, b)
# else: # иначе
#     print('a<b', a, b)
print('Конец условной конструкции')
print('--------------циклы с наборами элементов и условными конструкциями')
print(list2)
for a in list2:
    print(type(a) == list)
    if type(a) == list:
        for b in a:
            print(b)
    else:
        print(a)

str1 = ';'.join(['а','б','в'])
print(str1.upper())
print(str1)
