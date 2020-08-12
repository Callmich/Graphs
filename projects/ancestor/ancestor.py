

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

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("vertex does not exhist!")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # create an empty queue and enqueue a starting vertex
        q = Queue()
        q.enqueue(starting_vertex)

        # create a set to store visited verts
        visited = set()

        # while queue is not empty
        while q.size() > 0:
            # dequeue the first vertex
            v = q.dequeue()
            # if vertext has not been visited 
            if v not in visited:
                print(v)
                visited.add(v)
                # print for debugging
                
                # add all neighbors to back of the queue
                for next_vert in self.get_neighbors(v):
                    q.enqueue(next_vert)


    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # create an empty stack push a starting vertex
        s = Stack()
        s.push(starting_vertex)

        # create a set to store visited verts
        visited = set()
        # while stack is not empty
        while s.size() > 0:
            # pop the first vert
            v = s.pop()
            # if vert has not been visited
            if v not in visited:
                # mark vert as visited
                visited.add(v)
                # print for debug
                print(v)
                # push all neighbors to the top of the stack
                for next_vertex in self.get_neighbors(v):
                    s.push(next_vertex)

    def dft_recursive(self, starting_vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        if visited == None:
            visited = set()
        
        if starting_vertex not in visited:
            visited.add(starting_vertex)
            print(starting_vertex)

            for nbrs in self.get_neighbors(starting_vertex):
                self.dft_recursive(nbrs, visited)
        

        

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        queue = Queue()
        queue.enqueue([starting_vertex])

        visited = set()

        while queue.size() > 0:
            path = queue.dequeue()

            vert = path[-1]

            if vert not in visited:
                visited.add(vert)

                if vert == destination_vertex:
                    return path
                
                else:
                    for ngbr in self.get_neighbors(vert):
                        new_path = list(path)
                        new_path.append(ngbr)
                        queue.enqueue(new_path)
        return None

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        stack = Stack()

        stack.push([starting_vertex])

        visited = set()

        while stack.size() > 0:
            path = stack.pop()

            vert = path[-1]

            if vert not in visited:
                visited.add(vert)
            if vert == destination_vertex:
                return path
            else:
                for ngbr in self.get_neighbors(vert):
                    new_path = list(path)
                    new_path.append(ngbr)
                    stack.push(new_path)

    def dfs_recursive(self, starting_vertex, destination_vertex, visited=None, path=None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        if visited == None and path == None:
            visited = set()
            path = []
        
        if starting_vertex not in visited:
            new_path = list(path)
            new_path.append(starting_vertex)

            visited.add(starting_vertex)

            if starting_vertex == destination_vertex:
                return new_path
            
            for ngbr in self.get_neighbors(starting_vertex):
                next_path = self.dfs_recursive(ngbr, destination_vertex, visited, new_path)
                if next_path:
                    return next_path

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
