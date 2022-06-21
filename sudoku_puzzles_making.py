import sys
import random
import itertools
random.seed(5180020) #random number

#####~~~~~~~~~~~~~~~~~~~~#####
##########################################Function part
def Makepuzzle(grid):
    puzzle = []
    for i in range(9):
        flag = 1
        for j in range(len(puzzle)):
            if puzzle[j]!=grid[i]:
                continue
            else:
                flag=0
                break
        if flag==1:
            puzzle.append(grid[i])
            
    puzzle.append(grid[len(grid)-1])
    return puzzle

def transRow123(row):
    for i in range(0,9):
        if i==0 or i==1 or i==2:
            row[i]=base[0][0]*3 + row[i] + 1
        elif i==3 or i==4 or i==5:
            row[i]=base[0][1]*3 + row[i] + 1
        elif i==6 or i==7 or i==8:
            row[i]=base[0][2]*3 + row[i] + 1
    return row

def transRow456(row):
    for i in range(0,9):
        if i==0 or i==1 or i==2:
            row[i]=base[1][0]*3 + row[i] + 1
        elif i==3 or i==4 or i==5:
            row[i]=base[1][1]*3 + row[i] + 1
        elif i==6 or i==7 or i==8:
            row[i]=base[1][2]*3 + row[i] + 1
    return row
    
def transRow789(row):
    for i in range(0,9):
        if i==0 or i==1 or i==2:
            row[i]=base[2][0]*3 + row[i] + 1
        elif i==3 or i==4 or i==5:
            row[i]=base[2][1]*3 + row[i] + 1
        elif i==6 or i==7 or i==8:
            row[i]=base[2][2]*3 + row[i] + 1
    return row

def diggingHole(grid, holes):
    holePercell = holes//9 #The number of holes on 1 cell
    holeFill9cell = holePercell*9
    holeresidual = holes - holeFill9cell #The number of holes left after completing the cells
    
    #Digging hole grid sudoku
    #cell1
    for i in range(0,holePercell):
        #Select a random cell that is not already empty
        row = random.randint(0,2)
        col = random.randint(0,2)
        while grid[row][col]==0:
            row = random.randint(0,2)
            col = random.randint(0,2)
            
        grid[row][col] = 0

    #cell2
    for i in range(0,holePercell):
        #Select a random cell that is not already empty
        row = random.randint(0,2)
        col = random.randint(3,5)
        while grid[row][col]==0:
            row = random.randint(0,2)
            col = random.randint(3,5)
            
        grid[row][col] = 0
        
    #cell3
    for i in range(0,holePercell):
        #Select a random cell that is not already empty
        row = random.randint(0,2)
        col = random.randint(6,8)
        while grid[row][col]==0:
            row = random.randint(0,2)
            col = random.randint(6,8)
            
        grid[row][col] = 0
    
    #cell4
    for i in range(0,holePercell):
        #Select a random cell that is not already empty
        row = random.randint(3,5)
        col = random.randint(0,2)
        while grid[row][col]==0:
            row = random.randint(3,5)
            col = random.randint(0,2)
            
        grid[row][col] = 0
    
    #cell5
    for i in range(0,holePercell):
        #Select a random cell that is not already empty
        row = random.randint(3,5)
        col = random.randint(3,5)
        while grid[row][col]==0:
            row = random.randint(3,5)
            col = random.randint(3,5)
            
        grid[row][col] = 0
    
    #cell6
    for i in range(0,holePercell):
        #Select a random cell that is not already empty
        row = random.randint(3,5)
        col = random.randint(6,8)
        while grid[row][col]==0:
            row = random.randint(3,5)
            col = random.randint(6,8)
            
        grid[row][col] = 0
    
    #cell7
    for i in range(0,holePercell):
        #Select a random cell that is not already empty
        row = random.randint(6,8)
        col = random.randint(0,2)
        while grid[row][col]==0:
            row = random.randint(6,8)
            col = random.randint(0,2)
            
        grid[row][col] = 0
    
    #cell8
    for i in range(0,holePercell):
        #Select a random cell that is not already empty
        row = random.randint(6,8)
        col = random.randint(3,5)
        while grid[row][col]==0:
            row = random.randint(6,8)
            col = random.randint(3,5)
            
        grid[row][col] = 0
    
    #cell9
    for i in range(0,holePercell):
        #Select a random cell that is not already empty
        row = random.randint(6,8)
        col = random.randint(6,8)
        while grid[row][col]==0:
            row = random.randint(6,8)
            col = random.randint(6,8)
            
        grid[row][col] = 0
    
    #Check holes residual
    while holeresidual>0:
        #Select a random cell that is not already empty
        row = random.randint(0,8)
        col = random.randint(0,8)
        while grid[row][col]==0:
            row = random.randint(0,8)
            col = random.randint(0,8)
            
        grid[row][col]=0
        holeresidual -= 1
    
    return grid


