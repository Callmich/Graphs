from stack import Stack
from graph import Graph


# def earliest_ancestor(ancestors, starting_node):
#     longest_path = 0
#     ancestors = []
#     s = Stack()
#     visited = set()

#     def get_parent(vertx):
#     parents = []
#     for x in ancestors:
#         check = Graph.get_neighbor(x)
#         if check == vertx:
#             parents.append(x)
    


#     s.push([starting_node])
#     while s.size() > 0:
#         path = s.pop()
#         check_path = path[-1]

#         if check_path not in visited:
#             visited.add(check_path)
#         if len(check_path) > longest_path:
#             longest_path = len(check_path)
#             ancestors = [check_path]
#         elif len(check_path) == longest_path:
#             ancestors = ancestors.append(check_path)
        
#         for parent in get_parent(check_path):
#             new_node = list(path)
#             new_node.append(parent)
#             s.push(new_node)


def earliest_ancestor(ancestors, starting_node):
    

# I have a list of ancestors which are individual sets
# I either want to work up from the starting_node to the top or start at the top and try to find the starting_node
# the ancestors are in sets with the first being the parent and the second being the child.

# if I cycle through the node trying to find the starting node - if it is found I can store the pathway in a variable. At the end of the cycle I can find the longest pathway and return the first number in the first set.

    # if visited == None and path == None:
    #     visited = set()
    #     longest_path
    #     path = []
    
    # if len(ancestors) == 1:
    #     return path
    
    # for p_c in ancestors:
    #     print(p_c[0])
    tree = Graph()

    for each_set in ancestors:
        tree.add_vertex(each_set[0])
        tree.add_vertex(each_set[1])
        tree.add_edge(each_set[1], each_set[0])

    s = Stack()
    visited = set()
    longest_path = []
    longest_length = 0
    s.push(starting_node)

    while s.size() > 0:
        path = s.pop()
        node = path[-1]
        longest_path.append(node)
    
    return longest_path