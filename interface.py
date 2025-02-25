import datetime


class CommandLineInterface:
    def __init__(self, package_table, truck_list):
        self.package_table = package_table
        self.truck_list = truck_list

    def print_total_miles(self):
        total_miles = 0
        for truck in self.truck_list:
            total_miles += truck.miles
        print(f"\nTotal miles driven: {total_miles}")

    def print_package_status(self):
        """
        Allows the user to view the status of a single package by ID at a specific time.
        """
        try:
            package_id = int(input("\nEnter a package ID: "))
            if package_id < 1 or package_id > 40:
                raise ValueError
            try:
                input_time = input("Enter a time (HH:MM:SS): ")
                (hours, minutes, seconds) = input_time.split(":")
                time_delta = datetime.timedelta(hours=int(hours), minutes=int(minutes), seconds=int(seconds))
                package = self.package_table.lookup(package_id)
                package.update_status(time_delta)
                print(str(package))
            except ValueError:
                print("\n❌ Invalid time format. Please enter a valid time (HH:MM:SS).")
                return
        except ValueError:
            print("\n❌ Invalid input! Please enter a numeric package ID (1-40).")


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

    def print_menu(self):
        while True:
            print(f'\n' + f'=' * 50)
            print(f"{'Western Governors University Parcel Service': ^50}")
            print(f'=' * 50)
            print(f'\n1. View delivery status of a package')
            print(f'2. View all packages at a specific time')
            print(f'3. View total mileage traveled by all trucks')
            print(f'4. Exit\n')

            choice = input(f'Enter your choice (1-4): ').strip()

            match choice:
                case "1":
                    self.print_package_status()
                    return_to_menu()
                case "2":
                    self.print_all_packages()
                    return_to_menu()
                case "3":
                    self.print_total_miles()
                    return_to_menu()
                case "4":
                    break
                case _:
                    print(f'❌ Invalid choice. Please try again.')

def return_to_menu():
    while True:
        try:
            print("\n")
            input("Press Enter to return to the main menu...")
            break
        except ValueError:
            print("❌ Invalid input! Please try again.")