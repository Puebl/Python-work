class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, n):
        self.items.append(n)
        print("ok")
    
    def pop(self):
        if not self.items:
            print("error")
            return
        print(self.items.pop())
    
    def back(self):
        if not self.items:
            print("error")
            return
        print(self.items[-1])
    
    def size(self):
        print(len(self.items))
    
    def clear(self):
        self.items = []
        print("ok")

def process_command(stack, command):
    if command.startswith("push"):
        try:
            n = int(command.split()[1])
            stack.push(n)
        except (IndexError, ValueError):
            return False
    elif command == "pop":
        stack.pop()
    elif command == "back":
        stack.back()
    elif command == "size":
        stack.size()
    elif command == "clear":
        stack.clear()
    elif command == "exit":
        print("bye")
        return False
    return True

def main():
    stack = Stack()
    while True:
        try:
            command = input().strip()
            if not process_command(stack, command):
                break
        except EOFError:
            break

if __name__ == "__main__":
    main() 