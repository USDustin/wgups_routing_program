

class Package:

    def __init__(self, package_id, address, city, state, zip_code, deadline, weight, status):
        self.package_id = package_id
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.deadline = deadline
        self.weight = weight
        self.status = status
        self.delivery_time = None
        self.depart_time = None

    def update_status(self, time_delta):
        match (self.delivery_time < time_delta, self.depart_time > time_delta):
            case (True, _):
                # User inputted time is after the delivery time
                self.status = "Delivered"
            case (_, True):
                # User inputted time is before the departure time
                self.status = "En route"
            case _:
                self.status = "At the hub"

    def __str__(self):
        return (f"Package ID: {self.package_id}, Address: {self.address}, City: {self.city}, State: {self.state},"
                f" Zip Code: {self.zip_code}, Deadline: {self.deadline}, Weight: {self.weight},"
                f" Status: {self.status}")

