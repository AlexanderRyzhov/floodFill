import cProfile
import time

from helpers import initialData
from helpers import printMatrix as printMatrixImpl
from collections import deque

customCopy = lambda matrix: [row.copy() for row in matrix]        
constMatrix = lambda m, n, val: [[val for i in range(m)] for i in range(n)]

def printMatrix(*args):
    try:
        printMatrixImpl(*args)
    except NameError:
        pass

def calcVolume(m1, m2):    
    volume = 0
    for (row1, row2) in zip(m1, m2):
        for v1,v2 in zip(row1, row2):
            volume += (v2 - v1)
    return volume

def spiralWalkMatrix(m, n, skip = 0):
    cycles = min((m + 1) // 2, (n + 1) // 2)
    for yi in range(skip, cycles):
        # left to rigth
        for xj in range(yi, m - yi):
            yield xj, yi, ">"
        # top to bottom
        if yi + 1 <= n - yi - 2:
            for yk in range (yi+1, n - yi - 1):
                x = m - yi - 1
                yield x, yk, "v"
        # rigth to left
        if yi < n - yi-1:
            for xj in range(m - yi - 1, 0+yi-1, -1):
                yield xj, n - yi -1, "<"
        # bottom to top
        if (yi + 1 <= n - yi - 2) and (yi < m - yi - 1):
            for yk in range (n - 2 - yi, yi, -1):
                x = yi
                yield x, yk, "^"

def spiralWalkMatrixCenter(m, n, skip = 0):
    cycles = min((m + 1) // 2, (n + 1) // 2)
    for yi in range(cycles, skip-1, -1):
        # left to rigth
        for xj in range(yi, m - yi):
            yield xj, yi, ">"
        # top to bottom
        if yi + 1 <= n - yi - 2:
            for yk in range (yi+1, n - yi - 1):
                x = m - yi - 1
                yield x, yk, "v"
        # rigth to left
        if yi < n - yi-1:
            for xj in range(m - yi - 1, 0+yi-1, -1):
                yield xj, n - yi -1, "<"
        # bottom to top
        if (yi + 1 <= n - yi - 2) and (yi < m - yi - 1):
            for yk in range (n - 2 - yi, yi, -1):
                x = yi
                yield x, yk, "^"


def fill(matrix, new, xs, ys, calculated, exact = False):

    n, m = len(matrix), len(matrix[0])
    unvisited = constMatrix(m, n, True)   

    Q = deque()
    Q.append((xs, ys))  
    unvisited[ys][xs] = False 
    overfill = False
    iterations = 0

    while Q:
        iterations += 1
        #x, y = Q.pop(0)
        x, y = Q.popleft()                

        if (exact and matrix[y][x] == new - 1) or (matrix[y][x] < new):

            matrix[y][x] = new    
            if calculated[y][x]:
                overfill = True
            neighbours = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
            for xi, yi in neighbours:
                if (0 <= xi <= (m - 1)) and (0 <= yi <= (n - 1)):
                    if unvisited[yi][xi]:
                        unvisited[yi][xi] = False
                        Q.append((xi, yi))
                else:
                    overfill = True 
    
    # print (xs, ys, ":  ",iterations)
    return overfill

def fillXY(matrix, calculated, x, y):

    oldVal = matrix[y][x]    
    delta = 0
    noOverfill = True
    
    matrix_prev = customCopy(matrix)

    n, m = len(matrix), len(matrix[0])

    while noOverfill:        

        delta += 1   
        newVal = oldVal + delta

        matrix_tmp = customCopy(matrix)
        noOverfill = not fill(matrix_tmp, newVal, x, y, calculated)

        if noOverfill:
            matrix_prev = customCopy(matrix_tmp)

    matrix_tmp = customCopy(matrix_prev)
    fill(matrix_tmp, newVal, x, y, calculated, True)

    for x in range(m):
        for y in range(n):        
            if not(matrix[y][x] == matrix_tmp[y][x]):
                if (0 < x < m - 1) and ( 0 < y < n - 1):
                    matrix[y][x] = matrix_prev[y][x]
                if (matrix_tmp[y][x] == matrix_prev[y][x]+1):
                    calculated[y][x] = True

    
def volume(heightmap):

    n, m = len(heightmap), len(heightmap[0])
    
    initial = customCopy(heightmap)     
    printMatrix(initial)
    
    calculated  = constMatrix(m, n, False)   
    
    for x,y,k in spiralWalkMatrixCenter(m,n,1):
        print(x,y)
        if not calculated[y][x]:
            fillXY(heightmap, calculated, x, y)

    volume = calcVolume(initial, heightmap)
    printMatrix(initial, heightmap)

    return volume
    

def main():

    heightmap = initialData()
    print(volume(heightmap))



if __name__ == "__main__":    
    start_time = time.time()    
    #cProfile.run('main()')
    main()    
    print("--- %s seconds ---" % (time.time() - start_time))