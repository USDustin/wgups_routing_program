import csv
from datetime import datetime, time

from package import Package
from truck import Truck

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

def create_truck(truck_number):
    """Creates a truck object with default values"""
    # Default values for all trucks
    # avg_speed = 18, truck_capacity = 16, starting_address = "4001 South 700 East", depart_time = "08:00:00"
    # One of the trucks can't leave until 10:20 am since the delivery address for package #9 is wrong
    avg_speed = 18
    truck_capacity = 16
    starting_address = "4001 South 700 East"
    depart_time = datetime.strptime("08:00:00", "%H:%M:%S").time()

    match truck_number:
        case 1:
            # Truck 1 (Leaves at 8:00 AM, prioritizes early deadlines)
            # 13 packages
            package_list = [1, 13, 14, 15, 16, 19, 20, 29, 30, 31, 34, 37, 40]
            truck = Truck(avg_speed, truck_capacity, package_list, 0,
                          0, starting_address, depart_time)
            return truck
        case 2:
            # Truck 2 (Leaves at 9:05 AM, takes delayed packages & must-be-on-truck-2 packages)
            # 8 packages
            package_list = [3, 6, 18, 25, 28, 32, 36, 38]
            truck = Truck(avg_speed, truck_capacity, package_list, 0,
                          0, starting_address, depart_time)
            return truck
        case 3:
            # Truck 3 (Leaves after 10:20 AM, takes package #9 and remaining packages)
            # 19 packages
            package_list = [2, 4, 5, 7, 8, 9, 10, 11, 12, 17, 21, 22, 23, 24, 26, 27, 33, 35, 39]
            truck = Truck(avg_speed, truck_capacity, package_list, 0,
                          0, starting_address, depart_time)
            return truck

