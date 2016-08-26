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
        
    def getVertices(self):
        return self.vertices
        
    def getAdjacecyList(self, vertex):
        return vertex.getAdjacencyList()
    

def test():
    g = Graph()
    v1 = Vertex("a")
    v2 = Vertex("b")
    v3 = Vertex("c")
    g.addVertex(v1)
    g.addVertex(v2)
    g.addVertex(v3)
    g.addEdge(v1, v2)
    g.addEdge(v2, v3)

    vertices = g.getVertices()

    for vertex in vertices:
        str = vertex.data + " -> [" 
        for adjVertex in g.getAdjacecyList(vertex):
            str += " " + adjVertex.data
        str += " ]"
        print(str)
        
test()