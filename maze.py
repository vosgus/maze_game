import time
import os
import random

# Reads in maze from text file and returns it
def getMaze(width, height, fileName):
    f = open(fileName, "r")
    maze = [[0 for x in range(width)] for y in range(height)]

    width, height = 0, -1
    for line in f:
        height += 1
        width = 0
        for char in line:
            maze[height][width] = char
            width += 1
    return maze

def getAction():
    return input()[0]
        

# Checks if move is legal
def legalMove(direction, maze, human_position):
    human_x, human_y = human_position[0], human_position[1]

    if direction == 'w':
        return (maze[human_x - 1][human_y] != '#' and human_x - 1 > 0)
    if direction == 'a':
        return (maze[human_x][human_y - 1] != '#' and human_y - 1 > 0)
    if direction == 's':
        return (maze[human_x + 1][human_y] != '#' and human_x + 1 < 23)
    if direction == 'd':
        return (maze[human_x][human_y + 1] != '#' and human_y + 1 < 74)
    else:
        return False

def canPush(direction, maze, human_position):
    human_x, human_y = human_position[0], human_position[1]
    
    # todo list index goes out of ronge, needs to check
    if direction == 'w':
        return (maze[human_x - 1][human_y] == '#' and maze[human_x - 2][human_y] != '#' and human_x - 2 > 0)
    if direction == 'a':
        return (maze[human_x][human_y - 1] == '#' and maze[human_x][human_y - 2] != '#' and human_y - 2 > 0)
    if direction == 's':
        return (maze[human_x + 1][human_y] == '#' and maze[human_x + 2][human_y] != '#' and human_x + 2 < 23) 
    if direction == 'd':
        return (maze[human_x][human_y + 1] == '#' and maze[human_x][human_y + 2] != '#' and human_y + 2 < 74)
        
def drawMaze(maze, width, height):
    for x in range(height):
        for y in range(width):
            print(maze[x][y], end="")
        
def move(direction, human_position):
    if direction == 'w':
        human_position[0] -= 1
    if direction == 'a':
        human_position[1] -= 1
    if direction == 's':
        human_position[0] += 1
    if direction == 'd':
        human_position[1] += 1

def push(maze, direction, human_position):   
    human_x, human_y = human_position[0], human_position[1]
 
    if direction == 'w':
        clearBlock(maze, human_x - 1, human_y)
        addToBlock(maze, '#', human_x - 2, human_y)
    if direction == 'a':
        clearBlock(maze, human_x, human_y - 1)
        addToBlock(maze, '#', human_x, human_y - 2)
    if direction == 's':
        clearBlock(maze, human_x + 1, human_y)
        addToBlock(maze, '#', human_x + 2, human_y)
    if direction == 'd':
        clearBlock(maze, human_x, human_y + 1)
        addToBlock(maze, '#', human_x, human_y + 2)
        
def clearBlock(maze, x, y):
    maze[x][y] = ' '

def addToBlock(maze, entity, x, y):
    maze[x][y] = entity
   
# Generates a list of n trolls
def generateTrolls(n, maze):
    trolls = [[0 for x in range(0, n)] for x in range(0, n)]
    
    for i in range(0, n):
        position = randomPosition()
        while not validSpawn(maze, position[0], position[1]):
            position = randomPosition()
        trolls[i] = position
    return trolls

def validSpawn(maze, x, y):
    return (maze[x][y] != '#')
    
def addTrolls(maze, trolls):
    for i in range(0, len(trolls)):
        addToBlock(maze, '@', trolls[i][0], trolls[i][1])
        
def randomPosition():
    return [random.randint(1, 21), random.randint(1, 72)] 
    
def clearScreen():
    clear = lambda: os.system('cls')
    clear()
    
width, height = 74, 23    
maze = getMaze(width, height, "maze_ascii.txt");
human = '&'
human_position = [0, 0]
human_position[0], human_position[1] = 1, 1
maze[human_position[0]][human_position[1]] = human
trolls = generateTrolls(2, maze)
addTrolls(maze, trolls)

while (True):
    # First we draw the maze
    clearScreen()
    drawMaze(maze, width, height);
    
    # Get player to move
    action = getAction()
    
    if (action in "wasd" and legalMove(action, maze, human_position)):
        clearBlock(maze, human_position[0], human_position[1])
        move(action, human_position)
        addToBlock(maze, human, human_position[0], human_position[1])        
    elif (action in "wasd" and canPush(action, maze, human_position)):
        print("canpush")
        push(maze, action, human_position)
        
        
  

       

    
