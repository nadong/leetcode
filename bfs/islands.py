"""
[a, 0, 0, 0]
[0, 1, 0, 1]
[0, 2, 0, 1]

"""
dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]


def bfs(grid, k):
    q = [(0, 0, k)]
    grid[0][0] = -1
    step = 0
    while len(q):
        s = len(q)
        step += 1
        for i in range(s):
            front = q[0]
            q = q[1:]
            for d in dirs:
                nx = front[0] + d[0]
                ny = front[1] + d[1]
                if nx < 0 or nx >= len(grid) or ny < 0 or ny >= len(grid[0]):
                    continue
                if grid[nx][ny] == 2:
                    return step
                if grid[nx][ny] == 0 or (grid[nx][ny] == 1 and front[2] > 0):
                    q.append((nx, ny, front[2] - (grid[nx][ny] == 1)))
                    grid[nx][ny] = -1
    return -1


paths = [
    [-1, 0, 1, 0],
    [0, 1, 1, 1],
    [1, 1, 2, 1],
]

print(bfs(paths, 2))


def maxIsland(grid) -> (int):
    res = 0
    cnt = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j]:
                res = max(res, bfs(grid, i, j))
                cnt += 1
    return res, cnt


def bfs(grid, i, j):
    q = []
    q.append((i, j))
    grid[i][j] = 0
    res = 1
    while len(q):
        s = len(q)
        for i in range(s):
            front = q[0]
            q = q[1:]
            for dir in dirs:
                nx = front[0] + dir[0]
                ny = front[1] + dir[1]
                if nx < 0 or nx >= len(grid) or ny < 0 or ny >= len(grid[0]) or grid[nx][ny] == 0:
                    continue
                q.append((nx, ny))
                grid[nx][ny] = 0
                res += 1
    return res


grid = [
    [0, 1, 0, 1, 1],
    [1, 1, 0, 1, 0],
    [1, 1, 1, 0, 0]
]

print(maxIsland(grid))
