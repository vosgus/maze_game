class Vertex:
    
    def __init__ (self, data):
        self.data = data
        self.adjacent = []
        
    def addAdjacent(self, Vertex):
        if Vertex not in self.adjacent:
            self.adjacent.append(Vertex)
        
    def getAdjacencyList(self):
        return self.adjacent
        
