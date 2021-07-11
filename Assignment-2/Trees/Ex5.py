# List
class ListPhoneBook:
    def __init__(self):
        self.list = list()
    
    def size(self) -> int:
        return len(self.list)

    def insert(self, name, phoneNumber):
        self.list.append({"name": name, "phoneNumber": phoneNumber})

    def find(self, name) -> int:
        for contact in self.list:
            if name == contact.get("name"):
                return contact.get("phoneNumber")
        return -1


# Tree
class BinarySearchTreePhoneBook:
    def __init__(self, name, phoneNumber):
        self.name = name
        self.phoneNumber = phoneNumber
        self.left = None
        self.right = None

    def size(self) -> int:
        counter = 1
        if self.left is not None:
            counter += self.left.size()
        if self.right is not None:
            counter += self.right.size()

        return counter

    def insert(self, name, phoneNumber):
        if self.name is None:
            print("oops...")
        else:
            contact = BinarySearchTreePhoneBook(name, phoneNumber)
            if self.name > contact.name:
                if self.left is None:
                    self.left = contact
                else:
                    self.left.insert(name, phoneNumber)
            else:
                if self.right is None:
                    self.right = contact
                else:
                    self.right.insert(name, phoneNumber)

    def find(self, name) -> int:
        if self.name == name:
            return self.phoneNumber
        elif name > self.name:
            if self.right is not None:
                self.right.find(name)
            else:
                return -1
        else:
            if self.left is not None:
                self.left.find(name)
            else:
                return -1



if __name__ == "__main__":
    print("------- LIST PHONE BOOK -------")

    list_phoneBook = ListPhoneBook()
    print(list_phoneBook.size())

    list_phoneBook.insert("ABC", 1111111111)
    list_phoneBook.insert("XYZ", 9999999999)
    list_phoneBook.insert("DEF", 2222222222)

    print(list_phoneBook.size())

    print(list_phoneBook.find("ABC"))
    print(list_phoneBook.find("XYZ"))
    print(list_phoneBook.find("DEF"))

    print("\n------- TREE PHONE BOOK -------")
    tree_phoneBook = BinarySearchTreePhoneBook("ABC", 1111111111)
    print(tree_phoneBook.size())

    tree_phoneBook.insert("XYZ", 9999999999)
    tree_phoneBook.insert("DEF", 2222222222)
    print(tree_phoneBook.size())

    print(tree_phoneBook.find("ABC"))
    print(tree_phoneBook.find("XYZ"))
    print(tree_phoneBook.find("DEF"))
