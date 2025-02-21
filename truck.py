import datetime


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
        self.depart_time = self._set_depart_time()
        self.current_time = self.depart_time


    def _set_depart_time(self):
        match self.truck_id:
            case 1:
                return datetime.timedelta(hours=8)
            case 2:
                return datetime.timedelta(hours=9, minutes=5)
            case 3:
                return datetime.timedelta(hours=10, minutes=20)

    def load_truck(self):
        """
        Manually loads the truck with packages based on the truck_id
        """
        match self.truck_id:
            case 1:
                # Truck 1 (Leaves at 8:00 AM, prioritizes early deadlines)
                # 13 packages
                self.packages = [1, 13, 14, 15, 16, 19, 20, 29, 30, 31, 34, 37, 40]

            case 2:
                # Truck 2 (Leaves at 9:05 AM, takes delayed packages & must-be-on-truck-2 packages)
                # 8 packages
                self.packages = [3, 6, 18, 25, 28, 32, 36, 38]

            case 3:
                # Truck 3 (Leaves after 10:20 AM and once another driver is back, takes package #9 and remaining packages)
                # 19 packages
                self.packages = [2, 4, 5, 7, 8, 9, 10, 11, 12, 17, 21, 22, 23, 24, 26, 27, 33, 35, 39]


#    def deliver_packages(self):
#        pass

    def __str__(self):
        return (f"Truck: {self.speed}, {self.capacity}, {self.packages}, {self.load}, {self.miles}, {self.address},"
                f" {self.depart_time}")