##########################################Start part
#Starting program

#Make basic Latin Square
grid = []
temp = []
block = [[0,1,2],
         [1,2,0],
         [2,0,1]]
perm = itertools.permutations(block)
for i in perm:  #row permutations
    temp.extend(i)
    if len(temp)==3:
        grid.extend([temp])
        temp = []
for perm in zip(itertools.permutations(block[0]), itertools.permutations(block[1]), itertools.permutations(block[2])): #column permutations
    temp.extend([perm])
for i in range(len(temp)):  #convert to list
    temp[i] = list(temp[i])
    for j in range(len(temp[0])):
        temp[i][j] = list(temp[i][j])
grid.extend(temp)

puzzle = Makepuzzle(grid) #Create puzzle with permutations from Latin Square was maked
random.shuffle(puzzle) #swap cells in puzzle
    
#Create grid for puzzle
#row1
row1 = []
row1.extend(puzzle[0][0])
row1.extend(puzzle[1][0])
row1.extend(puzzle[2][0])
#row2
row2 = []
row2.extend(puzzle[0][1])
row2.extend(puzzle[1][1])
row2.extend(puzzle[2][1])
#row3
row3 = []
row3.extend(puzzle[0][2])
row3.extend(puzzle[1][2])
row3.extend(puzzle[2][2])
#row4
row4 = []
row4.extend(puzzle[3][0])
row4.extend(puzzle[5][0])
row4.extend(puzzle[5][0])
#row5
row5 = []
row5.extend(puzzle[3][1])
row5.extend(puzzle[4][1])
row5.extend(puzzle[5][1])
#row6
row6 = []
row6.extend(puzzle[3][2])
row6.extend(puzzle[4][2])
row6.extend(puzzle[5][2])
#row7
row7 = []
row7.extend(puzzle[6][0])
row7.extend(puzzle[7][0])
row7.extend(puzzle[8][0])
#row8
row8 = []
row8.extend(puzzle[6][1])
row8.extend(puzzle[7][1])
row8.extend(puzzle[8][1])
#row9
row9 = []
row9.extend(puzzle[6][2])
row9.extend(puzzle[7][2])
row9.extend(puzzle[8][2])

#Each cell now has a pair of numbers.Treat these pairs as base 3 numbers, and convert to base 10, adding 1
'''base = [[2,1,0], #Example for base
        [1,0,2],
        [0,2,1]]'''

base=random.choice(grid) #random choice base from 12 latin squares was created

        
newRow1 = transRow123(row1)
newRow2 = transRow123(row2)
newRow3 = transRow123(row3)
newRow4 = transRow456(row4)
newRow5 = transRow456(row5)
newRow6 = transRow456(row6)
newRow7 = transRow789(row7)
newRow8 = transRow789(row8)
newRow9 = transRow789(row9)

sudogrid = [] #Generate a Grid
sudogrid.append(newRow1)
sudogrid.append(newRow2)
sudogrid.append(newRow3)
sudogrid.append(newRow4)
sudogrid.append(newRow5)
sudogrid.append(newRow6)
sudogrid.append(newRow7)
sudogrid.append(newRow8)
sudogrid.append(newRow9)

#Swap the 2nd & 4th rows, 3rd & 7th rows, and 6th & 8th rows to have perfect sudoku's grid 
swap24 = sudogrid[1]
sudogrid[1] = sudogrid[3]
sudogrid[3] = swap24

swap37 = sudogrid[2]
sudogrid[2] = sudogrid[6]
sudogrid[6] = swap37

swap68 = sudogrid[5]
sudogrid[5] = sudogrid[7]
sudogrid[7] = swap68

print('This is the sudoku grid:')
for i in sudogrid:
    print(i)
    
print()

##########################################End part  
paramters = sys.argv
k = int(paramters[1]) #Number of holes

copyGrid = [] #Take a full copy of the grid when you want backup
for row in range(0,9):
    copyGrid.append([])
    for column in range(0,9):
       copyGrid[row].append(sudogrid[row][column])

g = diggingHole(sudogrid, k) #digging hole
print('The content of output.txt file is as follows:')
for i in g:
    print(i)
#SaveResult
s = open(paramters[2], 'w')
result = []
for i in g:
    result.append(str(i))
s.write('\n'.join(result))

s.close()
    

#Example command-line to run program:  $python assignment_518h0020.py 9 output.txt
#'9' is the number of hole you want to digging from sudoku grid






