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
    match distance_list[address1_index][address2_index]:
        case "":
            return distance_list[address2_index][address1_index]
        case _:
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

def dijkstra_algorithm(distance_matrix, start_address):
    """ Dijkstra's Algo"""
    # float('inf') is used to represent infinity
    number_of_addresses = len(distance_matrix)
    unvisited_addresses = set(range(number_of_addresses))
    # Initialize the shortest distances list with all addresses as infinity
    shortest_distances = [float('inf')] * number_of_addresses
    # Initialize the previous addresses list with all addresses as none
    previous_addresses = [None] * number_of_addresses
    # Set the starting address distance to 0
    shortest_distances[start_address] = 0
    # Loop until all addresses have been visited
    while unvisited_addresses:
        # Find which address has the shortest distance
        current_address = min(unvisited_addresses, key=lambda address_index:
            shortest_distances[address_index])
        current_distance = shortest_distances[current_address]
        # Remove the current address from the unvisited set if it's not infinity
        if current_distance == float('inf'):
            break
        unvisited_addresses.remove(current_address)

        # Update distances to neighboring addresses
        for neighbor_index, distance in enumerate(distance_matrix[current_address]):
            if distance > 0 and neighbor_index in unvisited_addresses:
                new_distance = current_distance + distance
                if new_distance < shortest_distances[neighbor_index]:
                    shortest_distances[neighbor_index] = new_distance
                    previous_addresses[neighbor_index] = current_address




def generate_initial_route(distance_matrix, starting_location=0):
    """Generates an initial route using a greedy nearest neighbor algorithm"""
    """
    Create a set of unvisited locations and a route list
    Start at the starting location and remove it from unvisited locations
    Loop through the unvisited locations looking for the one with the shortest distance
        Find the nearest unvisited location
        Add it to the route
        Remove it from unvisited locations
    return the shortest route
    """
    number_of_locations = len(distance_matrix)
    unvisited_locations = set(range(number_of_locations))
    route = [starting_location]
    unvisited_locations.remove(starting_location)

    for _ in unvisited_locations:
        # Find the nearest unvisited location
        last_visited_location = route[-1]
        nearest_location = min(unvisited_locations, key=lambda location_index:
            distance_matrix[last_visited_location][location_index])
        route.append(nearest_location)
        unvisited_locations.remove(nearest_location)
    return route

#    while unvisited_locations:
#        current_location = route[-1]
#        nearest_location = min(unvisited_locations, key=lambda x: distance_matrix[current_location][x])
#        route.append(nearest_location)
#        unvisited_locations.remove(nearest_location)
#    pass
