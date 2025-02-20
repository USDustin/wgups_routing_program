

class Address:
    def __init__(self, index, name, street):
        self.address_index = index
        self.name = name
        self.street = street

    def __str__(self):
        return f"{self.address_index}, {self.name}, {self.street}"