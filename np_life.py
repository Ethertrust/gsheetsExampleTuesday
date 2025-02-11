import numpy as np
from time import sleep
from os import system

np.set_printoptions(edgeitems=60, linewidth=200)
def printZ(Z):
    # A = Z.copy().astype(str)
    # A[A=='1'] = '*'
    # A[A=='0'] = ' '
    for line in Z:
        print(''.join(['*' if el==1 else ' ' for el in line]))

def generation(Z):
    # print(Z)
    b = np.zeros((Z.shape[0]+2, Z.shape[1]+2), dtype=np.int8)
    b[1:-1, 1:-1] = Z[...]
    b[1:-1, 0] = Z[:, -1]
    b[1:-1, -1] = Z[:, 0]
    b[0, 1:-1] = Z[-1, :]
    b[-1, 1:-1] = Z[0, :]
    b[0, 0] = Z[-1, -1]
    b[-1, -1] = Z[0, 0]
    b[0, -1] = Z[0, -1]
    b[-1, 0] = Z[-1, 0]
    # print(b)
    #Матрица соседей
    N = (b[0:-2, 0:-2] + b[0:-2, 1:-1] + b[0:-2, 2:]
      +  b[1:-1, 0:-2] +               + b[1:-1, 2:]
      +  b[2:, 0:-2]   + b[2:, 1:-1]   + b[2:, 2:])
    # print(N)
    #Правило рождения
    birth = (Z==0) & (N==3)
    # print(birth)
    #Правило выживания
    survival = (Z==1) & ((N==2)|(N==3))
    #Правило жизни
    life = birth|survival
    Z[...] = 0
    Z[life] = 1
    return Z

# Z = np.random.randint(0, 2, [20, 20])
with open('C:\\Users\\HYPER\\PycharmProjects\\Classes 4 wave\\tuesday\\gsheetsExample\\numpy_datasets\\3', 'r') as f:
    Z = np.stack([np.fromiter(line.strip(), dtype=np.int8) for line in f])
printZ(Z)

while(True):
    Z = generation(Z)#np.random.randint(0, 2, [20, 20])
    printZ(Z)
    sleep(0.04)
    system('cls')
