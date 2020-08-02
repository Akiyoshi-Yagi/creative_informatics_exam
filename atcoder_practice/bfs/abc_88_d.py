from collections import deque

h, w = map(int, input().split())

maze = [list(input()) for _ in range(h)]
step = [[0] * w for _ in range(h)]
direction = [[1,0],[-1,0],[0,1],[0,-1]]

def bfs(maze,h,w):
    start = [0,0]
    #キューで座標保存
    q = deque([start])
    while q:
        x, y = q.popleft()
        for d in direction:
            nx = x + d[0]
            ny = y + d[1]
            if 0 <= nx < h and 0 <= ny < w and maze[nx][ny] == "." and step[nx][ny] == 0:
                q.append([nx,ny])
                step[nx][ny] = step[x][y] + 1
        if step[h-1][w-1] != 0:
            return step[h-1][w-1]
    return -1

#壁の数
wall = 0
for i in maze:
    for j in i:
        if j == "#":
            wall += 1
if bfs(maze,h,w) >= 0:
    ans = h * w - wall - (bfs(maze,h,w) + 1)
else:
    ans = -1
print(ans)
