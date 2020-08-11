from stack import Stack

def earliest_ancestor(ancestors, starting_node):
    longest_path = 0
    ancestors = None
    s = Stack()
    visited = set()

    s.push([starting_node])
    while s.size() > 0:
        path = s.pop()
        check_path = path[-1]

        if check_path not in visited:
            visited.add(check_path)
        if len(check_path) > longest_path:
            longest_path = len(check_path)
            