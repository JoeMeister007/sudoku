import tkinter as tk
import sudoku
import brian_sudoku
import joey_sudoku
import random
import datetime


class SodokuButton:

  def __init__(self, window, row, col, setInStone, currentVal = " ", bgc = "white"):
      self.row = row
      self.col = col
      self.setInStone = setInStone
      self.currentVal = currentVal
      self.button = tk.Button(window, text = currentVal, width = 2, height = 1, command = self.onClick, font = "Arial 20", highlightbackground = "black", bg = bgc)
      self.button.grid(row = self.row, column = self.col)

  def changeCurrentVal(self, newVal):
    self.currentVal = newVal
    self.button.config(text = self.currentVal)

    if not self.setInStone:
        self.button.config(fg = "blue")
  
  def onClick(self):
    global waitingCoords  
    if not self.setInStone:
      waitingCoords = [self.row, self.col]


# END CLASSES

def keypress(event):
  global waitingCoords
  nums = "123456789"
  #key = event.char.upper()
  key = event.keysym
  if jeff == 1:
    if key in ["BackSpace","Delete"]:
      grid[waitingCoords[0]][waitingCoords[1]].changeCurrentVal(" ")
      board[waitingCoords[0]][waitingCoords[1]] = 0
    elif nums.find(key) != -1:
      grid[waitingCoords[0]][waitingCoords[1]].changeCurrentVal(key)
      board[waitingCoords[0]][waitingCoords[1]] = int(key)

      if sudoku.checkForWin(board):
        print("You won!")

root = tk.Tk()
root.title("Sudoku by Brian and Joey")
root.bind("<Key>",keypress)
waitingCoords = []
jeff = 0

grid = []
for i in range(9):
  grid.append([])
  for j in range(9):
    if ( (i >=3 and  i <=5) and (j <= 2 or j >= 6) ) or ( (i <= 2 or i >= 6) and (j >= 3 and j <= 5)):
      grid[i].append(SodokuButton(root, i, j, False, " ", "light grey")) 
    else:
      grid[i].append(SodokuButton(root, i, j, False, " ",)) 

""" 
start = datetime.datetime.now()
board = brian_sudoku.generateBoard()
#while board == "error" or not sudoku.checkForWin(board):
while board == "error" or not joey_sudoku.checkForWin(board):
  board = brian_sudoku.generateBoard()
finish = datetime.datetime.now()
timeTook = finish - start
print("Brian's Board Generation Took",timeTook)
""" 
start = datetime.datetime.now()
board = joey_sudoku.genBoard()
#while not sudoku.checkForWin(board):
while not joey_sudoku.checkForWin(board):
  board = joey_sudoku.genBoard()
finish = datetime.datetime.now()
timeTook = finish - start
#print("Joey's Board Generation Took",timeTook)
print("Board Generation Took:",timeTook)

difficulty = input("Input Difficulty: Easy, Medium, or Hard? ").lower() #E: -46, M :-51, H :-66
#removeForDifficulty = {'easy':46,'medium':51,"hard":56}
removeForDifficulty = {'easy':23,'medium':25,"hard":28}

if difficulty not in removeForDifficulty:
  difficulty = "easy"
""" 
nums = list(range(40))
toBeRemoved  = random.sample(nums,removeForDifficulty[difficulty])
for i in toBeRemoved:
  r = i//9
  c = i % 9
  board[r][c] = 0
  board[8-r][8-c] = 0
""" 
spaces = []
for r in range(5):
  for c in range(9):
    spaces.append([r,c])

toBeRemoved = random.sample(spaces,removeForDifficulty[difficulty])
for i in range(len(toBeRemoved)):
  toBeRemoved.append([-(toBeRemoved[i][0] - 4)+4,-(toBeRemoved[i][1] - 4)+4])

for i in range(len(toBeRemoved)):
  board[toBeRemoved[i][0]][toBeRemoved[i][1]] = 0





#to get rotated one -4 from r and c, multiply by both by -1, add 4 once more.


""" 

if difficulty.lower() == "hard":
  for i in range(56):
    row = random.randint(0, 8)
    col = random.randint(0, 8)
    board[row][col] = 0
elif difficulty.lower() == "medium":
  for i in range(51):
    row = random.randint(0, 8)
    col = random.randint(0, 8)
    board[row][col] = 0
else:
  for i in range(46):
    row = random.randint(0, 8)
    col = random.randint(0, 8)
    board[row][col] = 0
"""
 

for r in range(len(board)):
  for c in range(len(board[r])):
    if board[r][c] != 0:
      grid[r][c].setInStone = True
      grid[r][c].changeCurrentVal(board[r][c])

jeff = 1


root.mainloop()
 

""" 
print("Testing the check for win functions on 100 boards...")

a = joey_sudoku.genBoard()
b = datetime.datetime.now() 
sudoku.checkForWin(a)
c = datetime.datetime.now()
old = c-b
b = datetime.datetime.now() 
joey_sudoku.checkForWin(a)
c = datetime.datetime.now()
new = c-b


for i in range(99):
  a = joey_sudoku.genBoard()
  b = datetime.datetime.now() 
  sudoku.checkForWin(a)
  c = datetime.datetime.now()
  old += c-b
  b = datetime.datetime.now() 
  joey_sudoku.checkForWin(a)
  c = datetime.datetime.now()
  new += c-b

print("Old check for win time: ",old)
print("New check for win time: ",new)
""" 
