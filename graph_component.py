def dfs(graph, vertex, visited):
    visited[vertex] = True
    count = 1
    for i in range(len(graph[vertex])):
        if graph[vertex][i] == 1 and not visited[i]:
            count += dfs(graph, i, visited)
    return count

def main():
    N, S = map(int, input().split())
    S = S - 1
    graph = []
    for _ in range(N):
        row = list(map(int, input().split()))
        graph.append(row)
    visited = [False] * N
    result = dfs(graph, S, visited)
    print(result)

if __name__ == "__main__":
    main() 