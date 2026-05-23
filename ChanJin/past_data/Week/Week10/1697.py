from collections import deque
import sys
input = sys.stdin.readline

n, k = map(int, input().split())

max_point = 100001
bfs_visited = [False] * max_point

def solve(start, time):
    bfs_deque = deque([(start, time)])
    bfs_visited[start] = True

    while(bfs_deque):
        start, time = bfs_deque.popleft()
        # print("현재 위치를 좀 볼까:", start, time)
        if start == k:
            print(time)
            return
        for next in (start -1, start + 1, start * 2):
            if 0 <= next < max_point and not bfs_visited[next]:
                bfs_deque.append((next, time+1))
                bfs_visited[next] = True


solve(n, 0)
