import datetime

import utils


class DeliveryScheduler:

    def __init__(self, distance_table, package_table, address_list):
        self.distance_table = distance_table
        self.package_table = package_table
        self.address_list = address_list


    def nearest_neighbor(self, truck, address_list):
        """
        Nearest Neighbor Algorithm

        """
        # Set the current_address to the hub
        # Create an empty list to store the delivery route returned by the algorithm
        # Create a copy of the truck's unoptimized package list
        # Clear the truck's unoptimized package list

        current_address_index = 0
        delivery_route = []
        remaining_packages = []

        for package_id in truck.packages:
            remaining_packages.append(self.package_table.lookup(package_id))
        truck.packages.clear()

        # While there are still packages to deliver
        # Find the nearest package to the current address calling min() on the remaining packages list
        # Customize comparison logic by passing a lambda function to min()
        # Lambda function compares the distance between the current address and the package address
        # Using distance_table and index of address in address_list
        # Append the nearest package to the delivery route
        while remaining_packages:
            nearest_package = min(remaining_packages, key=lambda package:
            self.distance_table.get_distance(current_address_index,
                                            utils.get_address_index(self.package_table.lookup(package.package_id).address,
                                                                    address_list)))
            delivery_route.append(nearest_package)
            remaining_packages.remove(nearest_package)
            current_address_index = utils.get_address_index(self.package_table.lookup(nearest_package.package_id).address,
                                                            address_list)
        # Return the optimized delivery route
        return delivery_route


    def create_route(self, truck):
        """Creates a route for each truck"""
        return self.nearest_neighbor(truck, self.address_list)

    def deliver_packages(self, truck, delivery_route):
        """
        Loads and delivers packages in the order determined by the nearest neighbor algorithm
        """
        current_address_index = 0
        # Load the truck with packages in order of delivery
        for package in delivery_route:
            truck.packages.append(package)
            truck.load += float(package.weight)

        # Deliver packages in order of delivery
        for package in delivery_route:
            # if truck.truck_id == 3:
            #     print(f'Truck 3 current time: {truck.current_time}')
            address_index = utils.get_address_index(package.address, self.address_list)
            miles = float(self.distance_table.get_distance(
                current_address_index, address_index))
            truck.miles += miles
            truck.address = package.address
            truck.current_time += datetime.timedelta(hours=(miles / truck.speed))
            package.delivery_time = truck.current_time
            package.depart_time = truck.depart_time
            current_address_index = address_index
