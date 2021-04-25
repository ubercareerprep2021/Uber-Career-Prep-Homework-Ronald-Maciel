class Stack:

    def __init__(self):
        self.stack = []

    # Add the element to the top of the stack
    def push(self, element):
        self.stack.append(element)

    # Remove the last element of the stack, i.e., the element present in the top of the stack
    def pop(self):
        if len(self.stack) == 0:
            return None
        else:
            self.stack.pop()

    # Return the last element of the stack
    def top(self):
        return self.stack[-1]

    # Returns a boolean that verifies if stack is empty
    def isEmpty(self):
        return self.stack == []

    # Return the actual size of the stack
    def size(self):
        return len(self.stack)