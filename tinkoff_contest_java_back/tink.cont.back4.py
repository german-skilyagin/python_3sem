from collections import defaultdict

def dfs(v, visited, graph, friends):
    visited[v] = True
    friends.append(v)
    for u in graph[v]:
        if not visited[u]:
            dfs(u, visited, graph, friends)

n, m, g = map(int, input().split())
interest = list(map(int, input().split()))
appetite = list(map(int, input().split()))

graph = defaultdict(list)
for _ in range(m):
    u, v = map(int, input().split())
    graph[u-1].append(v-1)
    graph[v-1].append(u-1)

visited = [False] * n
max_interest = 0
for i in range(n):
    if not visited[i]:
        friends = []
        dfs(i, visited, graph, friends)
        total_interest = sum(interest[x] for x in friends)
        total_appetite = sum(appetite[x] for x in friends)
        if total_appetite <= g:
            max_interest = max(max_interest, total_interest)

print(max_interest)
