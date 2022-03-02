import random

def genBoard():
    global board
    global left
    initStuff()
    while left > 0:
        fillOutOnlys()
        fillOutLeast()
    return board   

def initStuff():
    global board
    global columns
    global rows
    global squares
    global left

    board = []
    for i in range(9):
        board.append([])
        for j in range(9):
            board[i].append(0)

    columns = []
    for k in range(9):
        columns.append(list(range(1,10)))

    rows = []
    for crow in range(9):
        rows.append(list(range(1,10)))

    squares = []
    for r in range(3):
        squares.append([])
        for c in range(3):
            squares[r].append(list(range(1,10)))

    left = 81

def placeNumber(number,row,column): #purpose, put in the number and update remaining possible numbers for the row
    global board
    global columns
    global rows
    global squares
    global left
    if left > 0:
        """
        print("row:",row)
        print(rows[row])
        print("column:",column)
        print(columns[column])
        print(squares[row//3][column//3])
        """
        board[row][column] = number
        columns[column].remove(number)
        rows[row].remove(number)
        squares[row//3][column//3].remove(number)
        left -=1
    
def fillOutOnlys(): #purpose, fill out boxes with only one possibility. That way no breaky itself.
    global board
    global columns
    global rows
    global squares
    if left > 0:
        jeff = 0
        for index in range(0,81):
            row = index // 9
            column = index % 9
            if board[row][column] == 0:
                possibilities = []
                for i in range(1,10):
                    if i in rows[row] and i in columns[column] and i in squares[row//3][column//3]:
                        possibilities.append(i)
                """
                if len(rows[row]) == 1:
                    placeNumber(rows[row][0],row,column)
                    jeff = 1
                    break;
                elif len(columns[column]) == 1:
                    placeNumber(columns[column][0],row,column)
                    jeff = 1
                    break;
                elif len(squares[row//3][column//3]) == 1:
                    placeNumber(squares[row//3][column//3][0],row,column)
                    jeff = 1
                    break;
                """
                if len(possibilities) == 1:
                    placeNumber(possibilities[0],row,column)
                    jeff = 1
                    break;
        if jeff == 1: fillOutOnlys()

def fillOutLeast():
    global board
    global columns
    global rows
    global squares
    if left > 0:
        try:
            leastPoss = list(range(1,11))
            leastIn = []
            for i in range(81):
                r = i // 9
                c = i % 9
                if board[r][c] == 0:
                    leastIn.append(r)
                    leastIn.append(c)
                    break;
            for index in range(0,81):
                row = index // 9
                column = index % 9
                if board[row][column] == 0:
                    possibilities = []
                    for i in range(1,10):
                        if i in rows[row] and i in columns[column] and i in squares[row//3][column//3]:
                            possibilities.append(i)
                    if len(possibilities) < len(leastPoss):
                        leastPoss = possibilities
                        leastIn = []
                        leastIn.append(row)
                        leastIn.append(column)
                        #leastIn = [row,column]
            placeNumber(random.choice(leastPoss), leastIn[0], leastIn[1])
        except IndexError:
            genBoard()






def checkForWin(board):
    complete = set(range(1,10))
    squares = []
    for i in range(int(len(board)**.5)):
        squares.append([])
        for j in range(int(len(board)**.5)):
            squares[i].append([])
    for r in range(len(board)):
        if set(board[r]) != complete: return False
        column = []
        for c in range(len(board[r])):
            column.append(board[r][c])
            squares[r//3][c//3].append(board[r][c])
        if set(column) != complete: return False
    for h in range(len(squares)):
        for j in range(len(squares[h])):
            if set(squares[h][j]) != complete: return False
    return True

