# Name 1: John Reynoldson
# EID 1: jsr3598

# Name 2:
# EID 2:

import sys
from collections import deque

class Stack:
    """Stack implementation as a list"""

    def __init__(self):
        """Create new stack"""
        self.items = []

    def peek(self):
        """Get the value of the top item in the stack"""
        if self.is_empty():
            raise IndexError("Peek from empty stack")
        return self.items[-1]

    def push(self, item):
        """Add an item to the stack"""
        self.items.append(item)

    def pop(self):
        """Remove an item from the stack"""
        if self.is_empty():
            raise IndexError("Pop from empty stack")
        return self.items.pop()

    def is_empty(self):
        """Check if the stack is empty"""
        return not self.items

    def __str__(self):
        """String representation of the stack"""
        return str(self.items)

class Queue:
    """Queue class for search algorithms."""
    def __init__(self):
        self.q = deque()

    def peek(self):
        """Get the front element of the queue."""
        if self.is_empty():
            raise IndexError("Peek from empty queue")
        return self.q[0]

    def enqueue(self, item):
        """Add an item to the end of the queue."""
        self.q.append(item)

    def dequeue(self):
        """Remove and return the front element of the queue."""
        if self.is_empty():
            raise IndexError("Dequeue from empty queue")
        return self.q.popleft()

    def is_empty(self):
        """Check if the queue is empty."""
        return not self.q

    def __str__(self):
        """String representation of the queue"""
        return str(self.q)

class Vertex:
    """Vertex Class using properties and setters for better encapsulation."""

    def __init__(self, label):
        self.__label = label
        self.visited = False

    @property
    def visited(self):
        """Property to get the visited status of the vertex."""
        return self.__visited

    @visited.setter
    def visited(self, value):
        """Setter to set the visited status of the vertex."""
        if isinstance(value, bool):
            self.__visited = value
        else:
            raise ValueError("Visited status must be a boolean value.")

    @property
    def label(self):
        """Property to get the label of the vertex."""
        return self.__label

    def __str__(self):
        """String representation of the vertex"""
        return str(self.__label)


class Graph:
    """A Class to present Graph."""

    def __init__(self):
        self.vertices = []  # a list of vertex objects
        self.adjacency_matrix = []  # adjacency matrix of edges

    def has_vertex(self, label):
        """Check if a vertex is already in the graph"""
        num_vertices = len(self.vertices)
        for i in range(num_vertices):
            if label == self.vertices[i].label:
                return True
        return False

    def get_index(self, label):
        """Given a label get the index of a vertex"""
        num_vertices = len(self.vertices)
        for i in range(num_vertices):
            if label == self.vertices[i].label:
                return i
        return -1

    def add_vertex(self, label):
        """Add a Vertex with a given label to the graph"""
        if self.has_vertex(label):
            return

        # add vertex to the list of vertices
        self.vertices.append(Vertex(label))

        # add a new column in the adjacency matrix
        num_vertices = len(self.vertices)
        for i in range(num_vertices - 1):
            self.adjacency_matrix[i].append(0)

        # add a new row for the new vertex
        new_row = []
        for i in range(num_vertices):
            new_row.append(0)
        self.adjacency_matrix.append(new_row)

    def add_edge(self, start, finish):
        """Add unweighted directed edge to graph"""
        self.adjacency_matrix[start][finish] = 1

    def get_adjacent_vertices(self, vertex_index):
        """Return adjacent vertex indices to vertex_index"""
        vertices = []
        num_vertices = len(self.vertices)
        for j in range(num_vertices):
            if self.adjacency_matrix[vertex_index][j]:
                vertices.append(j)
        return vertices

    # Determine whether or no the graph has a cycle
    # Return as a boolean value
    def has_cycle(self):

        visited = [False] * len(self.vertices)
        rec_stack = [False] * len(self.vertices)

        def dfs(vertex):
            visited[vertex] = True
            rec_stack[vertex] = True

            for neighbor in self.get_adjacent_vertices(vertex):
                if not visited[neighbor]:
                    if dfs(neighbor):
                        return True
                elif rec_stack[neighbor]:
                    return True
                
            rec_stack[vertex] = False
            return False
        
        for vertex_index in range(len(self.vertices)):
            if not visited[vertex_index]:
                if dfs(vertex_index):
                    return True

        return False

    # Return a valid ordering of courses to take for registration as a list of vertex labels.
    # This method assumes that there is a valid registration plan.
    def get_registration_plan(self):

        # Because we don't want to destroy the original graph,
        # we have defined helper functions that work with a copy of the
        # adjacency matrix and vertices. This is also a hint that we
        # suggest you to manipulate the graph copy to solve this method.

        # We encourage you to use these variables and functions, although
        # if you come up with a solution that doesn't, you may delete them.
        temp_vertices = list(self.vertices)
        temp_matrix = [row[:] for row in self.adjacency_matrix]
        

        def get_index_from_copy(label, vertices_copy):
            """Given a label get the index of a vertex in the copy of the vertices list"""
            for i, vertex in enumerate(vertices_copy):
                if vertex.label == label:
                    return i
            return -1

        def delete_vertex_from_copy(vertex_label, adjacency_matrix_copy, vertices_copy):
            """delete vertex from the copy of the adjacency matrix and vertices list"""
            index = get_index_from_copy(vertex_label, vertices_copy)

            for row in adjacency_matrix_copy:
                del row[index]
            del adjacency_matrix_copy[index]
            del vertices_copy[index]

        courses = []

        while temp_vertices:
            no_incoming_edges = None
            for vertex in temp_vertices:
                index = get_index_from_copy(vertex.label, temp_vertices)
                if not any(row[index] for row in temp_matrix):
                    no_incoming_edges = vertex
                    break
            if not no_incoming_edges:
                break

            courses.append(no_incoming_edges.label)
            delete_vertex_from_copy(no_incoming_edges.label, temp_matrix, temp_vertices)

        return courses

# Read the input file and construct the graph. The output code has been written for you.
def main():
    # create a Graph object
    graph = Graph()

    # read the number of vertices
    num_vertices = int(input().strip())

    # read the vertices and add them into the graph
    for _ in range(num_vertices):
        vertex = input().strip()
        graph.add_vertex(vertex)

    # read the number of edges
    num_edges = int(input().strip())

    # read the edges and insert them into the graph
    # you will need to call the method to convert them from their labels to their index
    for _ in range(num_edges):
        edge = input().strip().split()
        start = graph.get_index(edge[0])
        finish = graph.get_index(edge[1])
        graph.add_edge(start, finish)

    ####################################################################################
    # DO NOT CHANGE ANYTHING BELOW THIS
    if graph.has_cycle():
        print("Registration plan invalid because a cycle was detected.")
    else:
        print("Valid registration plan detected.")

        courses = graph.get_registration_plan()
        print()
        print("Registration plan: ")
        print(courses)

main()