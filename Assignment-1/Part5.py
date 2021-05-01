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



def reverseLinkedList_Recursively(linkedList: LinkedList):
    current = linkedList.head
    new_list = LinkedList()
    aux = LinkedList()

    if (current == None): 
        return
    elif (current.next == None):
        new_list.push(current.element)
        return new_list
    aux.head = current.next
    new_list = reverseLinkedList_Recursively(aux.head)
    new_list.push(current.element)
    return new_list
