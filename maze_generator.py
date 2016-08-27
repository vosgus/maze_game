# Library for maze generation algorithms 
# A graph is used for generation of mazes 

from graph.graph import Graph
from graph.vertex import Vertex
import random

# Prints out a width * height maze given a graph of the maze
def printMaze(graph, width, height):
    maze = ""
    middle = ""
    up = ""
    for row in range(0, height):
        for col in range(0, width):
            vertex_1D = width * row + col
            
            # Cell top and bottom walls
            if vertex_1D < width * height:
                if col + 1 == width: # Corner case for the last wall piece
                    middle += "#"
                elif graph.adjacent(graph.getVertex(vertex_1D), graph.getVertex(vertex_1D + 1)):
                    middle += "##"
                elif col == 0:
                    middle += "# "
                else:
                    middle += "  "
                
            # Cell side walls, skip last row
            if vertex_1D < (width * height) - width:
                if graph.adjacent(graph.getVertex(vertex_1D), graph.getVertex(vertex_1D + width)) or col == 0:
                    up += "# "
                else:
                    up += "  "
                
        maze += middle + "\n" + up + "\n"
        middle = ""
        up = ""
    
    print(maze, end="")

# Binary Tree algorithm for generating a maze
# Returns a random maze given som bias.
def binaryMaze(graph, width, height):
    for row in range(1, height - 1):
        for col in range(1, width - 1):
            # formula for 2D -> 1D, width * row + col
            vertex_1D = width * row + col
            if random.randint(0, 1) == 1:    
                graph.removeEdge(graph.getVertex(vertex_1D), graph.getVertex(vertex_1D + width))
            else:
                graph.removeEdge(graph.getVertex(vertex_1D), graph.getVertex(vertex_1D - 1))
    printMaze(graph, width, height)
    
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