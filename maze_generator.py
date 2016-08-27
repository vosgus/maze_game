# Library for maze generation algorithms 
# A graph is used for generation of mazes 

from graph.graph import Graph
from graph.vertex import Vertex

# Prints out a width * height maze given a graph of the maze
def printMaze(graph, width, height):
    maze = ""
    middle = ""
    up = ""
    for i in range(0, width * height):           
        
        if  i > 0 and i % width == 0:
            maze += middle + "#" + "\n"
            middle = ""
            maze += up + "\n"
            up = ""
        
        # Rows above and under the cells
        if (i + 1) % width != 0 and graph.adjacent(graph.getVertex(i), graph.getVertex(i + 1)):
            middle += "##"
            
        # Side walls to the cells
        if i < (width * height) - width and graph.adjacent(graph.getVertex(i), graph.getVertex(i + width)):
            up += "# "       
    
    # Add last row to maze
    maze += middle + "#" + "\n"
    
    print(maze, end="")

# Returns a graph of a fully connected maze of size width * height    
def generateFullMaze(width, height):
    g = Graph()
    for i in range(0, width * height):
        v = Vertex(i)
        g.addVertex(v)
    
    # Create a fully connected maze graph
    for i in range(0, width * height):
        # Connect up
        if i > width - 1:
            g.addEdge(g.getVertex(i), g.getVertex(i - width))
        
        # Connect down
        if i < (width * height) - width:
            g.addEdge(g.getVertex(i), g.getVertex(i + width))
            
        # Connect right
        if i % width != (width - 1):
            g.addEdge(g.getVertex(i), g.getVertex(i + 1))
    return g