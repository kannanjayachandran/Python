class Stack:
    """
    Stack Implemented using List
    """

    def __init__(self) -> list:
        self.items = []

    def isEmpty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.isEmpty():
            return self.items.pop()
        else:
            raise Exception("Stack Underflow : Stack is empty !")

    def top(self):
        if not self.isEmpty():
            return self.items[-1]
        else:
            raise Exception("Stack Underflow : Stack is empty !")

    def size(self):
        return len(self.items)


stack = Stack()

print(stack.isEmpty())
stack.push(5)
print(stack.top())
stack.size()
