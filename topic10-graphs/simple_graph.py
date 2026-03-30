

class Vertex:
    def __init__(self, value):
        self.value = value 
        self.edges = []

    def __str__(self):
        s = self.value + " ["
        for e in self.edges:
            s += e.vertex.value
        s += "]"
        return s
    
    def add_connection(self, vertex):
        self.edges.append(Edge(vertex))

    
class Edge:
    def __init__(self, vertex):
        self.vertex = vertex 
        self.weight = 1

    
class Graph:
    def __init__(self):
        self.vertices = []

    def add_vertex(self, value):
        self.vertices.append(Vertex(value))

    def get_vertex(self, value):
        for v in self.vertices:
            if v.value == value:
                return v 
        return None
    
    def connect_many(self, v1, *args):
        for arg in args:
            self.connect(v1, arg)

    def connect(self, v1, v2):
        vertex1 = self.get_vertex(v1)
        vertex2 = self.get_vertex(v2)
        if vertex1 is not None and vertex2 is not None:
            vertex1.add_connection(vertex2)
            vertex2.add_connection(vertex1)
        else:
            print("One or both vertices not found")

    def display(self):
        for v in self.vertices:
            print(v)

    

values = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K"]   

graph = Graph()
for value in values:
    graph.add_vertex(value)

graph.connect_many("A", "B", "C", "E", "G")
graph.connect_many("B", "D")
graph.connect_many("C", "F", "D")
graph.connect_many("D", "F")
graph.connect_many("E", "E", "F")
graph.connect_many("F", "G", "H")
graph.connect_many("G", "H")
graph.connect_many("J", "K")

graph.display()
