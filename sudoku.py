import random

def checkColumn(twodArray,columnnum):
    column = []
    for e in range(len(twodArray)):
        column.append(twodArray[e][columnnum])
    column.sort()
    previous =  column[0]
    for i in range(1,len(column)):
        if column[i] == previous and column[i] != 0:
            return False #you lost
        previous = column[i]
    return True

def checkForDuplicates(board):
    tests = []
    for c in range(9):
        tests.append(checkColumn(board,c))
    for sr in range(3):
        for sc in range(3):
            tests.append(checkSquare(board,sr,sc))
    for r in range(9):
        tests.append(checkRow(board,r))
    if False in tests:
        return True #duplicate found
    return False #no duplicate found

def checkForWin(twodArray):
    if checkFor0s(twodArray):
        return False #no win
    elif checkForDuplicates(twodArray):
        return False #no win
    return True #win

def checkFor0s(twodArray):
    for r in range(len(twodArray)):
        for c in range(len(twodArray[r])):
            if twodArray[r][c] == 0:
                return True #zerofound
    return False

def checkRow(twodArray,rownum): #kinda useless cause row's are already gonna be fine
    unalteredRow = twodArray[rownum]
    row = []
    for s in unalteredRow:
        row.append(s)
    row.sort()
    previous =  row[0]
    for i in range(1,len(row)):
        if row[i] == previous and row[i] != 0:
            return False #you lost
        previous = row[i]
    return True

def checkSquare(twodArray,squareRow,squareColumn): #for first square do 0,0 for second square do 0,1 then 0,2 then 1,0 and so on
    square = []
    squareRow *=3
    squareColumn *=3
    for r in range(squareRow,squareRow+3):
        for c in range(squareColumn,squareColumn+3):
            square.append(twodArray[r][c])
    square.sort()
    previous = square[0]
    for i in range(1,len(square)):
        if square[i] == previous and square[i] !=0:
            return False #you lost
        previous = square[i]
    return True
                   
def generateBoard():
    board = []
    initializeBoard(board)
    board[0] = generateRow()
    i=0
    while i < 9:#can change this later if we want it to work for different sizes
        tests = []
        board[i] = generateRow()
        if checkForDuplicates(board) == False:
            i += 1
    return board

def generateBoardFromSeed(seed):
    board = [[],[],[],[],[],[],[],[],[]]
    if len(seed) != 81:
        print("Invalid Seed, Must Be Of Length 81")
        print("Generating Random Board Instead")
        return generateBoard()
    elif seed.isdigit() != True:
        print("Invalid Seed, Must Be Composed Of All Digits")
        print("Generating Random Board Instead")
        return generateBoard()        
    for i in range(len(seed)):
        row = i//9
        board[row].append(int(seed[i]))
    tests = []
    if checkForDuplicates(board) == True:
        print("Invalid Seed, Two Of The Same Number In A Row, Column, Or Square")
        print("Generating Random Board Instead")
        return generateBoard()     
    return board

def generateRow(): #only for 9x9
    possible = [1,2,3,4,5,6,7,8,9]
    howManyToDraw = [1,2,3,4,5]
    weights = [.05,.2,.5,.2,.05]
    numToPick = random.choices(howManyToDraw,weights)[0]
    nums = random.sample(possible,numToPick)
    for i in range(9-numToPick):
        nums.append(0)
    random.shuffle(nums)
    return nums

def generateSeed(board):
    seed = ""
    for r in range(len(board)):
        for c in range(len(board[r])):
            seed+= str(board[r][c])
    return seed

def initializeBoard(emptyBoard,rows = 9, columns = 9):
    for i in range(rows):
        emptyBoard.append([])
        for y in range(columns):
            emptyBoard[i].append(0)

def printArray(twodArray): #useful for testing
    for l in range(len(twodArray)):
        for e in range(len(twodArray[l])):
            print(twodArray[l][e],end=' ')
        print()