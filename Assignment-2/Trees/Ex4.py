class BinarySearchTree:
    def __init__(self, key, left = None, right = None):
        self.key = key
        self.left = left
        self.right = right

    def insert(self, key):
        if self.key is None:
            self.key = key
            return
        else:
            if self.key < key:
                if self.right is None:
                    self.right = BinarySearchTree(key)
                else:   
                    self.right.insert(key)
            else:
                if self.left is None:
                    self.left = BinarySearchTree(key)
                else:
                    self.left.insert(key)

    
    def find(self, key):
        print(key)

    class Node:
        def __init__(self, key, left = None, right = None):
            self.key = key
            self.left = left
            self.right = right


if __name__ == "__main__":
    print("a")
    # root_node = BinarySearchTree.Node(16)
    tree = BinarySearchTree(16)
    tree.insert(10)
    tree.insert(21)
    tree.insert(7)
    tree.insert(13)
    tree.insert(18)
    tree.insert(29)
    tree.insert(99)
    
