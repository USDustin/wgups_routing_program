import datetime


class Package:

    def __init__(
        self, package_id, address, city, state, zip_code, deadline, weight, status
    ):
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
        if self.package_id == 9 and time_delta >= datetime.timedelta(hours=10, minutes=20):
            self.update_address("410 S State St", "Salt Lake City", "UT", "84111")
        elif self.package_id ==9 and time_delta < datetime.timedelta(hours=10, minutes=20):
            self.update_address("300 State St", "Salt Lake City", "UT", "84103")
        match (self.delivery_time < time_delta, self.depart_time > time_delta):
            case (True, _):
                # User inputted time is after the delivery time
                self.status = "Delivered"
            case (_, True):
                # User inputted time is before the departure time
                self.status = "At the hub"
                self.update_delayed_packages(time_delta)
            case _:
                # User inputted time is between the delivery and departure times
                self.status = "En route"

    def update_address(self, address, city, state, zip_code):
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code

    def update_delayed_packages(self, time_delta):
        """
        Updates the status of delayed packages
        """
        match (self.package_id, time_delta <= datetime.timedelta(hours=9, minutes=5)):
            case (6, True):
                self.status = "Delayed on flight - will not arrive to depot until 9:05 AM"
            case (25, True):
                self.status = "Delayed on flight - will not arrive to depot until 9:05 AM"
            case (28, True):
                self.status = "Delayed on flight - will not arrive to depot until 9:05 AM"
            case (32, True):
                self.status = "Delayed on flight - will not arrive to depot until 9:05 AM"
            case _:
                return


    def __str__(self):
        return (
            f"Package ID: {self.package_id}, Address: {self.address}, City: {self.city}, State: {self.state},"
            f" Zip Code: {self.zip_code}, Deadline: {self.deadline}, Weight: {self.weight},"
            f" Status: {self.status}, Delivery Time: {self.delivery_time}"
        )