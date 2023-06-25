# Travel Agency

# This file will contain all the code required to create a travel agency program.

#Define class for travel agency
class TravelAgency(object):
    #initialize with empty list of customers
    def __init__(self):
        self.customers = []

    #Create function to add customer to list
    def add_customer(self,customer):
        self.customers.append(customer)

    #Create function to remove customer from list
    def remove_customer(self,customer):
        self.customers.remove(customer)

#Define class for customers
class Customer(object):
    #initialize with empty list of destinations
    def __init__(self):
        self.destinations = []

    #Create function to add destination to customer list
    def add_destination(self,destination):
        self.destinations.append(destination)

    #Create function to remove destination from customer list
    def remove_destination(self,destination):
        self.destinations.remove(destination)

#Define class for destinations
class Destination(object):
    #initialize with name, price, and description
    def __init__(self, name, price, description):
        self.name = name
        self.price = price
        self.description = description

    #Create function to get description
    def get_description(self):
        return self.description

#Create function to search customers for specific destination
def search_customer_for_destination(travel_agency, destination):
    found_customers = []
    #Loop through customers
    for customer in travel_agency.customers:
    #If customer has destination, append to list
        if destination in customer.destinations:
            found_customers.append(customer)
    #Return list of found customers
    return found_customers

#Create function to print list of customers who have specific destination
def print_customers_with_destination(travel_agency, destination):
    customers = search_customer_for_destination(travel_agency, destination)
    #Loop through customers
    for customer in customers:
    #Print customer name
        print("Customer: " + customer.name)

#Create sample data
paris = Destination('Paris', 500, 'The City of Light')
london = Destination('London', 300, 'The Big Smoke')

john = Customer()
john.name = "John Smith"
john.add_destination(paris)
john.add_destination(london)

jane = Customer()
jane.name = "Jane Doe"
jane.add_destination(paris)

travel_agency = TravelAgency()
travel_agency.add_customer(john)
travel_agency.add_customer(jane)

#Search customers with Paris destination and print their names
print_customers_with_destination(travel_agency, paris)

#Expected output:
#Customer: John Smith
#Customer: Jane Doe