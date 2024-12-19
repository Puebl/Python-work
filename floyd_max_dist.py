def floyd_warshall(graph):
    n = len(graph)
    dist = [[float('inf') if i != j else 0 for j in range(n)] for i in range(n)]
    
    for i in range(n):
        for j in range(n):
            if graph[i][j] != -1:
                dist[i][j] = graph[i][j]
    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] != float('inf') and dist[k][j] != float('inf'):
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    
    max_dist = 0
    for i in range(n):
        for j in range(n):
            if dist[i][j] != float('inf'):
                max_dist = max(max_dist, dist[i][j])
    
    return max_dist

def main():
    n = int(input())
    
    graph = []
    for _ in range(n):
        row = list(map(int, input().split()))
        graph.append(row)
    
    result = floyd_warshall(graph)
    print(result)

if __name__ == "__main__":
    main() 