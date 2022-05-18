'''
Implement Greedy search algorithm for any one of the following application: 

I	Selection Sort 
II	Minimum Spanning Tree 
III	Single-Source Shortest Path Problem 
IV	Job Scheduling Problem 
V	Prim's Minimal Spanning Tree Algorithm 
VI	Kruskal's Minimal Spanning Tree Algorithm 
VII	Dijkstra's Minimal Spanning Tree Algorithm 
'''

'''
Greedy search algorithm for Kruskal's Minimal Spanning Tree Algorithm
'''

class Graph:
    def __init__(self, vertices):
        self.V = vertices  
        self.graph = []  
 
    def addEdge(self, u, v, w):
        self.graph.append([u, v, w])
 
    def find(self, parent, i): #recursive function to find the parent of a node
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])
 
    def union(self, parent, rank, x, y): #checks if any cycle is formed
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)
 
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
 
        else:
            parent[yroot] = xroot
            rank[xroot] += 1
 

    def KruskalMST(self):
        result = [] 
        i = 0
        e = 0
 
        self.graph = sorted(self.graph,key=lambda item: item[2]) #sorting the edges
        parent = []
        rank = []
 
        for node in range(self.V):
            parent.append(node)
            rank.append(0)
 
        while e < self.V - 1:
            u, v, w = self.graph[i]
            i = i + 1
            x = self.find(parent, u)
            y = self.find(parent, v)
            if x != y: #condition for eliminating loops, if any
                e = e + 1
                result.append([u, v, w])
                self.union(parent, rank, x, y)
 
        minimumCost = 0
        print ("\nEdges in the MST :- ")
        for u, v, weight in result:
            minimumCost += weight
            print("%d -- %d == %d" % (u, v, weight))
        print("Minimum Spanning Tree Cost = " , minimumCost)
 


v = int(input("Enter the number of vertices: "))
g = Graph(v)
e = int(input("\nEnter the number of edges: "))
print("\n")
for i in range(e):
    u, v, w = map(int, input("Enter the edge u, v, w: \n").split())
    g.addEdge(u, v, w)

g.KruskalMST()

'''
    10
0 ------ 1
|\       |
|        |
|  \     |15
|6   5   |
|    \   |
|        |
|       \|
2 ------ 3
     4

'''

'''
Input :-
4
5
0 1 10
0 3 5
1 3 15
0 2 6
2 3 4

'''
