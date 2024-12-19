def dijkstra(graph, start, end):
    n = len(graph)
    dist = [float('inf')] * n
    dist[start] = 0
    visited = [False] * n
    prev = [-1] * n
    
    for _ in range(n):
        min_dist = float('inf')
        min_vertex = -1
        for v in range(n):
            if not visited[v] and dist[v] < min_dist:
                min_dist = dist[v]
                min_vertex = v
        
        if min_vertex == -1:
            break
            
        visited[min_vertex] = True
        
        for v in range(n):
            if (graph[min_vertex][v] != -1 and
                not visited[v] and
                dist[min_vertex] + graph[min_vertex][v] < dist[v]):
                dist[v] = dist[min_vertex] + graph[min_vertex][v]
                prev[v] = min_vertex
    
    if dist[end] == float('inf'):
        print(-1)
        return
    
    path = []
    current = end
    while current != -1:
        path.append(current + 1)
        current = prev[current]
    
    print(*path[::-1])

def main():
    N, S, F = map(int, input().split())
    S -= 1
    F -= 1
    
    graph = []
    for _ in range(N):
        row = list(map(int, input().split()))
        graph.append(row)
    
    dijkstra(graph, S, F)

if __name__ == "__main__":
    main() 