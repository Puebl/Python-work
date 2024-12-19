def main():
    classes = {9: [], 10: [], 11: []}
    try:
        while True:
            line = input().strip()
            if not line:
                break
            parts = line.split()
            if len(parts) < 2:
                continue
            try:
                class_num = int(parts[0])
                surname = ' '.join(parts[1:])
                if class_num in [9, 10, 11] and len(surname) <= 50:
                    classes[class_num].append(surname)
            except ValueError:
                continue
    except EOFError:
        pass
    for class_num in [9, 10, 11]:
        for surname in classes[class_num]:
            print(surname)
if __name__ == "__main__":
    main() 