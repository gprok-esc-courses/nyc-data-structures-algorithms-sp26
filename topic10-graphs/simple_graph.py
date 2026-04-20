import sys

class Vertex:
    def __init__(self, value):
        self.value = value 
        self.edges = []
        # vars for BFS 
        self.color = None 
        self.parent = None
        self.distance = sys.maxsize

    # A d:0 [B C E G ]
    def __str__(self):
        parent = "None" if self.parent is None else self.parent.value
        s = self.value + " d:" + str(self.distance) + " p:" + parent + " ["
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

    def init_vertices(self):
        for vertex in self.vertices:
            vertex.parent = None
            vertex.color = 'white'
            vertex.distance = sys.maxsize

    def bfs(self, starting_value):
        self.init_vertices()
        vertex = self.get_vertex(starting_value)
        if vertex is None:
            print(f"{starting_value} not in the Graph")
        else:
            q = []
            vertex.distance = 0
            vertex.color = 'gray'
            q.append(vertex)
            while len(q) > 0:
                vertex = q.pop(0)
                for connection in vertex.edges:
                    v = connection.vertex
                    if v.color == 'white':
                        v.distance = vertex.distance + 1
                        v.color = 'gray'
                        v.parent = vertex
                        q.append(v)
                vertex.color = 'black'

    def print_path(self, start_value, dest_value):
        start = self.get_vertex(start_value)
        dest = self.get_vertex(dest_value) 
        if start is None or dest is None:
            print("One or both vertices not found")
        else:
            self.print_path_recursive(start, dest)
            print()

    def print_path_recursive(self, start, dest):
        if start == dest:
            print(start.value, end=' ')
        elif dest.parent is None:
            print(f"No path to {start.value} from {dest.value}")
        else:
            self.print_path_recursive(start, dest.parent)
            print(dest.value, end=' ')
            




values = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K"]   

graph = Graph()
for value in values:
    graph.add_vertex(value)

graph.connect_many("A", "B", "C", "E")
graph.connect_many("B", "D")
graph.connect_many("C", "F", "D")
graph.connect_many("D", "F")
graph.connect_many("E", "F")
graph.connect_many("F", "G", "H")
graph.connect_many("G", "H")
graph.connect_many("J", "K")

graph.bfs("A")
graph.print_path("A", "H")

graph.display()
