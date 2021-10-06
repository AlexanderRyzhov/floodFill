import cProfile
import time

from helpers import initialData
from helpers import printMatrix as printMatrixImpl

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

def findMinCoordsSpiral(matrix, calculated):

    n, m = len(matrix), len(matrix[0])
    
    minValue = xmin = ymin = None
     
    for x,y,k in spiralWalkMatrix(m,n,1):

        if minValue == None:
            minValue = matrix[y][x]
        if matrix[y][x] <= minValue:
            if not (calculated[y][x]):
                minValue = matrix[y][x]
                xmin, ymin = x, y
    
    return xmin, ymin, minValue

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

def fill(matrix, new, x, y, calculated, exact = False):

    Q = []
    Q.append((x, y))   
    overfill = False

    while len(Q)>0:
        
        x, y = Q.pop(0)

        if (exact and matrix[y][x] == new - 1) or (matrix[y][x] < new):

            matrix[y][x] = new    
            if calculated[y][x]:
                overfill = True
            neighbours = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
            for xi, yi in neighbours:
                if (0 <= xi <= len(matrix[0])-1) and (0 <= yi <= len(matrix)-1):
                    Q.append((xi, yi))
                else:
                    overfill = True 
    
    return overfill

def fillXY(matrix, calculated, x, y):

    oldVal = matrix[y][x]    
    delta = 0
    noOverfill = True
    
    matrix_prev = customCopy(matrix)

    while noOverfill:        

        delta += 1   
        newVal = oldVal + delta

        matrix_tmp = customCopy(matrix)
        noOverfill = not fill(matrix_tmp, newVal, x, y, calculated)

        if noOverfill:
            matrix_prev = customCopy(matrix_tmp)

    matrix_tmp = customCopy(matrix_prev)
    fill(matrix_tmp, newVal, x, y, calculated, True)

    n = len (matrix_tmp)
    m = len (matrix_tmp[0])

    for x, y, k in spiralWalkMatrix(m, n):
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
    
    #x, y, val = findMinCoordsSpiral(heightmap, calculated) 

    for x,y,k in spiralWalkMatrix(m,n,1):
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