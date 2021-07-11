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

# class BinarySearchTreePhoneBook:

if __name__ == "__main__":
    list_phoneBook = ListPhoneBook()

    print(list_phoneBook.size())

    list_phoneBook.insert("ABC", 1111111111)
    list_phoneBook.insert("XYZ", 9999999999)
    list_phoneBook.insert("DEF", 2222222222)

    print(list_phoneBook.size())

    print(list_phoneBook.find("ABC"))
    print(list_phoneBook.find("XYZ"))
    print(list_phoneBook.find("DEF"))
