
# Assignment 2 Programming Fundamentals
# John Murrowood s3923075
from datetime import datetime
import sys

# Sets the default rates for store discounts
class default_rate:
    customer = 0.00
    member = 0.05
    VIPMember = 0.10
    VIP_Price = 200

# Normal custemors will be stored as a customer class
class customer:

    def __init__(self, id, name, dis_rate, value):
        self.id = id
        self.name = name
        self.dis_rate = dis_rate
        self.value = value
  
    def get_discount(self, price):
        return (self.dis_rate, price)

    def display_info(self):
        print(f"Customer ID is: {self.id}")
        print(f"Customer name is: {self.name}")
        print(f"Customer value is: {self.value}")
        print(f"Customer discount is: {self.dis_rate}")
    # Updates the value of the member after they make an order
    def value_update(self, new_value):
        self.value = float(self.value) + new_value
# Store members data will be stored as a maber class
class member:

    def __init__(self, id, name, dis_rate, value):
        self.id = id
        self.name = name
        self.value = value
        self.dis_rate = dis_rate

    def get_discount(self, price):
        dis = 1.0 - self.dis_rate
        price = round(price * dis, 2)
        return (self.dis_rate, price)

    def display_info(self):
        print(f"Customer ID is: {self.id}")
        print(f"Customer name is: {self.name}")
        print(f"Customer value is: {self.value}")
        print(f"Customer discount is: {self.dis_rate}")
    # Updates the value of the member after they make an order
    def value_update(self, new_value):
        self.value = float(self.value) + new_value
# Store VIP Members will be stored as a VIPMember class
class VIPMember:
    threshold = 1000.00

    def __init__(self, id, name, dis_rate, value):
        self.id = id
        self.name = name
        self.value = value
        self.dis_rate = dis_rate
        self.dis_rate_sec = self.dis_rate + 0.05
    # Calculates member discount based on whether order is above or below class threshold
    def get_discount(self, price):
        if price <= VIPMember.threshold:
            discount = self.dis_rate
        else:
            discount = self.dis_rate_sec
        dis = 1.0 - discount
        price = round(price * dis, 2)
        return (discount, price)

    def display_info(self):
        print(f"Customer ID is: {self.id}")
        print(f"Customer name is: {self.name}")
        print(f"Customer value is: {self.value}")
        print(f"Customer discount threshold is: {VIPMember.threshhold}")
        print(f"Customer 1st discount rate is: {self.dis_rate_first}")
        print(f"Customer 2nd discount rate is: {self.dis_rate_sec}")
    # Sets the 1st discount rate for a VIP Member
    def set_rate(self, rate):
        self.dis_rate = rate
        self.dis_rate_sec = rate + 0.05
    # Updates the value of the member after they make an order
    def value_update(self, new_value):
        self.value = float(self.value) + new_value
    
    @staticmethod
    def set_threshold(threshold):
        VIPMember.threshold = threshold
# All store product information will be stored as a product class    
class product:

    def __init__(self, id, name, price, stock):
        self.id = id
        self.name = name
        self.price = price
        self.stock = stock
    # Allows for the product price to be changed
    def price_update(self):
        new_price = input("Enter new product price: ")
        i = 0
        while i == 0:
            try:
                new_price == type(float)
                self.price = new_price
                i = 1
            except:
                print("Error input must be decimal number above zero")
    # Changes the stock level of a product after an order has been made
    def stock_update(self, quantity):
        self.stock = int(self.stock) - quantity
# Store product bundles will be stored as a bundle class
# They are multipple products bundled together
class bundle:
    bundle_discount = 0.8
    
    def __init__(self, id, name, products, stock):
        self.id = id
        self.name = name
        self.products = products # List of products in bundle
        self.stock = stock
    # Calculates the bundle price based on 80% of combined products value in bundle
    def get_bundle_price(self):
        value = 0
        for i in self.products:
            product = operations.store_records.find_product(i)
            # Ensure all products of bundle have a store price
            try:
                value = value + float(product.price)
            except:
                print("Error: product in bundle has no price")
                return False
            value = value * bundle.bundle_discount
        return round(value, 2)
    # Changes the stock level after a bundle is purchased
    def stock_update(self, quantity):
        self.stock = int(self.stock) - quantity

