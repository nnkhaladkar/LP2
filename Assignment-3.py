class Greedy():
    def __init__(self):
        self.n = int(input("Enter number of elements: "))
        self.arr = []
        print("Enter elements:")
        for i in range(self.n):
            s = int(input())
            self.arr.append(s)
    
    def sort(self):
        for i in range(self.n):
            minindex = i
            for j in range(i + 1, self.n):
                if self.arr[minindex] > self.arr[j]:
                    minindex = j
            self.arr[i], self.arr[minindex] = self.arr[minindex], self.arr[i]
        print(self.arr)

G = Greedy()
G.sort()