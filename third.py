
# print(list1)
# Объявление функции
# 1. Порядковые параметры
# 2. Кортеж параметров
# 3. Именованные параметры с дефолтными значениями
def printList(list2, name1, name2, name3, *tuple1, name5, sep = ' '):
    print(1,2,3,4)#*tuple1
    for el in list1:
        el = '###'
        print(el)
    list1[-1] = '###'
    list3 = [name1] + [name2] + [name3]
    print(list3)
    print('Конец вызова функции')
    return sep.join(list3)

#Функция
def printL(list1):
    for el in list1:
        return el

#Генератор
def printGenL(list1):
    for el in list1:
        yield el

list1 = [1,2,'Привет!']
#Вызов функции
result = printList(list1, 'Вася', 'Мася', 'Кто-то', 1,2,3,4, sep= ' ', name5='tuple')
print(result)
# print(list1)
print('Конец программы')
# gen = range(4)
# print(gen)
for el in printGenL(list1):#[0,1,2,3,4]
    print(el)

a = 0
while a<5:
    a+=1
    print(a)

printList(list1, 'Вася', 'Мася', 'Кто-то', 1,2,3,4, sep= ' ', name5='tuple')
printList(list1, 'Вася', 'Мася', 'Кто-то', 1,2,3,4, sep= ' ', name5='tuple')
printList(list1, 'Вася', 'Мася', 'Кто-то', 1,2,3,4, sep= ' ', name5='tuple')
printList(list1, 'Вася', 'Мася', 'Кто-то', 1,2,3,4, sep= ' ', name5='tuple')


