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
    print("a")



def reverseLinkedList_Recursively(linkedList: LinkedList):
    print("a")


