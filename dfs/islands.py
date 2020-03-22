"""
tree 深度优先 递归/stack  
广度优先 queue  = 层序遍历

[0,1,0,1,1]
[1,1,0,1,0]
[1,1,1,0,0]

"""


def maxIsland(grid) -> (int, int):
    res = 0
    cnt = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j]:
                res = max(res, dfs(grid, i, j))
                cnt += 1
    return res, cnt


def dfs(grid: [[]], x, y) -> int:
    if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or grid[x][y] != 1:
        return 0
    grid[x][y] = 0
    return 1 + dfs(grid, x + 1, y) + dfs(grid, x - 1, y) + dfs(grid, x, y - 1) + dfs(grid, x, y + 1)


grid = [
    [0, 1, 0, 1, 1],
    [1, 1, 0, 1, 0],
    [1, 1, 1, 0, 0]
]
print(maxIsland(grid))
