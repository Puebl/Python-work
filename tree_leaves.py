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

def get_leaves(root, leaves):
    if root:
        if not root.left and not root.right:
            leaves.append(root.value)
        get_leaves(root.left, leaves)
        get_leaves(root.right, leaves)

def build_and_print_leaves():
    numbers = list(map(int, input().split()))
    
    numbers.pop()
    
    if not numbers:
        return
        
    root = None
    for num in numbers:
        root = insert(root, num)
    
    leaves = []
    get_leaves(root, leaves)
    leaves.sort()
    
    for leaf in leaves:
        print(leaf)

if __name__ == "__main__":
    build_and_print_leaves() 