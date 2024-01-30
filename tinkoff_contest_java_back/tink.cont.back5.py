from collections import deque


# Функция для поиска кратчайшего пути в графе
def shortest_path(graph, start, end):
    queue = deque([start])
    visited = set([start])
    parent = {}

    while queue:
        current = queue.popleft()
        if current == end:
            path = []
            while current != start:
                path.append(current)
                current = parent[current]
            path.append(start)
            return path[::-1]

        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
                parent[neighbor] = current

    return None


n = int(input())
graph = {i: [] for i in range(1, n + 1)}
for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

q = int(input())
for _ in range(q):
    from_room, to_room = map(int, input().split())
    path = shortest_path(graph, from_room, to_room)
    print(path[1])

