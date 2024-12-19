from collections import deque

def dfs(graph, vertex, start, visited, path, max_cycle):
    visited[vertex] = True
    path.append(vertex)
    
    for next_vertex in range(len(graph)):
        if graph[vertex][next_vertex]:
            if next_vertex == start and len(path) > 2:
                max_cycle[0] = max(max_cycle[0], len(path) - 1)
            elif not visited[next_vertex]:
                dfs(graph, next_vertex, start, visited, path, max_cycle)
    
    path.pop()
    visited[vertex] = False

def find_max_cycle(graph):
    n = len(graph)
    max_cycle = [0]
    
    for start in range(n):
        visited = [False] * n
        path = []
        dfs(graph, start, start, visited, path, max_cycle)
    
    return max_cycle[0]

def main():
    n, m = map(int, input().split())
    
    graph = [[0] * n for _ in range(n)]
    
    for _ in range(m):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        graph[u][v] = graph[v][u] = 1
    
    result = find_max_cycle(graph)
    print(result)

if __name__ == "__main__":
    main() 