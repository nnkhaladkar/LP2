class Graph:

    def __init__(self):
        self.Graph = {}
        self.visited = []
        self.queue = []
        self.stack = []
        self.v = int(input("Enter number of vertices: "))
        self.e = int(input("Enter number of edges: "))
        for i in range(self.v):
            self.Graph[i] = []
            self.visited.append(False)
        for i in range(self.e):
            a = int(input("\nEnter vertex 1: "))
            b = int(input("Enter vertex 2: "))
            self.Graph[a].append(b)
            self.Graph[b].append(a)
            print("Edge", i, "is added")

    def BFS(self, n):
        self.queue.append(n)
        self.visited[n] = True
        while self.queue:
            s = self.queue.pop(0)
            print(s, end=" ")
            for i in self.Graph[s]:
                if self.visited[i] == False:
                    self.queue.append(i)
                    self.visited[i] = True
    
    def DFS(self, n):
        self.stack.append(n)
        print(n, end= " ")
        for i in self.Graph[n]:
            if i not in self.stack:
                self.DFS(i)



G = Graph()
n = int(input("\nEnter starting node: "))
print("\nBFS: ")
G.BFS(n)
print("\nDFS:")
G.DFS(n)