import random

constMatrix = lambda m, n, val: [[val for i in range(m)] for i in range(n)]

def initialData():
        #m = 25
    #n = 10
    #matrix = initMatrix(m,n) 

    heightmap = [[ 0, 10,  0, 20,  0],
                [20,  0, 30,  0, 40],
                [ 0, 40,  0, 50,  0],
                [50,  0, 60,  0, 70],
                [ 0, 60,  0, 70,  0]]

    
    #heightmap = [  [9, 9, 9, 9, 9],
    #            [9, 0, 1, 2, 9],
    #            [9, 7, 8, 3, 9],
    #            [9, 6, 5, 4, 9],
    #            [9, 9, 9, 9, 9]]

    #heightmap = [  [2, 1, 2],
    #            [1, 0, 1],
    #            [2, 1, 2]]
    
    #heightmap = [[0]]

    # 56    
    heightmap = [[8, 8, 8, 8, 6, 6, 6, 6],
                [8, 0, 0, 8, 6, 0, 0, 6],
                [8, 0, 0, 8, 6, 0, 0, 6],
                [8, 8, 8, 8, 6, 6, 6, 0]]

    # : 319 should equal 326

    heightmap = [   [2,  0,  8,  3, -4,  9,  9, -3, 13, -5,  4,  5,  5, -3, -2],
                    [2,  2,  8, 14, -3,  7,  2, 14,  2,  9,  2, 14,  0,  5,  7],
                    [0,  2, 13,  9,  2,  2,  2,  2,  2,  2,  2, 14,  0, -1,  6],
                    [-3, 4,  4,  8,  2,  8, 11,  4,  5, 12,  3,  3,  7, -1, -3],
                    [14, 8, 12, 14, 12, 10,  4,  8,  2,  7,  3,  6,  7,  2, -5],
                    [6,  6,  6,  6,  6,  9, 10,  6,  2,  2,  3,  3, 12, 12, -5],
                    [10, 6,  6,  9,  6, 12,  6,  6, 14,  2, 10, 11,  8,  3, -3],
                    [13, 13, 4,  9, 10, 10,  6,  8,  2,  2,  2,  9, 11,  3,  0],
                    [7,  6, 11, 12, 14,  6,  6, 11,  2,  7,  5,  5,  5, 10, 14],
                    [13,10,  7,  7,  8, 13, 14,  3,  2, 10,  9,  5,  5, 11,  9],
                    [12,10,  7,  7, 10, 10, 10, 13,  2,  2,  2,  5,  8,  2,  3],
                    [11,11,  7,  7,  7, 12, 10, 10, 12, 11,  2, 13, 11, -2, -5],
                    [-4, 3,  7, 14, 12, 13, 10, 10, 11,  1,  1,  6, -2, -2,  7],
                    [6, 13,  6, -1, 12,  4, 11,  6,  6,  2, -5,  2,  2, -3,  3]]

    m = 100
    n = 100
    heightmap = initMatrix(m,n) 


    return heightmap


def printMatrix(m1,  m2= None):
    print ("-"*30)
    for i, row in enumerate(m1):
        if m2:
            row2, row3 = m2[i], []            
            for j in range(len(row2)):
                row3.append(row2[j]-row[j])
            print ("".join(map ( lambda s: (str(s).center(3)), row)) 
            + " "*10 + "".join(map ( lambda s: (str(s).center(3)), row2))
            + " "*10 + "".join(map ( lambda s: (str(s).center(3)), row3))) 
        else:
            print ("".join(map ( lambda s: (str(s).center(3)), row)) )
    print ("-"*30)

def initMatrix(m,n):

    matrix = randomMatrix(m, n)
    #matrix = constMatrix(m, n, 7)    
    #modifyMatrix(matrix, 5, 10, 2, 7, 0)
    #modifyMatrix(matrix, 9, 14, 1, 5, 1)
    #modifyMatrix(matrix, 8, 20, 6, 9, 2)
    #modifyMatrix(matrix, 0, 6, 5, 6, 3)
    return matrix

def modifyMatrix(matrix, x1, x2, y1, y2, newVal):
    for x in range(x1, x2+1):
        for y in range(y1, y2):
            matrix[y][x] = newVal
    return matrix


def randomMatrix(m,n):
    matrix = [[random.randint(0,9) for i in range(m)] for i in range(n)]
    return matrix