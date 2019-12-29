from os import system, name
from time import sleep


def clear():
    if name == 'nt':
        system('cls')
    else:
        system('clear')


class RentalShop:
    shops = {}

    def __init__(self, name, bikes):
        self.shop_name = name
        self.bikes = bikes
        RentalShop.shops[name] = self

    def display(self, customer):
        clear()
        first_name = customer.name.split(" ")[0]
        blah = len(self.shop_name)*'='
        print("\nHi, {}! Welcome to \n\t{}\n\t{}\n\t{}\n\nAvailable Bikes:\n".format(
            first_name, blah, self.shop_name, blah))
        bike_list = []
        for number, item in enumerate(self.bikes.items()):
            bike_list.append(item[0])
            print("\t{}. {} => {} available".format(number + 1, *item))
        choice = int(input("Select your bike: "))
        customer.bike_selected = bike_list[choice - 1]
        self.take_request(customer)

    def take_request(self, customer):
        clear()
        print(f"Bike Selected: {customer.bike_selected}")
        rates = [("hourly", "hour", 5), ("daily", "day", 20),
                 ("weekly", "week", 60)]
        customer.basis = rates[customer.plan - 1]
        customer.duration = int(input(
            f"For how many {customer.basis[1]}s, do you wish to rent {customer.bike_selected}/s? "))
        customer.price = customer.basis[2] * \
            customer.duration * customer.bikes_required

        confirmation = input("\nIt will be ${} for {} {}/s to be rented on a/an {} basis for {} {}/s. \nDo you wish to continue (y/n): ".format(
            customer.price, customer.bikes_required, customer.bike_selected, customer.basis[0], customer.duration, customer.basis[1]))
        if confirmation in 'yY':
            self.rent(customer)
        elif confirmation in 'nN':
            print("Kindly start again!")
            start()

    def rent(self, customer):
        print("So, here you go! Kindly verify your identity when you arrive to take your rented bikes. Note: Keep track of time. Return the {} on or before scheduled date to avoid fines".format(customer.bike_selected))
        self.bikes[customer.bike_selected] -= customer.bikes_required
        print(self.bikes)


class Customer:
    customers = []

    def __init__(self, name):
        self.name = name
        self.make_choices()

    def make_choices(self):
        self.bikes_required = int(
            input(f"How many bikes do you wish to avail?\n=> "))
        print("Shops available according to your requirements:\n")
        for shop in RentalShop.shops.values():
            available_bikes = sum(shop.bikes.values())
            if self.bikes_required <= available_bikes:
                print("\t{} => {} bikes available".format(
                    shop.shop_name, available_bikes))
        shop_name = input("\nType the name of your shop's choice: ")
        self.shop = RentalShop.shops[shop_name]
        self.plan = int(input(
            "Available rental plans:\n\t1. Hourly => $5/hour\n\t2. Daily => $20/day\n\t3. Weekly => $60/week\n\n Select your plan: "))
        shop.display(self)
        Customer.customers.append(self)


def start():
    clear()
    who = input("Who are you?\n1. Shop Owner\t 2. Customer\n=> ")
    if who == '1':
        add_shop()
    elif who == '2':
        add_customer()


def add_shop():
    shop_name = input("\nEnter your shop's name: ")
    print("\nTime to add bikes to your shop. \n'''Keep pressing Enter after each entry to continue adding bikes and input any other key to exit'''\n")
    bikes = {}
    q = ""
    while not q:
        bike_name = input("Enter bike's name: ")
        quantity = int(input(f"Enter quantity of {bike_name}: "))
        bikes.setdefault(bike_name, quantity)
        q = input("=>")
    RentalShop(shop_name, bikes)
    start()


def add_customer():
    clear()
    print("Hello, customer!\n")
    name = input("May I know your good name: ")
    activity = input(
        "\nWhat do you wish to do?\n1. Rent bike/s\t2. Return bike/s")
    if activity == '1':
        Customer(name)
    elif activity == '2':
        if name in Customer.customer_list:
            Customer.return_bikes(name)
        else:
            print(
                "You have not rented any bikes yet! Kindly have a look at the available facilities.")
            Customer(name)


print("The market seems empty. \n\tLet's create our market!")
add_shop()
