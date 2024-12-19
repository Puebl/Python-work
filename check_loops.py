def has_loops(matrix, n):
    for i in range(n):
        if matrix[i][i] == 1:
            return True
    return False
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
            if not all(x in [0, 1] for x in row):
                print("NO")
                return
            matrix.append(row)
        result = has_loops(matrix, n)
        print("YES" if result else "NO")
    except Exception as e:
        print("NO")
if __name__ == "__main__":
    main()