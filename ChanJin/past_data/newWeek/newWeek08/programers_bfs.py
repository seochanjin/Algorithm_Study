# 게임 맵 최단거리 (난이도 Lv.2)

from collections import deque


def solution(maps):
    answer = 0

    m = len(maps)
    n = len(maps[0])

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    visited = [[False] * n for _ in range(m)]

    bfs_queue = deque([(0, 0)])
    visited[0][0] = True

    while bfs_queue:
        y, x = bfs_queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if not visited[ny][nx] and maps[ny][nx] > 0:
                    visited[ny][nx] = True
                    maps[ny][nx] = maps[y][x] + 1
                    bfs_queue.append((ny, nx))

    if maps[m - 1][n - 1] == 1:
        answer = -1
    else:
        answer = maps[m - 1][n - 1]

    return answer