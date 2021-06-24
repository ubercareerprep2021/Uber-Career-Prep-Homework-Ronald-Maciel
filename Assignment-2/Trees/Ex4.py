class BinarySearchTree:
    def __init__(self, root):
        self.root = root


    class Node():
        def __init__(self, key, left = None, right = None):
            self.key = key
            self.left = left
            self.right = right

    def insert(self, key):
        print(key)

    def find(self, key):
        print(key)





if __name__ == "__main__":
    tree = BinarySearchTree(0)