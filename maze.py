import time
import os
import random
import maze_generator

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

def clearEntitities(maze, entities):
    for entity in entities:
        clearBlock(maze, entity[0], entity[1])
        
def clearBlock(maze, x, y):
    maze[x][y] = ' '

def addToBlock(maze, figure, x, y):
    maze[x][y] = figure
    
def addEntity(maze, figure, entityPosition):
    maze[entityPosition[0]][entityPosition[1]] = figure
   
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
    
def addEntities(maze, figure, entities):
    for entity in entities:
        addEntity(maze, figure, entity)
        
def moveTrolls(maze, trolls):
    for troll in trolls:
        direction = randomDirection()
        while not legalMove(direction, maze, troll):
            direction = randomDirection()
        move(direction, troll)

def randomDirection():
    return "wasd"[random.randint(0, 3)]
        
def randomPosition():
    return [random.randint(1, 21), random.randint(1, 72)] 

def checkWin(maze, human_position, goalPosition):
    return human_position == goalPosition
    
def clearScreen():
    clear = lambda: os.system('cls')
    clear()
  
def run():
    goalPosition = [22, 2]    
    width, height = 74, 23    
    maze = getMaze(width, height, "maze_ascii.txt");
    human = '&'
    human_position = [0, 0]
    human_position[0], human_position[1] = 1, 1
    maze[human_position[0]][human_position[1]] = human
    trolls = generateTrolls(10, maze)
    addEntities(maze, '@', trolls)

    while (True):
        # First we draw the maze
        clearScreen()
        drawMaze(maze, width, height);
        
        # Get player to move
        action = getAction()
        
        if (action in "wasd" and legalMove(action, maze, human_position)):
            clearBlock(maze, human_position[0], human_position[1])
            move(action, human_position)
            addEntity(maze, human, human_position)        
        elif (action in "wasd" and canPush(action, maze, human_position)):
            print("canpush")
            push(maze, action, human_position)
            
        clearEntitities(maze, trolls)
        moveTrolls(maze, trolls)
        addEntities(maze, '@', trolls)
            
        if (checkWin(maze, human_position, goalPosition)):
            print("You made it to the end!!")
            break
    
def testMazeGenerator():
    w, h = 70, 25
    mazeGraph = maze_generator.generateFullMaze(w, h)
    maze_generator.binaryMaze(mazeGraph, w, h)

testMazeGenerator()
    
    
