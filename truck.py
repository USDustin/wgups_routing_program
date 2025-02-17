

class Truck:

    def __init__(self, speed, capacity, packages, load, miles, address, depart_time):

        self.speed = speed
        self.capacity = capacity
        self.packages = packages
        self.load = load
        self.miles = miles
        self.address = address
        self.depart_time = depart_time


#    def load_truck(self):
#        pass

#    def deliver_packages(self):
#        pass

    def __str__(self):
        return (f"Truck: {self.speed}, {self.capacity}, {self.packages}, {self.load}, {self.miles}, {self.address},"
                f" {self.depart_time}")