# All orders made previously are stored as an order class        
class order:

    def __init__(self, customer, product, quantity, date):
        self. customer = customer 
        self.product = product  
        self.quantity = quantity
        self.value = 0
        self.date = date # date class object
    # Gets which customer type made the order        
    def get_customer_type(self):
        print(self.cust_type)
    # Calculates the quantity of a particular product in an order
    def get_order_quantity(self, product_name):
        for i in range(len(self.product)):
            if product_name == self.product[i]:
                order_quantity = self.quantity[i]
                return order_quantity

# All records of the classes mentioned above are stored as lists in the records class
# Input txt file lines are read into below lists
class records:
    customers = [] # list of customer/ member / VIP member class objects
    products = [] # list of product / bundle class objects
    orders = [] # list containing  order class objects
    # Checks if customers.txt file is in correct format
    def check_valid_cust_file(self, next_line):
        valid = True
        for i in operations.store_records.customers:
            if i.id == next_line[0]:
                valid = False
        if len(next_line) != 4:
            valid = False
        if "C" in next_line[0] or "M" in next_line[0] or "V" in next_line[0]:
            pass
        else:
            valid = False
        try:
            float(next_line[2])
            float(next_line[3])
            if float(next_line[2]) > 1 or float(next_line[2]) < 0:
                valid = False
            if float(next_line[3]) < 0:
                valid = False
        except:
            valid = False
        for i in next_line[1]:
            if i.isdigit():
                valid = False
        return valid
    # Reads in customers.txt file into records.customers list
    def read_customers(self, customers):
        file = open(customers,'r')
        while True:
            next_line = file.readline()
            if not next_line:
                break
            next_line = next_line.split(", ")
            if self.check_valid_cust_file(next_line) == True:
                if "C" in next_line[0]:
                    customer_add = customer(next_line[0], next_line[1], float(next_line[2]), float(next_line[3]))
                elif "M" in next_line[0]:
                    customer_add = member(next_line[0], next_line[1], float(next_line[2]), float(next_line[3]))
                else:
                    customer_add = VIPMember(next_line[0], next_line[1], float(next_line[2]), float(next_line[3]))
                self.customers.append(customer_add)
            else:
                # Returns an error message and ends task if an inorrectly formatted line is found
                print("Error: Invalid file format") 
                file.close() 
                return False
        file.close()

    # Checks if products.txt file is in correct format
    def check_valid_prod_file(self, next_line):
        valid = True
        for i in operations.store_records.products:
            if i.id == next_line[0]:
                valid = False
        if "P" in next_line[0]:
            if len(next_line) != 4:
                valid = False
            try:
                int(next_line[3])
                if int(next_line[3]) < 0:
                    valid = False
            except:
                valid = False
            for i in next_line[1]:
                if i.isdigit():
                    valid = False
        elif "B" in next_line[0]:
            for i in next_line[1]:
                if i.isdigit():
                    valid = False
            for i in next_line[-1]:
                if i.isdigit():
                    pass
            for i in next_line[2:-1]:
                if "P" not in i:
                    valid = False
        else:
            valid = False
        return valid
    # Reads in products.txt file into records.products list    
    def read_products(self, products ):
        file = open(products,'r')
        while True:
            next_line = file.readline()
            if not next_line:
                break
            next_line = next_line.split(", ")
            if self.check_valid_prod_file(next_line) == True:
                if "P" in next_line[0]:
                    product_add = product(next_line[0], next_line[1], next_line[2], int(next_line[3]))
                else:
                    prod_list = []
                    for i in next_line[2:-1]:
                        prod_list.append(i)
                    product_add = bundle(next_line[0], next_line[1], prod_list, int(next_line[-1]))
                self.products.append(product_add)    
            else:
                # Returns an error message and ends task if an inorrectly formatted line is found
                print("Error: Invalid file format") 
                file.close()
                return False
        file.close()
    # Finds a customer/ Member/ VIPMember from a name or ID in the customer records list
    def find_customer(self, customer):
        for i in records.customers:
            if i.id == customer:
                return i
            if i.name == customer:
                return i
        return None
    # Finds a customer and displays the customers information
    def display_customer(self, customer):
        for i in records.customers:
            if i.id == customer:
                print(f"Customer id is: {i.id}")
                print(f"Customer name is : {i.name}")
                print(f"Customer value is : {i.value}")
                return i
            if i.name == customer:
                print(f"Customer id is: {i.id}")
                print(f"Customer name is : {i.name}")
                print(f"Customer value is : {i.value}")
                return i
        return None
    # Finds a product / bundle from a name or ID in the products records list
    def find_product(self, product):
        for i in records.products:
            if i.id == product:
                return i
            if i.name == product:
                return i
        return None
    # Finds a product and displays the products information
    def display_product(self, product):
        for i in records.products:
            if i.id == product:
                print(f"Product id is: {i.id}")
                print(f"Product name is : {i.name}")
                print(f"Product price is : {i.price}")
                print(f"No. in Stock : {i.stock}")
                return i
            if i.name == product:
                print(f"Product id is: {i.id}")
                print(f"Product name is : {i.name}")
                print(f"Product price is : {i.price}")
                print(f"No. in Stock : {i.stock}")
                return i
        return None
    # prints a list of all the stored customers / members in the records customer list
    def list_customers(self):
        print("List of customers in Records:")
        print("ID".ljust(4),  "name".ljust(8), "Discount".ljust(8), "Value".ljust(8))
        for i in records.customers:
            print(f"{i.id} ".ljust(4),  f"{i.name} ".ljust(8),  f"{i.dis_rate} ".ljust(8), f"{round(i.value, 2)}".ljust(8))
    # prints a list of all the stored bundles / products in the records customer list
    def list_products(self):
        print("List of Products in Records:")
        print("ID".ljust(4),  "name".ljust(12), "Price".ljust(12),  "Stock".ljust(5))
        for i in records.products:
            if "P" in i.id:
                print(f"{i.id}".ljust(4),  f"{i.name}".ljust(12),  f"{i.price}".ljust(12), f"{i.stock}".ljust(5))
            else:
                 print(f"{i.id}".ljust(4),  f"{i.name}".ljust(12),   f"{', '.join(i.products)}".ljust(12), f"{i.stock}".ljust(5))
    # Generates a new customer numerical part of ID if a new customer makes an order
    def new_cust_id(self):
        j = "1"
        a = 0
        while a == 0:
            for i in records.customers:
                a = 1
                if j in i.id:
                    j = str(int(j) + 1)
                    a = 0
            return j
    # Ensures all lines of the order.txt file are read in correctly
    def check_valid_order_file(self, next_line):
        valid = True
        if operations.store_records.find_customer(next_line[0]) == None:
            valid = False
        n = 2 
        i = 1
        for x in next_line[1:-1]:
            if i % n == 0:
                if x.isdigit() == False:
                    valid = False
            else:
                if operations.store_records.find_product(x) == None:
                    valid = False
            i += 1
        try:
            date = datetime.strptime(next_line[-1].strip(), '%d/%m/%Y %H:%M:%S')
        except:
            valid = False
        return valid
    # Reads in all the orders stored in the order.txt file into records.orders list
    def read_orders(self, orders):
        file = open(orders,'r')
        while True:
            next_line = file.readline()
            if not next_line:
                break
            next_line = next_line.split(", ")
            if self.check_valid_order_file(next_line) == True:
                date = next_line[-1].strip()
                product_list = []
                quantity_list = []
                for i in next_line[1:-1]:
                    if i.isdigit() == True:
                        quantity_list.append(i)
                    else:
                        product_list.append(i)
                order_add = order(next_line[0], product_list, quantity_list, date)
                self.orders.append(order_add)
            else:
                print("\nInvalid order file format will proceed without order history\n")
                self.orders = []
                file.close()
                return False   
        file.close()
    # Prints a list of all the stored orders in the records list
    def list_orders(self):
        print("List of Orders in Records:\n")
        print("ID/ Name".ljust(9),  "product".ljust(25), "quantity".ljust(8), "Time".ljust(10))
        for i in records.orders:
            print(f"{i.customer}".ljust(9), f"{', '.join(i.product)}".ljust(25), f"{', '.join(i.quantity)}".ljust(8), end = " ")
            print(f"{i.date}".ljust(10))
    # Returns the number or orders containing a specified product
    def product_ordered_number(self, product):
        ordered_number = 0
        for i in records.orders:
            if product.id in i.product or product.name in i.product:
                ordered_number += 1
        return ordered_number
    # Returns how many times a specified product has been ordered
    def product_ordered_qty(self, product):
        ordered_number = 0
        for i in records.orders:
            for j in range(len(i.product)):
                if product.id == i.product[j] or product.name == i.product[j]:
                    ordered_number += int(i.quantity[j])
        return ordered_number
    # Re-writes the customers.txt file when program is exited including any changes in custermer value or new customers
    def write_customers(self):
        file = open("customers.txt",'w')
        for i in self.customers:
            line = f"{i.id}, {i.name}, {i.dis_rate}, {i.value}\n"
            file.write(line)
        file.close()
    # Re-writes the products.txt file when program is exited including any changes to stock levels or price
    def write_products(self):
        file = open("products.txt",'w')
        for i in self.products:
            if "B" in i.id:
                line = f"{i.id}, {i.name}, {', '.join(i.products)}, {i.stock}\n"
            else:
                line = f"{i.id}, {i.name}, {i.price}, {i.stock}\n" 
            file.write(line)
        file.close()
    # Re-writes the orders.txt file when program is exited including adding any new orders
    def write_orders(self):
        file = open("orders.txt",'w')
        for i in self.orders:
            product_lst = []
            for j in range(len(i.product)):
                product_lst.append(i.product[j])
                product_lst.append(i.quantity[j])
            line = f"{i.customer}, {', '.join(product_lst)}, {str(i.date)}\n" 
            file.write(line)
        file.close()
