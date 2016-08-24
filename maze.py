import time
import os

def getMove():
    return input()[0]

def legalMove(direction, maze, human_x, human_y):
    if direction == 'w':
        return (maze[human_x - 1][human_y] != '#' and human_x - 1 > 0)
    if direction == 'a':
        return (maze[human_x][human_y - 1] != '#' and human_y - 1 > 0)
    if direction == 's':
        return (maze[human_x + 1][human_y] != '#' and human_x - 1 > 0)
    if direction == ''
        

def move(x, y):
    return
    
f = open("maze_ascii.txt", "r");
w, h = 74, 23;
maze = [[0 for x in range(w)] for y in range(h)]

w, h = 0, -1
for line in f:
    h += 1
    w = 0
    for char in line:
        maze[h][w] = char
        w += 1
        
human = "^"
maze[2][2] = human

for x in range(23):
    for y in range(74):
        print(maze[x][y], end="")

#time.sleep(3)
#clear = lambda: os.system('cls')    
  
print(legalMove(getMove(), maze, 2, 2)) 
  

       

    
