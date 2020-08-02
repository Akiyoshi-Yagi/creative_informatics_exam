width, height = map(int, input().split())


maze = [list(map(int,input().split())) for _ in range(height)]
direction = [[1,1], [1,0],[1,-1],[0,1],[0,-1],[-1,1],[-1,0],[-1,-1]]

def dfs(maze,h,w):
    group = [[0] * w for _ in range(h)]
    g_num = 1
    for i in range(h):
        for j in range(w):
            #島かつまだ訪れていない位置
            if maze[i][j] == 1 and group[i][j] == 0:
                group[i][j] = g_num
                stack = [[i, j]]
                while stack:
                    x, y = stack.pop()
                    for d in direction:
                        n_x = x + d[0]
                        n_y = y + d[1]
                        if 0 <= n_x < h and 0 <= n_y < w and group[n_x][n_y] == 0 and maze[n_x][n_y] == 1:
                            group[n_x][n_y] = g_num
                            stack.append([n_x,n_y])
                g_num += 1
    return g_num-1

print(dfs(maze,height,width))

'''
5 4
1 0 1 0 0
1 0 0 0 0
1 0 1 0 1
1 0 0 1 0

5 5
1 0 1 0 1
0 0 0 0 0
1 0 1 0 1
0 0 0 0 0
1 0 1 0 1
'''



