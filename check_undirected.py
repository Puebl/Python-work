def check_matrix(matrix, n):
    for i in range(n):
        for j in range(n):
            if matrix[i][j] not in [0, 1]:
                return False
            if i == j and matrix[i][j] != 0:
                return False
            if matrix[i][j] != matrix[j][i]:
                return False
    return True

def main():
    try:
        n = int(input().strip())
        if not 1 <= n <= 100:
            print("NO")
            return
        matrix = []
        for _ in range(n):
            row = list(map(int, input().strip().split()))
            if len(row) != n:
                print("NO")
                return
            matrix.append(row)
        result = check_matrix(matrix, n)
        print("YES" if result else "NO")
    except Exception as e:
        print("NO")

if __name__ == "__main__":
    main() 