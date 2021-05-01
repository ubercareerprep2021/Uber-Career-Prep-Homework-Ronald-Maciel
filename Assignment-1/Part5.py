from Part4 import *

def reverseLinkedList_Iteratively(linkedList: LinkedList):
    prev_node = None
    current = linkedList.head

    while (current != None):
        next_node = current.next
        current.next = prev_node
        prev_node = current
        current = next_node
    linkedList.head = prev_node
    return linkedList

def reverseLinkedList_Stack(linkedList: LinkedList):
    stack = []
    current = linkedList.head

    while (current.next != None):
        stack.append(current)
        current = current.next

    linkedList.head = current
    while (len(stack) != 0):
        current.next = stack.pop()
        current = current.next
    current.next = None
    return linkedList



def reverseLinkedList_Recursively(head: LinkedList):
    if head is None or head.next is None:
        return head

    rest = reverseLinkedList_Recursively(head.next)
 
    head.next.next = head
    head.next = None
 
    return rest


linkedList = LinkedList()
linkedList.push(Node(20))
linkedList.push(Node(4))
linkedList.push(Node(15))
linkedList.push(Node(85))
 
print("Given linked list: ", linkedList.printList())
 
linkedList.head = reverseLinkedList_Recursively(linkedList.head)
 
print("Reversed linked list: ", linkedList.printList())