# This class handles all the menus and operational requirem,ents of the program    
class operations:
    # store_records contains all the customer, products and orders lists
    store_records = records()
    argument_list = list(sys.argv)
    # This method operates the main program interface and menus
    def menu(self):
        # Checks if any txt files given in command line and ensures there is the correct number
        if len(self.argument_list) > 4 or len(self.argument_list) == 2:
            print("Error: incorrect number of input arguments")
            print("Input python file followed by customers.txt, products.txt, orders.txt")
            return
        try:
            if self.store_records.read_customers(sys.argv[1]) == False:
                return
            if self.store_records.read_products(sys.argv[2]) == False:
                return           
        except:
            # if no customer or products file detected in command line, program will search directory
            if self.store_records.read_customers("customers.txt") == False:
                return
            if self.store_records.read_products("products.txt") == False:
                return

        try:
            self.store_records.read_orders(sys.argv[3])
        except:
            # If no order file given program will start without order history
            if len(self.argument_list) == 3:
                pass
            else:
                self.store_records.read_orders("orders.txt")
        # Main interface of program --> Can select which option to perform
        option = 1
        while option != 0:
            print("Welcome to the RMIT retail management system")
        
            print("\nYou can choose from the following options:")
            print("1 :".ljust(4), " Place an order")
            print("2 :".ljust(4), " Display Existing Customers")
            print("3 :".ljust(4), " Display Exisitng Products")
            print("4 :".ljust(4), " Adjust the discount rates of a VIP member")
            print("5 :".ljust(4), " Display all orders")
            print("6 :".ljust(4), " Display all orders of a customer")
            print("7 :".ljust(4), " Adjust threshold price for VIP Member")
            print("8 :".ljust(4), " Summarise all orders")
            print("9 :".ljust(4), " Display most valuable customer")
            print("10:".ljust(4), " Display most popular product")
            print("0 :".ljust(4), " Exit the program")
            print("\n")
            option = input("Choose one option: ")
            # Allows user to select which program to see
            # Each selection enters the relevant function
            if option == "1":
                self.place_an_order()
            elif option == "2":
                self.display_exisitng_customers()
            elif option == "3":
                self.display_exisitng_products()
            elif option == "4":
                self.adjust_VIPmember_rate()
            elif option == "5":
                self.display_all_orders()
            elif option == "6":
                self.display_customer_orders()
            elif option == "7":
                self.adjust_threshhold()
            elif option == "8":
                self.summarise_all_orders()
            elif option == "9":
                self.most_valued_customer()
            elif option == "10":
                self.popular_product()
            elif option == "0":
                # Upon exit all txt files will be re-written
                self.store_records.write_customers()
                self.store_records.write_products()
                if len(self.argument_list) == 3:
                    return
                else:
                    self.store_records.write_orders()
                    return
            else:
                print("Error invalid input (Must be integer 0 - 10 inclusive)\n")

    
    #Place an order function
    def place_an_order(self):
        customer_name = input("Enter the name of the customer:\n")
        # Adds all customer products and quantity to dictionary for easy adding to orders later
        customer_order = {}
        # while loop keeps going till customer doesnt want to purchase any more products
        j = 0
        while j == 0:
        # Adds customer name to store data if not already in there
            # while loop ensures correct inputs and keeps going till one entered
            i = 0
            while i == 0:
                customer_product = input("Enter the name of product chosen:\n")
                if self.store_records.find_product(customer_product) == None:
                    print("Error store does not have product")
                    print("Please enter another product")
                else:
                    i = 1
            # Checks quantity input acceptable
            i = 0
            while i == 0:
                prod_quantity = input("Enter amount of product chosen:\n")
                if prod_quantity.isdigit() == True:
                    if int(prod_quantity) > 0:
                        # Checks enough product stock left for order
                        if int(prod_quantity) <= self.store_records.find_product(customer_product).stock:
                            i = 1
                        else:
                            print("Error: Not enough of given product in stock")
                    else:
                        print("Error: Integer must be greter than 0")
                else:
                    print("Error: Please enter a positive integer value")
            customer_order[customer_product] = prod_quantity
            a = 0
            # checks for acceptable y or n inputs
            while a == 0:
                another_product = input("Would customer like another product? (y or n): ")
                if another_product == "n":
                    j = 1
                    a = 1
                elif another_product == "y":
                    a = 1
                else:
                    print("Error: must enter y for yes or n for no") 
        member_type = 0
        # Checks if customer exisitng in records
        # If not asks if they want a membership
        if self.store_records.find_customer(customer_name) == None:
            cust_id_new = str(self.store_records.new_cust_id())
            i = 0
            # while loop ensures acceptable input responses
            while i == 0:
                member_offer = input("Would customer like membership?: \n")
                if member_offer == "y" or member_offer == "n":
                    if member_offer == "y":
                        j = 0
                        while j == 0:
                            member_type = input("What membership type would customer like? (M or V)\n")
                            if member_type == "V":
                                customer_add = VIPMember(("V" + cust_id_new), customer_name, default_rate.VIPMember, 0.00)
                                j = 1
                                i = 1
                            elif member_type == "M":                                
                                customer_add = member(("M" + cust_id_new), customer_name, default_rate.member, 0.00)
                                j = 1
                                i = 1
                            else:
                                input("Error: must enter V for VIP or M for Member")     
                    else:
                        # adds new customer to records with necessary information
                        customer_add = customer(("C" + cust_id_new), customer_name, default_rate.customer, 0.00)
                        i = 1
                else:
                    print("Error: must enter y for yes or n for no")
            self.store_records.customers.append(customer_add)
        # Finds the customer in the store records and brings up details of customer
        current_customer = self.store_records.find_customer(customer_name)
        # Test if products have a price
        for key in customer_order:
            current_product = self.store_records.find_product(key)
            # Gets product or bundle unit prices and ensures they have a price on record for order to proceed
            if "B" in current_product.id:
                unit_price = current_product.get_bundle_price()
                if unit_price == False:
                    return
            else:
                try:
                    price = float(current_product.price)
                    if price <= 0:
                        print("Error: product has no price")
                        return
                except:
                    print("Error: product has no price")
                    return
        price_prelim = 0
        # Find total price of order by looping through all products in order
        for key in customer_order:
            current_product = self.store_records.find_product(key)
            if "B" in current_product.id:
                unit_price = current_product.get_bundle_price()
            else:    
                unit_price = float(current_product.price)
            price_prelim = price_prelim + float(unit_price) * int(customer_order[key])
        # Price after discount
        final_price = current_customer.get_discount(price_prelim)[1]
        discount = current_customer.get_discount(price_prelim)[0]
        # Prints all order data out using formatted strings and for loop to loop through all products in order
        if  member_type == "V":
            final_price = final_price + default_rate.VIP_Price
            for key in customer_order:
                print(f"\n{customer_name} purchases {key} x {customer_order[key]}.")
                if "B" in self.store_records.find_product(key).id:
                    unit_price = self.store_records.find_product(key).get_bundle_price()
                else:
                    unit_price = self.store_records.find_product(key).price
                print(f"Unit price:           {unit_price}(AUD)")
            print(f"Membership price:           {default_rate.VIP_Price}(AUD)")
            print(f"\n{customer_name} gets a discount of {(discount * 100)} %.")
            print(f"Total price:           {final_price:.2f} (AUD)")

        else:
            for key in customer_order:
                print(f"\n{customer_name} purchases {key} x {customer_order[key]}.")
                if "B" in self.store_records.find_product(key).id:
                    unit_price = self.store_records.find_product(key).get_bundle_price()
                else:
                    unit_price = self.store_records.find_product(key).price
                print(f"Unit price:           {unit_price}(AUD)")
            for i in range(18):
                print("-", end = " ")
            print(f"\n{customer_name} gets a discount of {(discount * 100)} %.")
            print(f"Total price:           {final_price:.2f} (AUD)")

        # Increase value of customer after order
        self.store_records.find_customer(customer_name).value_update(final_price)
        # Deacrease stock quantity after order
        for key in customer_order:
            self.store_records.find_product(key).stock_update(int(customer_order[key]))
        # Add order to store_records.orders
        products_list = []
        products_quantity = []
        for key in customer_order:
            products_list.append(key)
            products_quantity.append(customer_order[key])
        now = datetime.today()
        date = now.strftime("%d/%m/%Y %H:%M:%S")
        order_add = order(customer_name, products_list, products_quantity, date)
        self.store_records.orders.append(order_add)
            
        print("\n")
        input("Press any key to return to main menu: ")
        print("\n")
    # Method displays all existing customer data
    def display_exisitng_customers(self):
        self.store_records.list_customers()
        print("\n")
        input("Press any key to return to main menu: ")
        print("\n")
    # Method displays all exisitng product data
    def display_exisitng_products(self):
        self.store_records.list_products()
        print("\n")
        input("Press any key to return to main menu: ")
        print("\n")
    # Method adjusts the discount rate of a specified VIPMember
    def adjust_VIPmember_rate(self):
        i = 0
        # Ensures valid VIPMember entered
        while i == 0:
            customer = input("Enter VIP customer name or ID: ")
            if self.store_records.find_customer(customer) == None:
                print("Error: Invalid customer name or ID please try again")
            else:
                i = 1
        i = 0
        # Ensures an acceptable dicount rate is entered
        while i == 0:
            new_rate = input("Enter a new discount rate: ")
            try:
                new_rate = float(new_rate)
                if new_rate < 1 and new_rate > 0:
                    i = 1
                else:
                    print("Error: Number must be float between 0 and 1")
            except:
                print("Error: Number must be float between 0 and 1")
        customer = self.store_records.find_customer(customer)
        customer.set_rate(new_rate)
    # Displays all order data on record
    def display_all_orders(self):
        self.store_records.list_orders()
        print("\n")
        input("Press any key to return to main menu: ")
        print("\n")
    # Displays all orders made by a specified customer
    def display_customer_orders(self):
        customer_orders = []
        i = 0
        # Ensures inputed customer exists
        while i == 0:
            customer = input("Enter customer to find order details:\n")
            if self.store_records.find_customer(customer) == None:
                print("Error invalid customer please try again")
            else:
                i = 1
        customer_id = self.store_records.find_customer(customer).id
        customer_name = self.store_records.find_customer(customer).name
        for i in self.store_records.orders:
            if customer_id in i.customer or customer_name in i.customer:
                customer_orders.append(i)
        # Prints formatted strings of all orders
        print(f"List of orders for {customer}:\n")
        print("ID/ Name".ljust(9),  "Product".ljust(25), "Quantity".ljust(8), "Time".ljust(10))
        for i in customer_orders:
            print(f"{i.customer}".ljust(9), f"{', '.join(i.product)}".ljust(25), f"{', '.join(i.quantity)}".ljust(8), end = " ")
            print(f"{i.date}".ljust(10))
        print("\n")
        input("Press any key to return to main menu: ")
        print("\n")
        return customer_orders
    # Finds all orders made by a specific customer without printing information
    # Returns a dictionary or products and quantities purachsed across all orders for each product
    def find_customer_order(self, customer):
        customer_orders = []
        customer_products = {}
        customer_id = self.store_records.find_customer(customer).id
        customer_name = self.store_records.find_customer(customer).name
        for i in self.store_records.orders:
            if customer_id in i.customer or customer_name in i.customer:
                customer_orders.append(i)
        for orders in customer_orders:
            for i in range(len(orders.product)):
                customer_products[orders.product[i]] = orders.quantity[i]
        return customer_products
    # Changes the threshold value for the whole VIPMember class
    def adjust_threshhold(self):
        i = 0
        while i == 0:
            new_threshold = input("Enter new VIP Member threshold price:  ")
            try:
                new_threshold = float(new_threshold)
                if new_threshold > 0:
                    i = 1
                else:
                    print("Error must be float number greater than 0")
            except:
                print("Error must be float number greater than 0")
    # Prints out a table of all the products and quantity purchased by all customers on record
    def summarise_all_orders(self):
        print("\n        ", end=" ")
        for i in self.store_records.products:
            print(f"{i.id}", end=" ")
        print("\n")
        for i in self.store_records.customers:
            customer_order = self.find_customer_order(i.name)
            print(f"{i.name} ".ljust(9), end = " ")
            for j in self.store_records.products:
                if j.id in customer_order:
                    print(f"{customer_order[j.id]} ", end = " ")
                elif j.name in customer_order:
                    print(f"{customer_order[j.name]} ", end = " ")
                else:
                    print("0 ", end = " ")
            print("\n")
        for i in range(20):
            print("-", end = " ")
        print("\nOrderNum ".ljust(10), end = " ")
        for j in self.store_records.products:
            print(f"{self.store_records.product_ordered_number(j)} ", end = " ")
        print("\nOrderQty ".ljust(10), end = " ")
        for j in self.store_records.products:
            print(f"{self.store_records.product_ordered_qty(j)} ", end = " ")
        print("\n")
        input("\nPress any key to return to menu: ")
        print("\n")
    # Finds and prints the customer with the highest value across all customer classes
    def most_valued_customer(self):
        value = 0
        for i in self.store_records.customers:
            if i.value > value:
                most_valued = i.name
                value = i.value
        print(f"Most valuable customer is: {most_valued} with value of {value}$AUD")
        input("\nPress any key to return to menu: ")
        print("\n")
        return
    # Finds and prints the product in the most number of orders
    def popular_product(self):
        amount = 0
        for i in self.store_records.products:
            if self.store_records.product_ordered_number(i) > amount:
                popular_product = i
                amount = self.store_records.product_ordered_number(i)
        print(f"Most popular product is: {popular_product.name} with purchase amount of {amount}")
        input("\nPress any key to return to menu: ")
        print("\n")


operation = operations()
operation.menu()


