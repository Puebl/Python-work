class Queue:
    def __init__(self):
        self.items = []
    
    def push(self, n):
        self.items.append(n)
        print("ok")
    
    def pop(self):
        if not self.items:
            print("error")
            return
        print(self.items.pop(0))
    
    def front(self):
        if not self.items:
            print("error")
            return
        print(self.items[0])
    
    def size(self):
        print(len(self.items))
    
    def clear(self):
        self.items = []
        print("ok")

def process_command(queue, command):
    if command.startswith("push"):
        try:
            n = int(command.split()[1])
            queue.push(n)
        except (IndexError, ValueError):
            return False
    elif command == "pop":
        queue.pop()
    elif command == "front":
        queue.front()
    elif command == "size":
        queue.size()
    elif command == "clear":
        queue.clear()
    elif command == "exit":
        print("bye")
        return False
    return True

def main():
    queue = Queue()
    while True:
        try:
            command = input().strip()
            if not process_command(queue, command):
                break
        except EOFError:
            break

if __name__ == "__main__":
    main() 