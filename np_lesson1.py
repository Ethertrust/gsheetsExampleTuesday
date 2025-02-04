import numpy as np

scores_l = [[20, 40, 56, 80, 0, 5, 25, 27, 74, 1],
         [0, 98, 67, 100, 8, 56, 34, 82, 100, 7],
         [78, 54, 23, 79, 100, 0, 0, 42, 95, 83],
         [51, 50, 47, 23, 100, 94, 25, 48, 38, 77],
         [90, 87, 41, 89, 52, 0, 5, 17, 28, 99],
         [32, 18, 21, 18, 29, 31, 48, 62, 76, 22],
         [6, 0, 65, 78, 43, 22, 38, 88, 94, 100]]
scores = np.array(scores_l)

list1 = [[1, 2, 3],
         [4, 5, 6]]

print(list1, type(list1))
a = np.array(list1)
print(a, type(a))
print('----------')
print('1. Основные свойства Numpy массивов')
print('Размерность - количество измерений', a.ndim)
print('Количество элементов', a.size)
print('Форма массива', a.shape)
print('Хранимый тип данных', a.dtype)
list2 = [[1, 2, 3],
         [4, 'строка', 6]]
b = np.array(list2, dtype=object)
print(b, type(b),  b.dtype, type(b[0][0]))
print('----------')
print('2. Создание Numpy массивов')
c = np.zeros((3, 4), dtype=np.int16)
print(c, type(c))
c = np.ones((3, 4), dtype=np.int16)
print(c, type(c))
c = np.eye(5,dtype=np.int16)
print(c, type(c))
c = np.full((4, 3, 2), 6, dtype=np.int16)
print(c, type(c))
d = np.full_like(b, 6, dtype=np.int16)
print(d, type(d))
d = np.random.rand(6, 6) * 6 - 3
print(d.reshape((2,6,3)), type(d))
d = np.random.randint(2, 6, [3, 3, 3])
print(d, type(d))
print('----------')
print('3. Нарезка Numpy массивов')
print(scores, scores.shape)
# print(scores[-1])
print(scores[-1][-2])
print(scores[-1][-2:])
print(scores_l[-2:][-2:])
print(scores[-2:][-2:])
print(scores[-2:, -2:])
# print(scores[-2:])
print('----------')
print('4. Нарезка Numpy массивов с помощью булевых Numpy массивов')
d = (scores > 50) & (scores < 70) # and &
d = (scores > 70) | (scores < 50) # or |
print(scores, scores.shape)
print(d, d.shape)
print(scores[d])
print('----------')
print('5. Нарезка Numpy массивов с помощью булевых Numpy массивов')
list1 = [[1, 2, 3],
         [4, 5, 6]]
a = np.array(list1)
list3 = [[1, 2],
         [4, 5],
         [3, 6]]
c = np.array(list3)
list2 = [[7, 8, 9],
         [10, 11, 12]]
b = np.array(list2)
print(a)
# print(a/1)
print(b)
print(c)
print(a * b)
print(a @ c)
print(np.pow(a, 2))
print(np.pow(a, b))
d = np.random.randint(2, 6, [3, 3])
print(d)
print(d.T)
print('----------')
print('6. Стандартные функции Numpy массивов')
# print(scores)
# print(scores.min())
# print(scores.min(axis=0))
# print(scores.min(axis=1))
# d = np.random.randint(2, 6, [2, 3, 4])
# print(d)
# print(d.argmin(axis=0), d.min(axis=0))
# print(d.min(axis=1))
# print(d.min(axis=2))
list1 = [0, 30, 90]
a = np.array(list1)
print(a)
print(np.sin(np.deg2rad(a)))
print(np.rad2deg(a))
print(np.sin(a))
print(np.exp(a))
#[1.00000000e+00 1.06864746e+13 1.22040329e+39]
#[1 * 10^0 1.06864746e * 10^13 1.22040329 * 10^39]
print('----------')
print('7. Нарезка многомерных Numpy массивов')
cube1 = np.random.randint(1, 3, [3, 3, 3])
cube2 = np.random.randint(3, 5, [3, 3, 3])
cube3 = np.random.randint(5, 7, [3, 3, 3])
q1 = np.array([cube1, cube2, cube3])
q2 = np.array([cube2, cube1, cube3])
q3 = np.array([cube3, cube1, cube2])
array5 = np.array([q1, q2, q3])
print(array5[0])
print(q1[-1,:,:,-1])
print(q1[-1,...,-1])
print(q1[-1,-2,...,-1])
# print(q1[-1,...,-2,...,-1])
print(q1[-1,-2,...])
# print(array5[...,-1])

