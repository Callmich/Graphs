from stack import Stack
from graph import Graph


def earliest_ancestor(ancestors, starting_node):
    longest_path = 0
    ancestors = []
    s = Stack()
    visited = set()

    def get_parent(vertx):
    parents = []
    for x in ancestors:
        check = Graph.get_neighbor(x)
        if check == vertx:
            parents.append(x)
    


    s.push([starting_node])
    while s.size() > 0:
        path = s.pop()
        check_path = path[-1]

        if check_path not in visited:
            visited.add(check_path)
        if len(check_path) > longest_path:
            longest_path = len(check_path)
            ancestors = [check_path]
        elif len(check_path) == longest_path:
            ancestors = ancestors.append(check_path)
        
        for parent in get_parent(check_path):
            new_node = list(path)
            new_node.append(parent)
            s.push(new_node)
            