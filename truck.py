

class Truck:


    def __init__(self, truck_id):
        """
        Initializes the Truck class with default values
        """
        self.truck_id = truck_id
        self.speed = 18
        self.capacity = 16
        self.packages = []
        self.load = 0
        self.miles = 0
        self.address = "4001 South 700 East"
        self.depart_time = "08:00:00"


#    def deliver_packages(self):
#        pass

    def __str__(self):
        return (f"Truck: {self.speed}, {self.capacity}, {self.packages}, {self.load}, {self.miles}, {self.address},"
                f" {self.depart_time}")