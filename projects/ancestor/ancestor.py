from graph import Graph
from util import Stack


def earliest_ancestor(ancestors, starting_node):
    


    tree = Graph()

    for each_set in ancestors:
        tree.add_vertex(each_set[0])
        tree.add_vertex(each_set[1])
        tree.add_edge(each_set[1], each_set[0])

    s = Stack()
    s.push([starting_node])
    longest_len = 1
    earliest_anc = -1
    visited = set()
    longest_path = []
    
    while s.size() > 0:
        path = s.pop()
        node = path[-1]

        if (len(path) >= longest_len and node < earliest_anc) or (len(path) > longest_len):
            earliest_anc = node
            longest_len = len(path)
        
        for ngbr in tree.vertices[node]:
            new_path = list(path)
            new_path.append(ngbr)
            s.push(new_path)
    return earliest_anc
