class Node:
    def __init__(self, element):
        self.element = element
        self.next = None 


class LinkedList: 
    def __init__(self):
        self.head = None 
        self.size = 0

    def push(self, node: Node):
        if self.head == None:
            self.head = node
        else:
            while node.next != None:
                self.head = self.next
            self.next = node

    def pop(self):
        current = 0
        linked = None
        if (self.size > 0):
            current = self.head
            while(self.next != None):
                linked = self
                self = self.next
            if (linked != None):
                linked.next = None
            return self
        else: 
            return       

    def insert(self, index, node):
        current = self.head
        if (index == 0):
            self.head = node
            node.next = current
            self.size +=1
            return
        elif (index <= self.size):
            counter = 0
            while (current != None):
                if (counter == index-1):
                    next_node = current.next
                    current.next = node
                    node.next = next_node
                    self.size +=1
                    return
                current = current.next
                counter += 1
    
    def remove(self, index):
        if (index == 0):
            self.head = self.head.next
            return 
        if (index < self.size):
            current = self.head 
            count = 0 
            while(current != None):
                if (index-1 == count):
                    current.next = current.next.next 
                    return 
                current = current.next 
                count+=1 
        else:
            return

    def elementAt(self, index):
        node = self.head 
        count = 0 
        while (node != None):
            if (count == index):
                return node
            node = node.next 
            count+=1 
        return None

    def list_size(self):
        count = 0
        node = self.head
        while node is not None:
            count += 1
            node = node.next
        return count

    def printList(self):
        string = ""
        node = self.head

        if node is None:
            return None
        else:
            while (node != None):
                string += str(node.element) + " -> "
                node = node.next
            return string


if __name__ == '__main__':
    linkedList = LinkedList()
    linkedList.push(Node(1))
    print("list: ", linkedList.printList())
    print("list size: ", linkedList.list_size())

    print("insert at position 0:")
    linkedList.insert(0, Node(5))
    print("list: ", linkedList.printList())



