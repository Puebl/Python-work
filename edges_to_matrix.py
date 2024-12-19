def create_adjacency_matrix(n, edges):
    matrix = [[0] * n for _ in range(n)]
    for start, end in edges:
        start -= 1
        end -= 1
        matrix[start][end] = 1
    return matrix

def print_matrix(matrix):
    for row in matrix:
        print(' '.join(map(str, row)))

def main():
    try:
        n, m = map(int, input().strip().split())
        if not (1 <= n <= 100 and 1 <= m <= n * (n - 1)):
            return
        edges = []
        for _ in range(m):
            start, end = map(int, input().strip().split())
            if not (1 <= start <= n and 1 <= end <= n):
                return
            edges.append((start, end))
        matrix = create_adjacency_matrix(n, edges)
        print_matrix(matrix)
    except Exception as e:
        return

if __name__ == "__main__":
    main() 