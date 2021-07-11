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
    list = ListPhoneBook()
    list_size = list.size()
    print(list_size)

    list.insert("ABC", 1111111111)
    list.insert("XYZ", 9999999999)
    list.insert("DEF", 2222222222)

    list_size = list.size()
    print(list_size)

    phone = list.find("ABC")
    print(phone)
