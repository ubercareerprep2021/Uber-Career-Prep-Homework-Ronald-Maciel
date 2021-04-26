class Stack:

    def __init__(self):
        self.stack = []

    # Pushes an integer on top of the stack
    def push(self, element):
        self.stack.append(element)

    # Removes what is on the top of the stack, and returns that value to the caller
    def pop(self):
        if len(self.stack) == 0:
            return 0
        else:
            self.stack.pop()

    # Looks at the top value, and returns it. Does not manipulate the stack
    def top(self):
        if len(self.stack) == 0:
            return None
        else:
            return self.stack[-1]

    # Returns True or False if the stack is Empty or not, respectively
    def isEmpty(self):
        return self.stack == []

    # Returns an integer value with the count of elements in the stack
    def size(self):
        return len(self.stack)


class Queue:
    def __init__(self):
        self.queue = []
        
    # adds an item to the queue
    def enqueue(self, element):
        self.queue.append(element)

    # removes an item from the queue
    def dequeue(self):
        if len(self.queue) == 0:
            return None
        else:
            self.queue = self.queue[1:]

    # returns the item at the end of the queue
    def rear(self):
        if len(self.queue) == 0:
            return None
        else:
            return self.queue[-1]

    # returns the item at the front of the queue
    def front(self):
        if len(self.queue) == 0:
            return None
        else:
            return self.queue[0]

    # returns the size of the queue
    def size(self):
        return len(self.queue)
    
    # returns whether or not the queue is empty
    def isEmpty(self):
        return self.queue == []


def testingStack():
    stack = Stack()
    print("----------- Testing Stack -----------\nStack empty:")
    print("size:", stack.size())
    print("empty:", stack.isEmpty())
    print("top:", stack.top())
    
    element = 100
    print("\nPushed value:", element)
    stack.push(element)
    print("size:", stack.size())
    print("empty:", stack.isEmpty())
    print("top:", stack.top())
    print("pop:", stack.pop())

def testingQueue():
    queue = Queue()

    print("\n\n----------- Testing Queue -----------\nQueue empty:")
    print("size:", queue.size())
    print("empty:", queue.isEmpty())
    print("rear:", queue.rear())

    element = 100
    print("\nPushed value:", element)
    queue.enqueue(element)
    print("size:", queue.size())
    print("empty:", queue.isEmpty())
    print("rear:", queue.rear())
    print("dequeue:", queue.dequeue())
    
    print("\nPushed value: 100")
    queue.enqueue(100)
    print("size:", queue.size())
    print("empty:", queue.isEmpty())
    print("rear:", queue.rear())
    print("dequeue:", queue.dequeue())
    


if __name__ == '__main__':
    testingStack()
    testingQueue()
