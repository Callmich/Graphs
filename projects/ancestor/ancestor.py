

class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertices(self, vert):
        if vert not in self.vertices:
            self.vertices[vert] = set()

    def add_edge(self, vertI, vertII):
        if vertI in self.vertices and vertII in self.vertices:
            self.vertices[vertI].add(vertII)
        else:
            raise IndexError("vertex does not exhist!")

    def get_neighbors(self, vert):
        return self.vertices[vert]


def create_graph(ancestors):
    graph = Graph()
    for p, c in ancestors:
        graph.add_vertices(p)
        graph.add_vertices(c)
        graph.add_edge(c, p)
    return graph

class Stack():
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None

    def size(self):
        return len(self.stack)


def earliest_ancestor(ancestors, starting_node):
    g = create_graph(ancestors)

    s = Stack()
    visited = set()
    s.push([starting_node])
    longest_path = []

    while s.size() > 0:
        path = s.pop()
        current_node = path[-1]

        if len(path) > len(longest_path):
            longest_path = path

        if current_node not in visited:
            visited.add(current_node)
            family = g.get_neighbors(current_node)

            for parent in family:
                new_path = path+[parent]
                s.push(new_path)
    if starting_node == longest_path[-1]:
        return -1
    else:
        return longest_path[-1]


