def count_edges(matrix, n):
    edges = 0
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 1:
                edges += 1
    return edges

def main():
    try:
        n = int(input().strip())
        if not 1 <= n <= 100:
            print(0)
            return
        matrix = []
        for _ in range(n):
            row = list(map(int, input().strip().split()))
            if len(row) != n or not all(x in [0, 1] for x in row):
                print(0)
                return
            matrix.append(row)
        print(count_edges(matrix, n))
    except Exception as e:
        print(0)

if __name__ == "__main__":
    main() 