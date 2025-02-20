

class DistanceTable:

    def __init__(self):
        pass

    def _read_distances(self):
        """Reads resources/distance-file.csv and returns a 2D list of distance data."""
        with open(self.file, "r") as file:
            csv_reader = csv.reader(file)
            distance_list = list(csv_reader)
            return distance_list

    def get_distance(self, address1, address2):
        pass

    def __str__(self):
        pass
