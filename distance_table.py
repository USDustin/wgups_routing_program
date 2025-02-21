import csv

class DistanceTable:

    def __init__(self, file):
        self.file = file
        self.distance_list = self._read_distances()

    def _read_distances(self):
        """Reads resources/distance-file.csv and returns a 2D list of distance data."""
        with open(self.file, "r") as file:
            csv_reader = csv.reader(file)
            distance_list = list(csv_reader)
            return distance_list

    def get_distance(self, address1, address2):
        """Calculate the distance between two addresses using the data from distance-file.csv"""
        # Distance is stored in a 2D list
        # The larger index must be used for row and the smaller for column
        match self.distance_list[address1][address2]:
            case "":
                return float(self.distance_list[address2][address1])
            case _:
                return float(self.distance_list[address1][address2])

    def __str__(self):
        return f"{self.distance_list}"
