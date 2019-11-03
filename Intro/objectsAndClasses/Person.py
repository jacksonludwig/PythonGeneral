class Person:
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def reverse_name(self):
        reversed_name = ""
        for index in range(len(self.name) - 1, -1, -1):
            reversed_name += self.name[index]
        return reversed_name
