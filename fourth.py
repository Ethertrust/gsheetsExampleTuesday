from datetime import datetime as dt
# not and or in
# not - "не" True->False / False->True
# and - "и"
# or - "или"
# in - "в" проверить есть ли в наборе элементов какой-то элемент

hum1 = {'Имя': 'Василий', 'Age': 42}
hum2 = {'Имя': 'Игорь', 'Age': 28}
hum3 = {'Имя': 'Василий'}
hums = [hum1, hum2, hum3]
# if not hum1['Age'] == 30:
#     print('Проваливай!')

# for hum in hums:
#     if hum['Имя'] == 'Игорь':
#         if hum['Age'] == 28:
#             print('Проваливай,', hum['Имя'] + '!')

# for hum in hums:
#     if hum['Имя'] == 'Игорь' and hum['Age'] == 28:
#         print('Проваливай,', hum['Имя'] + '!')
#
# for hum in hums:
#     if hum['Имя'] == 'Игорь' or hum['Age'] <= 30:
#         print('Проваливай,', hum['Имя'] + '!')

# for hum in hums:
#     if 'Age' in hum and hum['Age'] == 28 and hum['Имя'] == 'Игорь':
#         print('Проваливай,', hum['Имя'] + '!')

# for hum in hums:
#     if 'Age' in hum and (hum['Age'] <= 30 or hum['Имя'] == 'Игорь'):
#         print('Проваливай,', hum['Имя'] + '!')

date_time_str = '18/19/09 01:55:19'
date_time_str2 = '28//09//18'

date_time_obj = dt.strptime(date_time_str, '%d/%y/%m %H:%M:%S')
date_time_obj2 = dt.strptime(date_time_str2, '%d//%m//%y')
#>,<, =, !=

print("The type of the date is now",  type(date_time_obj))
print("The date is", date_time_obj, 'and', date_time_obj2)
if date_time_obj > date_time_obj2:
    print("Latest one is", date_time_obj.strftime("%d/%m/%y %H:%M:%S"))
else:
    print("Latest one is", date_time_obj2.strftime("%d/%m/%y %H:%M:%S"))