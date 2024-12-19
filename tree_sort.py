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

def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.value)
        inorder_traversal(root.right)

def build_and_traverse_tree():
    numbers = list(map(int, input().split()))
    
    numbers.pop()
    
    if not numbers:
        return
        
    root = None
    for num in numbers:
        root = insert(root, num)
    
    inorder_traversal(root)

if __name__ == "__main__":
    build_and_traverse_tree() 