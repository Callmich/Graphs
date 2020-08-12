from util import Stack


def earliest_ancestor(ancestors, starting_node):
    


    verts = {}

    for each_set in ancestors:
        if each_set[1] in verts.keys():
            verts[each_set[1]].append(each_set[0])
        else:
            verts[each_set[1]] = [each_set[0]]

    s = Stack()
    s.push([starting_node])
    longest_path = []
    
    while s.size() > 0:
        path = s.pop()
        v = path[-1]

        if v not in verts.keys():
            if v == starting_node:
                return -1

            if len(path) > len(longest_path):
                longest_path = path
            elif len(path) == len(longest_path):
                if v < longest_path[-1]:
                    longest_path = path
        else:
            for i in verts[v]:
                copy_path = path.copy()
                copy_path.append(i)
                s.push(copy_path)

    return longest_path[-1]