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

    distance_table = DistanceTable("resources/distance-file.csv")
    distance_list = distance_table.distance_list
    package_list = utils.read_packages_file("resources/package-file.csv")
    package_table = HashTable()
    address_list = utils.read_address_file("resources/address-file.csv")

    package_table = HashTable()
    utils.load_package_list(package_list, package_table)

    #print(package_table.__str__())
    #print(package_table.__len__())
    #print(package_table.lookup(5))

    distance_between = utils.calculate_distance(10,5,distance_list)

    truck_1 = Truck(1)
    truck_2 = Truck(2)
    truck_3 = Truck(3)

    truck_1.load_truck()
    truck_2.load_truck()
    truck_3.load_truck()


if __name__ == "__main__":
    main()
