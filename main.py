"""
Author: Dustin Luttrell
Student ID: 010433124
Email: dlutrel@wgu.edu
Date: 2025-02-10
"""
import utils
from hashtable import HashTable
from distance_table import DistanceTable
from package import Package
from scheduler import DeliveryScheduler
from truck import Truck

from datetime import datetime, time


def main():

    package_list = utils.read_packages_file("resources/package-file.csv")
    distance_list = utils.read_distances_file("resources/distance-file.csv")
    address_list = utils.read_address_file("resources/address-file.csv")

    package_table = HashTable()
    utils.load_package_list(package_list, package_table)

    #print(package_table.__str__())
    #print(package_table.__len__())
    #print(package_table.lookup(5))

    distance_between = utils.calculate_distance(10,5,distance_list)

    # Initialize 3 trucks and load them with data
    truck_1 = utils.create_truck(1)
    truck_2 = utils.create_truck(2)
    truck_3 = utils.create_truck(3)




    # Initialize the truck objects
    #depart_time_str = "08:00:00"
    #depart_time = datetime.strptime(depart_time_str, "%H:%M:%S").time()
    #truck_1 = Truck(16,18, depart_time,)

    # Load the trucks
    # Schedule the deliveries
    # Deliver the packages




if __name__ == "__main__":
    main()
