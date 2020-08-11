"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy
from collections import deque # I want practice with actual Python libraries

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
            raise IndexError("Vertex does not exist")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        if vertex_id in self.vertices:
            return self.vertices[vertex_id]
        else:
            raise IndexError("Vertex does not exist")

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # Create a queue, add starting_vertex
        q = deque([starting_vertex])
        visited = set()

        while len(q) > 0:
            # Pull the next item from the queue and print it
            node = q.pop()
            if node not in visited:
                print(node)
                visited.add(node)

                # Add that node's connections to the queue
                for conn in self.vertices[node]:
                    if conn not in visited:
                        q.appendleft(conn)
                        visited.add(node)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # Create a stack, add starting_vertex
        stack = [starting_vertex]
        visited = set()

        while len(stack) > 0:
            # Pull the next item from the stack and print it
            node = stack.pop()
            if node not in visited:
                print(node)
                visited.add(node)

                # Add that node's connections to the stack
                for conn in self.vertices[node]:
                    if conn not in visited:
                        stack.append(conn)
                        visited.add(node)

    def dft_recursive(self, starting_vertex, visited=set()):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        # print starting vertex
        print(starting_vertex)
        visited.add(starting_vertex)

        # call dft on connections
        for conn in self.vertices[starting_vertex]:
            if conn not in visited:
                self.dft_recursive(conn, visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # create a queue and enqueue the path to starting_vertex
        q = deque()
        q.append([starting_vertex])
        visited = set()

        while len(q) > 0:
            # dequeue the next path
            path = q.pop()
            # grab the last vertex from that path
            v = path[-1]

            # check if the vertex has been visited
            if v not in visited:
                # is this the target?
                if v == destination_vertex:
                    return path  # return the path
                
                # mark it as visited
                visited.add(v)
                # add paths to its neighbors to the queue
                for conn in self.vertices[v]:
                    # make a copy and append the neighbor to the path
                    new_path = path.copy()
                    new_path.append(conn)
                    q.appendleft(new_path)

        # traversal finished and target not found
        return None


    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # create a stack and push the path to starting_vertex
        s = [[starting_vertex]]
        visited = set()
        
        while len(s) > 0:
            # pop the next path
            path = s.pop()
            # grab the last vertex from that path
            v = path[-1]

            # check if the vertex has been visited
            if v not in visited:
                # is this the target?
                if v == destination_vertex:
                    return path  # return the path
                
                # mark it as visited
                visited.add(v)
                # add paths to its neighbors to the stack
                for conn in self.vertices[v]:
                    # make a copy and append the neighbor to the path
                    new_path = path.copy()
                    new_path.append(conn)
                    s.append(new_path)
        
        # traversal finished and target not found
        return None

    def dfs_recursive(self, starting_vertex, destination_vertex,
                      visited=set(), path=[]):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        # add starting vertex to the path
        path.append(starting_vertex)
        visited.add(starting_vertex)

        # have we found the target?
        if starting_vertex == destination_vertex:
            return path

        # call dfs on each connection to starting_vertex
        for conn in self.vertices[starting_vertex]:
            if conn not in visited:
                p = self.dfs_recursive(conn, destination_vertex, visited, path.copy())
                if p is not None:
                    return p  # if a path was found, return it
        
        # traversal finished, destination not found
        return None

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
