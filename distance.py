import queue

def solution(maps):
    answer = 0
    n = len(maps)
    m = len(maps[0])
    sx = 0
    sy = 0
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    q  = queue.Queue()
    q.put([sx,sy])
    visited = [[0]*m for _ in range(n)]
    visited[sx][sy]=1
    while q.qsize()!=0:
        now = q.get()
        x = now[0]
        y = now[1]
        for dir in range(4):
            nx = x+dx[dir]
            ny = y+dy[dir]
            if nx<0 or nx>=n or ny<0 or ny>=m:
                continue
            if maps[nx][ny]==0 or visited[nx][ny]>0:
                continue
            visited[nx][ny] = visited[x][y]+1
            q.put([nx,ny])
    if visited[n-1][m-1]==0:
        return -1
    return visited[n-1][m-1]


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]))