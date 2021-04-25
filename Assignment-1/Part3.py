class Stack:

    def __init__(self):
        self.stack = []

    def push(self, element):
        self.stack.append(element)

    def pop(self):
        if len(self.stack) == 0:
            return None
        else:
            self.stack.pop()

    def top(self):
        return self.stack[-1]

    def isEmpty(self):
        return self.stack == []

    def size(self):
        return len(self.stack)