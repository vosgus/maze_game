class Vertex:
    
    def __init__ (self, data):
        self.data = data
        self.adjacent = []
        
    def addAdjacent(self, vertex):
        if vertex not in self.adjacent:
            self.adjacent.append(vertex)
            
    def isAdjacent(self, vertex):
        return (vertex in self.adjacent)
            
    def removeAdjacent(self, vertex):
        if vertex in self.adjacent:
            self.adjacent.remove(vertex)
        
    def getAdjacencyList(self):
        return self.adjacent
        
