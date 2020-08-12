from util import Stack


def earliest_ancestor(ancestors, starting_node):
    


    verts = {}

    for each_set in ancestors:
        if each_set[1] in verts.keys():
            verts[each_set[1]].append(each_set[0])
        else:
            verts[each_set[1] = each_set[0]]

    s = Stack()
    s.push([starting_node])
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
