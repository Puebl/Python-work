from collections import deque

def read_graph():
    n = int(input().strip())
    
    graph = []
    for _ in range(n):
        row = list(map(int, input().strip().split()))
        graph.append(row)
    
    start, end = map(int, input().strip().split())
    start -= 1
    end -= 1
    
    return n, graph, start, end

def find_shortest_path(n, graph, start, end):
    dist = [-1] * n
    pred = [-1] * n
    
    queue = deque([start])
    dist[start] = 0
    
    while queue:
        current = queue.popleft()
        
        for next_vertex in range(n):
            if graph[current][next_vertex] == 1 and dist[next_vertex] == -1:
                queue.append(next_vertex)
                dist[next_vertex] = dist[current] + 1
                pred[next_vertex] = current
    
    if dist[end] == -1:
        print(-1)
        return
    
    path = []
    current = end
    while current != -1:
        path.append(current + 1)
        current = pred[current]
    path.reverse()
    
    print(len(path) - 1)
    print(*path)

def main():
    try:
        n, graph, start, end = read_graph()
        
        find_shortest_path(n, graph, start, end)
    except Exception as e:
        print(-1)

if __name__ == "__main__":
    main() 