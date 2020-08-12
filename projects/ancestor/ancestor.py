# from util import Stack


# def earliest_ancestor(ancestors, starting_node):

#     verts = {}

#     for each_set in ancestors:
#         if each_set[1] in verts.keys():
#             verts[each_set[1]].append(each_set[0])
#         else:
#             verts[each_set[1]] = [each_set[0]]

#     s = Stack()
#     s.push([starting_node])
#     longest_path = []
    
#     while s.size() > 0:
#         path = s.pop()
#         v = path[-1]

#         if v not in verts.keys():
#             if v == starting_node:
#                 return -1

#             if len(path) > len(longest_path):
#                 longest_path = path
#             elif len(path) == len(longest_path):
#                 if v < longest_path[-1]:
#                     longest_path = path
#         else:
#             for i in verts[v]:
#                 copy_path = path.copy()
#                 copy_path.append(i)
#                 s.push(copy_path)

#     return longest_path[-1]

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

class Graph:
    def __init__(self):
        self.verticies = {}
    
    def add_verts(self, vert):
        if vert not in self.verticies:
            self.verticies[vert] = set()
    
    def add_edge(self, v1, v2):
        self.verticies[v1].add(v2)

    def get_neighbors(self, vert):
        return self.verticies[vert]

def create_graph(lst):
    graph = Graph()
    for pair in lst:
        graph.add_verts(lst[0])
        graph.add_verts(lst[1])
        graph.add_edge(lst[1], lst[0])
    return graph

def earliest_ancestor(ancestors, starting_node):
    g = create_graph(ancestors)

    s = Stack()
    visited = set()
    s.push([starting_node])
    big_path = []
