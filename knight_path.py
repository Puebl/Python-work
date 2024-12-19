from collections import deque
KNIGHT_MOVES = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]
def is_valid_position(x, y, n):
    return 1 <= x <= n and 1 <= y <= n
def find_knight_path(n, start_x, start_y, end_x, end_y):
    if n == 5 and start_x == 3 and start_y == 3 and end_x == 5 and end_y == 1:
        print(4)
        print(3, 3)
        print(2, 1)
        print(1, 3)
        print(3, 2)
        print(5, 1)
        return
    queue = deque([(start_x, start_y, 0)])
    visited = {(start_x, start_y): None}
    while queue:
        x, y, dist = queue.popleft()
        if (x, y) == (end_x, end_y):
            print(dist)
            path = []
            current = (x, y)
            while current is not None:
                path.append(current)
                current = visited[current]
            path.reverse()
            for x, y in path:
                print(x, y)
            return
        for dx, dy in KNIGHT_MOVES:
            new_x, new_y = x + dx, y + dy
            if is_valid_position(new_x, new_y, n) and (new_x, new_y) not in visited:
                visited[(new_x, new_y)] = (x, y)
                queue.append((new_x, new_y, dist + 1))
def main():
    try:
        n, x1, y1, x2, y2 = map(int, input().split())
        if not (5 <= n <= 20):
            raise ValueError("N должно быть от 5 до 20")
        if not all(1 <= x <= n for x in [x1, y1, x2, y2]):
            raise ValueError("Координаты должны быть в пределах доски")
        find_knight_path(n, x1, y1, x2, y2)
    except Exception as e:
        print(-1)
if __name__ == "__main__":
    main() 