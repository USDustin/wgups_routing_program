import csv
from package import Package

def load_packages(package_list, package_table):
    """Loads package list from csv file into a hash table"""
    for row in package_list:
        package = Package(
            package_id = int(row[0]),
            address = row[1],
            city = row[2],
            state = row[3],
            zip_code = row[4],
            deadline = row[5],
            weight = row[6],
            special_notes = row[7]
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
    # Distance is stored in a 2D list, where the first index is the row and the second index is the column
    # The larger index must be used for row and the smaller for column
    if distance_list[address1_index][address2_index] is "":
        return distance_list[address2_index][address1_index]
    else:
        return distance_list[address1_index][address2_index]