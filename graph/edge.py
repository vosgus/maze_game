from vertex import Vertex

class Edge:
    
    def __init__ (self):
        self.v1 = None
        self.v2 = None
    
    def connect(self, v1, v2):
        self.v1 = v1
        self.v2 = v2
        