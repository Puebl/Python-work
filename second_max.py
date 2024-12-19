def find_second_max():
    numbers = list(map(int, input().split()))
    numbers.pop()
    
    if len(numbers) < 2:
        return
    
    max_num = max(numbers)
    second_max = max(x for x in numbers if x != max_num)
    
    print(second_max)

if __name__ == "__main__":
    find_second_max() 