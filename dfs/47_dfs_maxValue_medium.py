"""
在一个 m*n 的棋盘的每一格都放有一个礼物，每个礼物都有一定的价值（价值大于 0）。你可以从棋盘的左上角开始拿格子里的礼物，并每次向右或者向下移动一格、直到到达棋盘的右下角。给定一个棋盘及其上面的礼物的价值，请计算你最多能拿到多少价值的礼物？

"""
class Solution:
    def maxValue(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0

        #dp(i, j)
        # i = 0, j = 0: dp(i, j) = grid[i][j]
        # i != 0 , j = 0 : dp(i, j) = grid[i][j] + dfs(i-1, j)
        # i =0, j != 0 : dp(i, j) = grid[i][j] + dfs(i, j-1)
        # i != 0, j!= 0: dp(i, j) = grid[i][j] + max(dfs(i-1,j), dfs(i, j-1))
        for i in range(0 , len(grid)):
            for j in range(0, len(grid[0])):
                if i == 0 and j == 0: continue
                if i == 0: grid[i][j] += grid[i][j - 1]
                elif j == 0: grid[i][j] += grid[i - 1][j]
                else:
                    grid[i][j] += max(grid[i-1][j], grid[i][j-1])

        return grid[-1][-1]