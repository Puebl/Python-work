def get_edges(matrix, n):
    edges = []
    for i in range(n):
        for j in range(i + 1, n):
            if matrix[i][j] == 1:
                edges.append((i + 1, j + 1))
    return edges

def check_matrix(matrix, n):
    for i in range(n):
        if len(matrix[i]) != n:
            return False
        if matrix[i][i] != 0:
            return False
        for j in range(n):
            if matrix[i][j] not in [0, 1]:
                return False
            if matrix[i][j] != matrix[j][i]:
                return False
    return True

def main():
    try:
        n = int(input().strip())
        if not 1 <= n <= 100:
            print(0)
            return
        
        matrix = []
        for _ in range(n):
            row = list(map(int, input().strip().split()))
            matrix.append(row)
        
        if not check_matrix(matrix, n):
            print(0)
            return
            
        edges = get_edges(matrix, n)
        print(len(edges))
        for edge in edges:
            print(edge[0], edge[1])
            
    except Exception as e:
        print(0)
        return

if __name__ == "__main__":
    main() 