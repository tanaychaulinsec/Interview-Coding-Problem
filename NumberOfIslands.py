class Solution:
    def numIslands(self, grid):
        islands = 0
        for row in range(0, len(grid)):
            for col in range(0, len(grid[0])):
                if grid[row][col] == '1':
                    islands += 1
                    self.clearIsland(grid, row, col)

        return islands

    def clearIsland(self, grid, row, col):
        if row >= 0 and col >= 0 and row < len(grid) and col < len(grid[row]):
            if grid[row][col] == '1':
                grid[row][col] = '0'
                self.clearIsland(grid, row + 1, col)
                self.clearIsland(grid, row, col + 1)
                self.clearIsland(grid, row - 1, col)
                self.clearIsland(grid, row, col - 1)


graph = [[1, 1, 0, 0, 0],
         [1, 1, 0, 0, 1],
         [1, 0, 0, 1, 1],
         [0, 0, 0, 0, 0],
         [0, 0, 1, 0, 1]]

print("Number of islands is:")
print(Solution().numIslands(graph))
