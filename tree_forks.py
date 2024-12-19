class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def insert(root, value):
    if root is None:
        return Node(value)
    
    if value < root.value:
        root.left = insert(root.left, value)
    elif value > root.value:
        root.right = insert(root.right, value)
    
    return root

def get_forks(root, forks):
    if root:
        if root.left and root.right:
            forks.append(root.value)
        get_forks(root.left, forks)
        get_forks(root.right, forks)

def build_and_print_forks():
    numbers = list(map(int, input().split()))
    
    numbers.pop()
    
    if not numbers:
        return
        
    root = None
    for num in numbers:
        root = insert(root, num)
    
    forks = []
    get_forks(root, forks)
    forks.sort()
    
    for fork in forks:
        print(fork)

if __name__ == "__main__":
    build_and_print_forks() 