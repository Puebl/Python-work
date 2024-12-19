def dijkstra(graph, gas_prices, n):
    dist = [float('inf')] * n
    dist[0] = 0
    visited = [False] * n
    
    for _ in range(n):
        min_cost = float('inf')
        min_vertex = -1
        for v in range(n):
            if not visited[v] and dist[v] < min_cost:
                min_cost = dist[v]
                min_vertex = v
        
        if min_vertex == -1:
            break
            
        visited[min_vertex] = True
        
        for next_city in range(n):
            if graph[min_vertex][next_city]:
                new_cost = dist[min_vertex] + gas_prices[min_vertex]
                if not visited[next_city] and new_cost < dist[next_city]:
                    dist[next_city] = new_cost
    
    return dist[n-1] if dist[n-1] != float('inf') else -1

def main():
    n = int(input())
    
    gas_prices = list(map(int, input().split()))
    
    m = int(input())
    
    roads = [[0] * n for _ in range(n)]
    
    for _ in range(m):
        city1, city2 = map(int, input().split())
        city1 -= 1
        city2 -= 1
        roads[city1][city2] = roads[city2][city1] = 1
    
    result = dijkstra(roads, gas_prices, n)
    print(result)

if __name__ == "__main__":
    main() 