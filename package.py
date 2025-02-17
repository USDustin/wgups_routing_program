

class Package:

    def __init__(self, package_id, address, city, state, zip_code, deadline, weight, special_notes):
        self.package_id = package_id
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.deadline = deadline
        self.weight = weight
        self.special_notes = special_notes

    def update_status(self, time_delta):
        pass

    def __str__(self):
        return (f"Package ID: {self.package_id}, Address: {self.address}, City: {self.city}, State: {self.state},"
                f" Zip Code: {self.zip_code}, Deadline: {self.deadline}, Weight: {self.weight},"
                f" Special Notes: {self.special_notes}")

