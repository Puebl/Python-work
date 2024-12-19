def dfs(graph, vertex, visited, component):
    visited[vertex] = True
    component.append(vertex + 1)
    for neighbor in graph[vertex]:
        if not visited[neighbor - 1]:
            dfs(graph, neighbor - 1, visited, component)

def find_components(n, edges):
    graph = [[] for _ in range(n)]
    for v1, v2 in edges:
        graph[v1-1].append(v2)
        graph[v2-1].append(v1)
    visited = [False] * n
    components = []
    for vertex in range(n):
        if not visited[vertex]:
            component = []
            dfs(graph, vertex, visited, component)
            components.append(sorted(component))
    return components

def main():
    N, M = map(int, input().split())
    edges = []
    for _ in range(M):
        i, j = map(int, input().split())
        edges.append((i, j))
    components = find_components(N, edges)
    print(len(components))
    for component in components:
        print(len(component))
        print(*component)

if __name__ == "__main__":
    main() 