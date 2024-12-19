from collections import deque

def get_coordinates(pos):
    col = ord(pos[0]) - ord('a')
    row = int(pos[1]) - 1
    return (row, col)

def get_valid_moves(pos):
    moves = [
        (-2, -1), (-2, 1), (-1, -2), (-1, 2),
        (1, -2), (1, 2), (2, -1), (2, 1)
    ]
    valid = []
    row, col = pos
    for dr, dc in moves:
        new_row, new_col = row + dr, col + dc
        if 0 <= new_row < 8 and 0 <= new_col < 8:
            valid.append((new_row, new_col))
    return valid

def find_min_moves(pos1, pos2):
    start1 = get_coordinates(pos1)
    start2 = get_coordinates(pos2)
    visited = set()
    queue = deque([(start1, start2, 0)])
    visited.add((start1, start2))
    
    while queue:
        pos1, pos2, moves = queue.popleft()
        if pos1 == pos2:
            return moves
        for next1 in get_valid_moves(pos1):
            for next2 in get_valid_moves(pos2):
                if (next1, next2) not in visited:
                    visited.add((next1, next2))
                    queue.append((next1, next2, moves + 1))
    return -1

def main():
    pos1, pos2 = input().split()
    result = find_min_moves(pos1, pos2)
    print(result)

if __name__ == "__main__":
    main() 