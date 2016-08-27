from . import vertex
from . import edge

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
        
    def printAdjacencyList(self):
        out = ""
        for vertex in self.vertices:
            out += str(vertex.data) + " -> [ "
            for adjVertex in vertex.getAdjacencyList():
                out += str(adjVertex.data) + " "
            out += "]\n"
            print(out, end="")
            out = ""
    