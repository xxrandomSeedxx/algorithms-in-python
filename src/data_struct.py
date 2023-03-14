# DFS
def traverse_inorder(root):
    if root:
        traverse_inorder(root.left)
        print(root.value)
        traverse_inorder(root.right)

def traverse_postorder(root):
    if root:
        traverse_postorder(root.left)
        traverse_postorder(root.right)
        print(root.value)

def traverse_preorder(root):
    if root:
        print(root.value)
        traverse_preorder(root.left)
        traverse_preorder(root.right)

class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.value = data

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

class Graph:
    def __init__(self, numvertex):
        self.adjMatrix = [[-1] * numvertex for x in range(numvertex)]
        self.numvertex = numvertex
        self.verticeslist = [0] * numvertex

    def set_vertex(self, vertex, id):
        if 0 <= vertex <= self.numvertex:
            self.vertices[id] = vertex
            self.verticeslist[vertex] = id

    def set_edge(self, start, end, cost=0):
        start = self.verticeslist[start]
        end = self.verticeslist[end]
        self.adjMatrix[start][end] = cost

    def get_vertex(self, vertex, id):
        return self.verticeslist

    def get_edges(self):
        edges = []
        for i in range(self.numvertex):
            for j in range(self.numvertex):
                if self.adjMatrix[i][j] != -1:
                    edges.append(self.verticeslist[i], self.verticeslist[j], self.adjMatrix[i][j])
        return edges

    def get_matrix(self):
        return self.adjMatrix

# adjacency matrix

# adjacency list
