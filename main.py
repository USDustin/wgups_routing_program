"""
Author: Dustin Luttrell
Student ID: 010433124
Email: dlutrel@wgu.edu
Date: 2025-02-27
"""

import utils
from distance_table import DistanceTable
from hashtable import HashTable
from interface import CommandLineInterface
from scheduler import DeliveryScheduler
from truck import Truck


def main():
    # Read the 3 csv files under resources and load in their data
    distance_table = DistanceTable("resources/distance-file.csv")
    package_list = utils.read_packages_file("resources/package-file.csv")
    address_list = utils.read_address_file("resources/address-file.csv")

    # Create a package table and load it with the package data
    package_table = HashTable()
    utils.load_package_table(package_list, package_table)

    # Create 3 trucks and manually load them with packages in an unoptimized order
    truck_1 = Truck(1)
    truck_2 = Truck(2)
    truck_3 = Truck(3)

    # Create a delivery scheduler and create an optimized route for each truck
    scheduler = DeliveryScheduler(distance_table, package_table, address_list)
    truck_1_route = scheduler.create_route(truck_1)
    truck_2_route = scheduler.create_route(truck_2)
    truck_3_route = scheduler.create_route(truck_3)

    # Load and deliver the packages in the optimized order
    # There are 3 trucks and 2 drivers
    # truck_3 can not leave until one of the others has returned, and it's after 10:20 AM
    scheduler.deliver_packages(truck_1, truck_1_route)
    scheduler.deliver_packages(truck_2, truck_2_route)

    depart_time = utils.depart_time(truck_1, truck_2)
    truck_3.depart_time = depart_time
    truck_3.current_time = depart_time
    scheduler.deliver_packages(truck_3, truck_3_route)

    # Create a command line interface and print the main menu
    truck_list = [truck_1, truck_2, truck_3]
    cli = CommandLineInterface(package_table, truck_list)
    cli.print_menu()


if __name__ == "__main__":
    main()
