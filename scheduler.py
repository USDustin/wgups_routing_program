

class DeliveryScheduler:

    def __init__(self):
        pass

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
        while remaining_packages:
            nearest_package = min(remaining_packages, key=lambda package:
            self.distance_table.get_distance(current_address_index,
                                            utils.get_address_index(self.package_table.lookup(package.package_id).address,
                                                                    address_list)))
            delivery_route.append(nearest_package)
            truck.packages.append(nearest_package)
            remaining_packages.remove(nearest_package)
            current_address_index = utils.get_address_index(self.package_table.lookup(nearest_package.package_id).address,
                                                            address_list)



