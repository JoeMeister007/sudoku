import random

def copyArray(arr1):
    outArray = []
    
    for i in range(len(arr1)):
        outArray.append([])
        for j in range(len(arr1[i])):
            outArray[i].append(arr1[i][j])

    return outArray

def printArray(array):
    for i in range(len(array)):
        for j in range(len(array[i])):
            print(array[i][j], end = " ")
        print("")
    print("")
    
def compareArray(arr1, arr2):
    for i in range(len(arr1)):
        for j in range(len(arr1[i])):
            if arr2[i][j] != arr1[i][j]:
                return False
    return True

def checkSquare(r, c, num, arr):
    placeholder = copyArray(arr)
    
    start_r = r // 3 * 3
    start_c = c // 3 * 3

    for i in range(start_r, start_r + 3):
        for j in range(start_c, start_c+3):
            if placeholder[i][j] == num:
                return True
    return False


def placeNumber(num):
    global board, available
    
    placeholder = copyArray(board)
    spaces = copyArray(available)

    usedCols = []
    usedRows = []
    
    for i in range(9):
        attempts = 0
    
        space = random.choice(spaces)
        row = space[0]
        col = space[1]

        while row in usedRows or col in usedCols or checkSquare(row, col, num, placeholder):
            space = random.choice(spaces)
            row = space[0]
            col = space[1]

            if attempts >= 1000:
                return False

            attempts += 1

        usedCols.append(col)
        usedRows.append(row)
        spaces.remove(space)
        placeholder[row][col] = num
        
    board = copyArray(placeholder)
    available = copyArray(spaces)
    return True
        

def generateBoard():
    global board, available
    board = []

    for i in range(9):
        board.append([])
        for j in range(9):
            board[i].append(0)

    available = []

    for i in range(9):
        for j in range(9):
            available.append([i, j])


    for i in range(1, 10):
        attempt = 0
        while not placeNumber(i):
            attempt += 1
            if attempt >= 1000:
                return "error"
    return board
