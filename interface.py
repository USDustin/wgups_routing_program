import datetime


class CommandLineInterface:
    def __init__(self, package_table, truck_list):
        self.package_table = package_table
        self.truck_list = truck_list

    def print_total_miles(self):
        total_miles = 0
        for truck in self.truck_list:
            total_miles += truck.miles
        print(f"\nTotal miles driven: {total_miles:.2f}\n")

    def print_miles_by_truck(self):
        for truck in self.truck_list:
            print(f'Truck {truck.truck_id} miles driven: {truck.miles:.2f}')

    def print_package_status(self):
        """
        Allows the user to view the status of a single package by ID at a specific time.
        """
        package_id = get_user_package_id_input()
        timedelta = get_user_time_input()
        package = self.package_table.lookup(package_id)
        package.update_status(timedelta)
        print(str(package))

    def print_all_packages(self):
        """
        Prints all packages at a specific time
        """
        try:
            input_time = input("Enter a time (HH:MM:SS): ")
            (hours, minutes, seconds) = input_time.split(":")
            time_delta = datetime.timedelta(hours=int(hours), minutes=int(minutes), seconds=int(seconds))
            for package_id in range(1, 41):
                package = self.package_table.lookup(package_id)
                package.update_status(time_delta)
                print(str(package))
        except ValueError:
            print("\n❌ Invalid time format. Please enter a valid time (HH:MM:SS).")

    def print_packages_by_truck(self):
        """
        Prints the status of all packages loaded onto a specific truck at a specific time
        """
        try:
            truck_id = get_user_truck_id_input()
            timedelta = get_user_time_input()
            truck = self.truck_list[truck_id - 1]
            for package in truck.packages:
                package.update_status(timedelta)
                print(str(package))
        except ValueError:
            print("\n❌ Invalid input! Please enter a numeric truck ID (1-3).")
            return

    def print_menu(self):
        while True:
            print(f'\n' + f'=' * 50)
            print(f"{'Western Governors University Parcel Service': ^50}")
            print(f'=' * 50)
            print(f'\n1. View status of a package at a specific time')
            print(f'2. View status of all packages at a specific time')
            print(f'3. View total mileage traveled by all trucks')
            print(f'4. View status of packages per truck')
            print(f'5. Exit\n')

            choice = input(f'Enter your choice (1-5): ').strip()

            match choice:
                case "1":
                    self.print_package_status()
                    return_to_menu()
                case "2":
                    self.print_all_packages()
                    return_to_menu()
                case "3":
                    self.print_total_miles()
                    self.print_miles_by_truck()
                    return_to_menu()
                case "4":
                    self.print_packages_by_truck()
                    return_to_menu()
                case "5":
                    print(f'\nGoodbye!')
                    break
                case _:
                    print(f'\n❌ Invalid choice. Please try again.')

def return_to_menu():
    while True:
        try:
            input("\nPress Enter to return to the main menu...")
            break
        except ValueError:
            print("\n❌ Invalid input! Please try again.")

def get_user_package_id_input():
    try:
        package_id = int(input(f'Enter a package ID: '))
        if package_id < 1 or package_id > 40:
            raise ValueError
        return package_id
    except ValueError:
        print(f'\n❌ Invalid package ID! Please enter a numeric package ID (1-40).')
        return

def get_user_truck_id_input():
    try:
        truck_id = int(input(f'\nEnter a truck ID (1-3): '))
        if truck_id < 1 or truck_id > 3:
            raise ValueError
        return truck_id
    except ValueError:
        print(f'\n❌ Invalid truck ID! Please enter a numeric truck ID (1-3).')
        get_user_truck_id_input()

def get_user_time_input():
    try:
        input_time = input(f'\nEnter a time (HH:MM:SS): ')
        return get_timedelta(input_time)
    except ValueError:
        print(f'\n❌ Invalid time format. Please enter a valid time (HH:MM:SS).')
        get_user_time_input()

def get_timedelta(input_time):
    (hours, minutes, seconds) = input_time.split(':')
    return datetime.timedelta(hours=int(hours), minutes=int(minutes), seconds=int(seconds))
