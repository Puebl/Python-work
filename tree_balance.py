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

def get_height(root):
    if not root:
        return -1
    return 1 + max(get_height(root.left), get_height(root.right))

def is_balanced(root):
    if not root:
        return True
        
    left_height = get_height(root.left)
    right_height = get_height(root.right)
    
    if abs(left_height - right_height) <= 1:
        return is_balanced(root.left) and is_balanced(root.right)
    
    return False

def main():
    try:
        numbers = input().strip().split()
        numbers = [int(x) for x in numbers[:-1]]
        
        if not numbers:
            return
            
        root = None
        for num in numbers:
            root = insert(root, num)
        
        result = "YES" if is_balanced(root) else "NO"
        print(result)
        
    except Exception as e:
        print("NO")

if __name__ == "__main__":
    main() 