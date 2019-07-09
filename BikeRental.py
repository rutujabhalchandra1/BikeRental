"""
A full fledged bike rental system implemented in Python using object oriented programming.

Customers can
See available bikes on the shop
Rent bikes on hourly basis $5 per hour.
Rent bikes on daily basis $20 per day.
Rent bikes on weekly basis $60 per week.
Family Rental, a promotion that can include from 3 to 5 Rentals (of any type) with a discount of 30% of the total price


The bike rental shop can
issue a bill when customer decides to return the bike.
display available inventory
take requests on hourly, daily and weekly basis by cross verifying stock

For simplicity we assume that
Any customer requests rentals of only one type i.e hourly, monthly or weekly
Is free to chose the number of bikes he/she wants
Requested bikes should be less than available stock.

"""

STOCK = 100


class BikeRental:
    def __init__(self, user_info):
        self.stock = STOCK
        self.user_info = user_info
        self.rates = {"hourly": 5, "daily": 20, "weekly": 60}

    def issue_bill(self):
        if self.user_info["num_of_bikes"] < self.stock:
            self.stock += self.user_info["num_of_bikes"]
            print("You have returned {} bikes".format(self.user_info["num_of_bikes"]))
            if self.user_info['family_promotion']:
                return ((self.user_info["num_of_bikes"]
                * self.user_info["bike_rent_dur"]
                * self.rates[self.user_info["type"]]) -
                        0.3 * (
                self.user_info["num_of_bikes"]
                * self.user_info["bike_rent_dur"]
                * self.rates[self.user_info["type"]]
            ))
            return (
                self.user_info["num_of_bikes"]
                * self.user_info["bike_rent_dur"]
                * self.rates[self.user_info["type"]]
            )
        else:
            return

    def display_inventory(self):
        print("Available bikes are {}".format(self.stock))

    def rent_bike(self):
        if self.user_info["num_of_bikes"] < 1:
            print("Invalid number")
        else:
            if 3 >= self.user_info["num_of_bikes"] <= 5:
                self.user_info["family_promotion"] = True
            if self.user_info["num_of_bikes"] > self.stock:
                print("We currently have only {} bikes to rent".format(self.stock))
                return
            else:
                print("You have rented {} bikes".format(self.user_info["num_of_bikes"]))
                self.stock -= self.user_info["num_of_bikes"]


class Customer:
    def __init__(self, id, type, bike_rent_dur, num_of_bikes):
        self.user_info = {}
        self.user_info["id"] = id
        self.user_info["type"] = type
        self.user_info["bike_rent_dur"] = bike_rent_dur
        self.user_info["num_of_bikes"] = num_of_bikes
        self.user_info["family_promotion"] = False
        self.bike_shop = BikeRental(self.user_info)

    def see_available_bikes(self):
        self.bike_shop.display_inventory()

    def rent_bike(self):
        self.bike_shop.rent_bike()

    def return_bike(self):
        total_charge = self.bike_shop.issue_bill()
        if total_charge:
            print(("Total rental amount is {}$").format(total_charge))


if __name__ == "__main__":
    customer_obj = Customer(1, "daily", 2, 3)
    customer_obj.see_available_bikes()
    customer_obj.rent_bike()
    customer_obj.see_available_bikes()
    customer_obj.return_bike()
