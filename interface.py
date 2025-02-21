import datetime


class CommandLineInterface:
    def __init__(self, package_table, truck_list):
        self.package_table = package_table
        self.truck_list = truck_list

    def print_total_miles(self):
        total_miles = 0
        for truck in self.truck_list:
            total_miles += truck.miles
        print(f"Total miles driven: {total_miles}")
        return total_miles

    def print_package_status(self):
        """Allows the user to view the status of a single package by ID at a specific time."""
        try:
            package_id = int(input("Enter a package ID: "))
            try:
                input_time = input("Enter a time (HH:MM:SS): ")
                (hours, minutes, seconds) = input_time.split(":")
                time_delta = datetime.timedelta(int(hours), int(minutes), int(seconds))
                package = self.package_table.lookup(package_id)
                package.update_status(time_delta)
                print(f"{package.__str__()}")
            except ValueError:
                print("\n❌ Invalid time format. Please enter a valid time (HH:MM:SS).")
                return
        except ValueError:
            print("\n❌ Invalid input! Please enter a numeric package ID (1-40) and valid time (HH:MM:SS).")


    def get_input_time(self):
        pass

    def print_menu(self):
        while True:
            print("\n" + "=" * 50)
            print(f"{'Western Governors University Parcel Service': ^50}")
            print("=" * 50)
            print("\n1. View delivery status of a package")
            print("2. View all packages at a specific time")
            print("3. View total mileage traveled by all trucks")
            print("4. Exit\n")

            choice = input("Enter your choice (1-4): ").strip()

            match choice:
                case "1":
                    self.print_package_status()
                case "2":
                    self.get_input_time()
                case "3":
                    self.print_total_miles()
                case "4":
                    break
                case _:
                    print("Invalid choice. Please try again.")
