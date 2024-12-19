def count_roads():
    n = int(input().strip())
    if not 0 <= n <= 100:
        raise ValueError("N должно быть от 0 до 100")
    roads = 0
    matrix = []
    for i in range(n):
        row = list(map(int, input().strip().split()))
        matrix.append(row)
    for i in range(n):
        for j in range(i + 1, n):
            if matrix[i][j] == 1:
                roads += 1
    return roads
def main():
    try:
        result = count_roads()
        print(result)
    except Exception as e:
        print(0)
if __name__ == "__main__":
    main() 