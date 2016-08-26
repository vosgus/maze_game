class Vertex:
    
    def __init__ (self, data):
        self.data = data
        self.adjacent = []
        
    def addAdjacent(self, vertex):
        if vertex not in self.adjacent:
            self.adjacent.append(vertex)
        
    def getAdjacencyList(self):
        return self.adjacent
        
