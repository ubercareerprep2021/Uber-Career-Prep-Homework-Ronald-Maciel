class TreeNode:
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right

    def print_nodes(self):
        if self is None:
            return
        else:
            print(self.data)
            if self.left is not None:
                self.left.print_nodes()
            if self.right is not None:
                self.right.print_nodes()


if __name__ == "__main__":
    left_child = TreeNode(6, None, None)
    right_child = TreeNode(3, None, None)
    left = TreeNode(7, None, None)
    right = TreeNode(17, left_child, right_child)
    root = TreeNode(1, left, right)
    root.print_nodes()