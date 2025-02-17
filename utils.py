import csv
from package import Package

def load_package_list(package_list, package_table):
    """Loads package objects from list into a hash table"""
    # A.  Develop a hash table, without using any additional libraries or classes, that has an insertion function that
    # takes the package ID as input and inserts each of the following data components into the hash table:
    # •   delivery address
    # •   delivery deadline
    # •   delivery city
    # •   delivery zip code
    # •   package weight
    # •   delivery status (i.e., at the hub, en route, or delivered), including the delivery time
    for row in package_list:
        package = Package(
            package_id = int(row[0]),
            address = row[1],
            city = row[2],
            state = row[3],
            zip_code = row[4],
            deadline = row[5],
            weight = row[6],
            status = "at the hub"
        )
        package_table.insert(package.package_id, package)


def load_distances_csv(file_path):

    distances = []
    locations = []
    with open(file_path, "r") as file:
        csv_reader = csv.reader(file)
        locations = next(csv_reader)[1:]
        for row in csv_reader:
            distances.append([float(value) if value else 0.0 for value in row[1:]])
    return locations, distances

def read_packages_file(file_path):
    """Reads resources/package-file.csv and returns a list of package data."""
    with open(file_path, "r") as file:
        csv_reader = csv.reader(file)
        package_list = list(csv_reader)
        return package_list

def read_distances_file(file_path):
    """Reads resources/distance-file.csv and returns a list of distance data."""
    with open(file_path, "r") as file:
        csv_reader = csv.reader(file)
        distance_list = list(csv_reader)
        return distance_list

def read_address_file(file_path):
    """Reads resources/address-file.csv and returns a list of address data."""
    with open(file_path, "r") as file:
        csv_reader = csv.reader(file)
        address_list = list(csv_reader)
        return address_list

def calculate_distance(address1_index, address2_index, distance_list):
    """Calculate the distance between two addresses using the data from distance-file.csv"""
    # Distance is stored in a 2D list
    # The larger index must be used for row and the smaller for column
    if distance_list[address1_index][address2_index] == "":
        return distance_list[address2_index][address1_index]
    else:
        return distance_list[address1_index][address2_index]