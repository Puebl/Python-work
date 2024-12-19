def ford_bellman(n, edges):
    dist = [30000] * n
    dist[0] = 0
    
    for _ in range(n - 1):
        for start, end, weight in edges:
            if dist[start] != 30000 and dist[start] + weight < dist[end]:
                dist[end] = dist[start] + weight
    
    return dist

def main():
    n, m = map(int, input().split())
    
    edges = []
    for _ in range(m):
        start, end, weight = map(int, input().split())
        start -= 1
        end -= 1
        edges.append((start, end, weight))
    
    distances = ford_bellman(n, edges)
    print(*distances)

if __name__ == "__main__":
    main() 