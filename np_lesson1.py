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
list2 = [[1, 2.5, 3],
         [4, 'shgfsdj', scores_l]]
b = np.array(list2, dtype=object)