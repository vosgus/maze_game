from vertex import Vertex
from edge import Edge

class Graph:
    
    def __init__ (self):
        self.vertices = []
        
    def addVertex(self, vertex):
        if vertex not in self.vertices:
            self.vertices.append(vertex)
            
    def addEdge(self, vertex_1, vertex_2):
        vertex_1.addAdjacent(vertex_2)
        vertex_2.addAdjacent(vertex_1)
        
    def removeEdge(self, vertex_1, vertex_2):
        vertex_1.removeAdjacent(vertex_2)
        vertex_2.removeAdjacent(vertex_1)
    
    def adjacent(self, vertex_1, vertex_2):
        return vertex_1.isAdjacent(vertex_2)
    
    def getVertex(self, index):
        return self.vertices[index]
    
    def getVertices(self):
        return self.vertices
        
    def getAdjacecyList(self, vertex):
        return vertex.getAdjacencyList()
    

# Prints out a n * n maze given a graph of the maze
def printMaze(graph, n):
    maze = ""
    middle = ""
    up = ""
    for i in range(0, n * n):           
        
        if i % n == 0:
            maze += middle + "#" + "\n"
            middle = ""
            maze += up + "\n"
            up = ""
        
        # Rows above and under the cells
        if (i + 1) % n != 0 and graph.adjacent(graph.getVertex(i), graph.getVertex(i + 1)):
            middle += "##"
            
        # Side walls to the cells
        if i < (n * n) - n and graph.adjacent(graph.getVertex(i), graph.getVertex(i + n)):
            up += "# "       
    
    # Add last row to maze
    maze += middle + "#" + "\n"
    
    print(maze)
    
def test():
    g = Graph()
    n = 15
    for i in range(0, n * n):
        v = Vertex(i)
        g.addVertex(v)
    
    # Create a fully connected maze graph
    for i in range(0, n * n):
        # Connect up
        if i > n - 1:
            g.addEdge(g.getVertex(i), g.getVertex(i - n))
        
        # Connect down
        if i < (n * n) - n:
            g.addEdge(g.getVertex(i), g.getVertex(i + n))
            
        # Connect right
        if i % n != (n - 1):
            g.addEdge(g.getVertex(i), g.getVertex(i + 1))
            
    for vertex in g.getVertices():
        out = str(vertex.data) + " -> [" 
        for adjVertex in g.getAdjacecyList(vertex):
            out += " " + str(adjVertex.data)
        out += " ]"
        print(out)
        
    printMaze(g, n)
        
test()