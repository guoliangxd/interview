import sys
class Lands(object):
    def numIsLands(self, grid):
        row = len(grid)
        if row == 0 or grid == None:
            return 0
        col = len(grid[0])
        total = 0 
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    self.find(grid, i, j, row, col)
                    total += 1
        return total

    def find(self, grid, i, j, row, col):
        if grid[i][j] == 1:
            grid[i][j] = 0
            if i - 1 >= 0:
                grid = self.find(grid, i - 1, j, row, col)
            if i + 1 < row:
                grid = self.find(grid, i + 1, j, row, col)
            if j - 1 >= -0:
                grid = self.find(grid, i, j - 1, row, col)
            if j + 1 < col:
                grid = self.find(grid, i, j + 1, row, col)
        return grid

while True:
    try:
        data = [] 
        firstLine = sys.stdin.readline().strip().split()
        m = int(firstLine[0])
        n = int(firstLine[1])
        for i in range(m):
            line = sys.stdin.readline().strip().split()
            temp = []
            for j in range(n):
                temp.append(int(line[j]))
            data.append(temp)
        countLands = Lands()
        print(countLands.numIsLands(data))
        
    except:
        break