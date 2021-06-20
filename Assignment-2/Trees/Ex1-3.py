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

class Employee:
    def __init__(self, name, title, direct_reports: list):
        self.name = name
        self.title = title
        self.direct_reports = direct_reports

    def printLevelByLevel(self):
        queue = [self]

        if queue is None:
            return
        else:
            while len(queue) > 0:
                next_level = []
                for employee in queue:
                    print("Name: {}, Title: {}".format(employee.name, employee.title))

                    if len(employee.direct_reports) > 0:
                        for direct_report in employee.direct_reports:
                            next_level.append(direct_report)
                queue = next_level

    def printNumLevels(self):
        queue = [self]
        level_counter = 0

        if queue is None:
            return
        else:
            while len(queue) > 0:
                next_level = []
                for employee in queue:
                    if len(employee.direct_reports) > 0:
                        for direct_report in employee.direct_reports:
                            next_level.append(direct_report)
                level_counter += 1
                queue = next_level
            print(level_counter)


class OrganizationStructure:
    def __init__(self, ceo):
        self.ceo = ceo

            
if __name__ == "__main__":
    left_child = TreeNode(6, None, None)
    right_child = TreeNode(3, None, None)
    left = TreeNode(7, None, None)
    right = TreeNode(17, left_child, right_child)
    root = TreeNode(1, left, right)
    # Ex.1
    print("Ex.1\n----")
    root.print_nodes()


    K = Employee("K", "Sales Intern", [])
    J = Employee("J", "Sales Representative", [K])
    I = Employee("I", "Director", [J])  
    B = Employee("B", "CFO", [I])
    F = Employee("F", "Engineer", [])
    G = Employee("G", "Engineer", [])
    H = Employee("H", "Engineer", [])
    D = Employee("D", "Manager", [F, G, H])
    E = Employee("E", "Manager", [])
    C = Employee("C", "CTO", [D, E])
    A = Employee("A", "CEO", [B, C])
    # Ex.2
    print("\nEx.2\n----")
    A.printLevelByLevel()

    # Ex.3
    print("\nEx.3\n----")
    A.printNumLevels()


    
    


    



