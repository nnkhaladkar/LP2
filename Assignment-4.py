class Nqueens:
    def __init__(self):
        self.n = int(input("Enter size of board: "))
        self.board = []
        for i in range(self.n):
            temp = []
            for j in range(self.n):
                temp.append(0)
            self.board.append(temp)
    
    def isSafe(self, row, column):
        for i in range(column):
            if self.board[row][i] == 1:
                return False
        i = row
        j = column
        while i>=0 and j>=0:
            if self.board[i][j] == 1:
                return False
            i -= 1
            j -= 1
        i = row
        j = column
        while i<self.n and j>=0:
            if self.board[i][j] == 1:
                return False
            i += 1
            j -= 1
        return True
    
    def Solve(self, col):
        if col>=self.n:
            return True
        for row in range(self.n):
            if self.isSafe(row, col):
                self.board[row][col] = 1
                if self.Solve(col+1) == True:
                    return True
                self.board[row][col] = 0
        return False    
    
    def sol(self):
        for i in range(self.n):
            for j in range(self.n):
                print(self.board[i][j], end=" ")
            print()

N = Nqueens()
N.Solve(0)
N.sol()