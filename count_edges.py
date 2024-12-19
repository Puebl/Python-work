def count_edges(matrix, n):
    edges = 0
    for i in range(n):
        for j in range(i + 1, n):
            if matrix[i][j] == 1:
                edges += 1
    return edges

def main():
    try:
        n = int(input().strip())
        if not 1 <= n <= 100:
            raise ValueError("n должно быть от 1 до 100")
        matrix = []
        for _ in range(n):
            row = list(map(int, input().strip().split()))
            if len(row) != n:
                raise ValueError("Неверный размер строки")
            if not all(x in [0, 1] for x in row):
                raise ValueError("Элементы должны быть 0 или 1")
            matrix.append(row)
        result = count_edges(matrix, n)
        print(result)
    except Exception as e:
        print(0)

if __name__ == "__main__":
    main() 