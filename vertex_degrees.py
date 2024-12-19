def get_vertex_degrees(matrix, n):
    degrees = []
    for i in range(n):
        degree = 0
        for j in range(n):
            if matrix[i][j] == 1 or matrix[j][i] == 1:
                degree += 1
        degrees.append(degree)
    return degrees

def main():
    try:
        n = int(input().strip())
        
        if not 1 <= n <= 100:
            return
        
        matrix = []
        for _ in range(n):
            row = list(map(int, input().strip().split()))
            if len(row) != n or not all(x in [0, 1] for x in row):
                return
            matrix.append(row)
        
        degrees = get_vertex_degrees(matrix, n)
        for degree in degrees:
            print(degree)
        
    except Exception as e:
        return

if __name__ == "__main__":
    main() 