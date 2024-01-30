from collections import deque

n, m, k = map(int, input().split())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    u, v, d = map(int, input().split())
    graph[u].append(v, d)
    graph[v].append(u, d)

path = list(map(int, input().split()))

visited = set()
queue = deque([(1, 0)])  # (пункт доставки, индекс в path)
while queue:
    current_point, path_index = queue.popleft()
    if path_index == k:  # если дошли до конца пути
        print(current_point)
        break
    visited.add((current_point, path_index))
    for neighbor, car_number in graph[current_point]:
        if (neighbor, path_index+1) not in visited and car_number == path[path_index]:
            queue.append((neighbor, path_index+1))
else:
    print(0)  # если не дошли до конца пути
