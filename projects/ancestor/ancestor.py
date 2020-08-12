from graph import Graph
from util import Stack


def earliest_ancestor(ancestors, starting_node):
    


    tree = Graph()

    for each_set in ancestors:
        tree.add_vertex(each_set[0])
        tree.add_vertex(each_set[1])
        tree.add_edge(each_set[1], each_set[0])

    s = Stack()
    visited = set()
    longest_path = []
    s.push([starting_node])

    while s.size() > 0:
        path = s.pop()
        node = path[-1]

        if len(path) > len(longest_path):
            longest_path = path
        
        if node not in visited:
            visited.add(node)
            ps = tree.get_neighbors(node)

            for p in ps:
                new_path = path+[p]
                s.push(new_path)
    if starting_node == longest_path[-1]:
        return -1
    else:
        return longest_path[-1]
