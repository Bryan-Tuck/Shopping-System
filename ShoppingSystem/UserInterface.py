# -*- coding: utf-8 -*-
"""
Created on Thu May  6 21:29:51 2021

@author: Bryan
"""
import Customer
import Department
import Product
import Transaction
import pickle

LOOK_UP_CUSTOMER = 1
ADD_CUSTOMER = 2
CHANGE_CUSTOMER = 3
DELETE_CUSTOMER = 4
LOOK_UP_DEPARTMENT = 5
ADD_DEPARTMENT = 6
CHANGE_DEPARTMENT = 7
DELETE_DEPARTMENT = 8
LOOK_UP_PRODUCT = 9
ADD_PRODUCT = 10
CHANGE_PRODUCT = 11
DELETE_PRODUCT = 12
LOOK_UP_TRANSACTION = 13
ADD_TRANSACTION = 14
CHANGE_TRANSACTION = 15
DELETE_TRANSACTION = 16 
QUIT = 17

FILECUSTOMER = "Customers.dat"
FILEDEPARTMENT = "Departments.dat"
FILEPRODUCT = "Products.dat"
FILETRANSACTION = "Transactions.dat"



def main():
    
    # Load the existing customer dictionary and
    # assign it to mycustomers.
    mycustomers = load_customers()
    mydepartments = load_departments()
    myproducts = load_products()
    mytransactions = load_transactions()

    # Initialize a variable for the user's choice.
    choose = 0

    # Process menu selections until the user
    # wants to quit the program.
    while choose != QUIT:
        # Get the user's menu choice.
        choose = get_menu_choice()

        # Process the choice.
        if choose == LOOK_UP_CUSTOMER:
            look_up_customer(mycustomers)
        elif choose == ADD_CUSTOMER:
            add_customer(mycustomers)
        elif choose == CHANGE_CUSTOMER:
            change_customer(mycustomers)
        elif choose == DELETE_CUSTOMER:
            delete_customer(mycustomers)
        elif choose == LOOK_UP_DEPARTMENT:
            look_up_department(mydepartments)
        elif choose == ADD_DEPARTMENT:
            add_department(mydepartments)
        elif choose == CHANGE_DEPARTMENT:
            change_department(mydepartments)
        elif choose == DELETE_DEPARTMENT:
            delete_department(mydepartments)
        elif choose == LOOK_UP_PRODUCT:
            look_up_product(myproducts)
        elif choose == ADD_PRODUCT:
            add_product(myproducts)
        elif choose == CHANGE_PRODUCT:
            change_product(myproducts)
        elif choose == DELETE_PRODUCT:
            delete_product(myproducts)
        elif choose == LOOK_UP_TRANSACTION:
            look_up_transaction(mytransactions)
        elif choose == ADD_TRANSACTION:
            add_transaction(mytransactions)
        elif choose == CHANGE_TRANSACTION:
            change_transaction(mytransactions)
        elif choose == DELETE_TRANSACTION:
            delete_transaction(mytransactions)
        

    # Save the data dictionary to a file.
    save_customers(mycustomers)
    save_departments(mydepartments)
    save_products(myproducts)
    save_transactions(mytransactions)
    
def load_customers():
        
    try:
        # Open the Customers.dat file.
        input_file = open(FILECUSTOMER, 'rb')
            
        # Unpickle the dictionary.
        customer_dct = pickle.load(input_file)
            
        # Close the Customers.dat file.
        input_file.close()
    except IOError:
        # Could not open the file, so create
        # an empty dictionary.
        customer_dct = {}
                
        # Return the dictionary.
    return customer_dct

    
def load_departments():
        
    try:
        # Open the departments.dat file.
        input_file = open(FILEDEPARTMENT, 'rb')
            
        # Unpickle the dictionary.
        department_dct = pickle.load(input_file)
            
        # Close the departments.dat file.
        input_file.close()
    except IOError:
        # Could not open the file, so create
        # an empty dictionary.
        department_dct = {}
                
        # Return the dictionary.
    return department_dct


def load_products():
        
    try:
        # Open the products.dat file.
        input_file = open(FILEPRODUCT, 'rb')
            
        # Unpickle the dictionary.
        product_dct = pickle.load(input_file)
            
        # Close the products.dat file.
        input_file.close()
    except IOError:
        # Could not open the file, so create
        # an empty dictionary.
        product_dct = {}
                
        # Return the dictionary.
    return product_dct


def load_transactions():
        
    try:
        # Open the transactions.dat file.
        input_file = open(FILETRANSACTION, 'rb')
            
        # Unpickle the dictionary.
        transaction_dct = pickle.load(input_file)
            
        # Close the transactions.dat file.
        input_file.close()
    except IOError:
        # Could not open the file, so create
        # an empty dictionary.
        transaction_dct = {}
                
        # Return the dictionary.
    return transaction_dct

    # The get_menu_choice function displays the menu
    # and gets a validated choice from the user.
    
def get_menu_choice():
    print()
    print('Menu')
    print('---------------------------')
    print('1. Look up a customer')
    print('2. Add a new customer')
    print('3. Change an existing customer')
    print('4. Delete a customer')
    print('5. Look up a department')
    print('6. Add a new department')
    print('7. Change an existing department')
    print('8. Delete a department')    
    print('9. Look up a product')
    print('10. Add a new product')
    print('11. Change an existing product')
    print('12. Delete a product')
    print('13. Look up a transaction')
    print('14. Add a new transaction')
    print('15. Change an existing transaction')
    print('16. Delete a transaction')
    print('17. Quit the program')
    print()

    # Get the user's choice.
    choose = int(input('Enter your choice: '))
    
    # Validate the choice.
    while choose < LOOK_UP_CUSTOMER or choose > QUIT:
        choose = int(input('Enter a valid choice: '))

    # return the user's choice.
    return choose

   # The look_up function looks up an item in the
   # specified dictionary.
def look_up_customer(mycustomers):
    # Get a name to look up.
    name = input('Enter a name: ')

    # Look it up in the dictionary.
    print(mycustomers.get(name, 'That name is not found.'))
    
def look_up_department(mydepartments):
    # Get a name to look up.
    department_name = input('Enter a name: ')

    # Look it up in the dictionary.
    print(mydepartments.get(department_name, 'That name is not found.'))
    
def look_up_product(myproducts):
    # Get a name to look up.
    product_name = input('Enter a name: ')

    # Look it up in the dictionary.
    print(myproducts.get(product_name, 'That name is not found.'))
    
def look_up_transaction(mytransactions):
    # Get a name to look up.
    transaction_name = input('Enter a name: ')

    # Look it up in the dictionary.
    print(mytransactions.get(transaction_name, 'That name is not found.'))

# The add function adds a new entry into the
# specified dictionary.
def add_customer(mycustomers):
    # Get the customers info.
    name = input('Name: ')
    street = input('Street: ')
    city = input('City: ')
    zip_code = input('Zip Code: ')
    
    # Create a Customer object named entry.
    entry = Customer.Customer(name, street, city, zip_code)

    # If the name does not exist in the dictionary,
    # add it as a key with the entry object as the
    # associated value.
    if name not in mycustomers:
        mycustomers[name] = entry
        print('The entry has been added.')
    else:
        print('That name already exists.')
        
def add_department(mydepartments):
    # Get the departments info.
    department_name = input('Department Name: ')
    department_number = input('Department Number: ')
    description = input('Description: ')
    department_id = input('Department ID: ')
    
    # Create a department object named entry.
    entrytwo = Department.department(department_name, department_number, description, department_id)

    # If the name does not exist in the dictionary,
    # add it as a key with the entry object as the
    # associated value.
    if department_name not in mydepartments:
        mydepartments[department_name] = entrytwo
        print('The entry has been added.')
    else:
        print('That name already exists.')
        
def add_product(myproducts):
    # Get the products info.
    product_name = input('Product Name: ')
    product_brand = input('Product Number: ')
    product_id = input('Product ID: ')
    product_price = input('Product Price: ')
    product_country = input('Product Country Origin: ')
    
    # Create a product object named entry.
    entrythree = Product.product(product_name, product_brand, product_id, product_price, product_country)

    # If the name does not exist in the dictionary,
    # add it as a key with the entry object as the
    # associated value.
    if product_name not in myproducts:
        myproducts[product_name] = entrythree
        print('The entry has been added.')
    else:
        print('That name already exists.')
        
def add_transaction(mytransactions):
    # Get the transaction info.
    transaction_name = input('Transaction Name: ')
    total_price = input('Total Price: ')
    payment_info = input('Payment Information: ')
    cc_number = input('Credit Card Number: ')
    cc_expdate = input('Credit Card Expiration Date: ')
    
    # Create a transaction object named entry.
    entryfour = Transaction.Transaction(transaction_name, total_price, payment_info, cc_number, cc_expdate)

    # If the name does not exist in the dictionary,
    # add it as a key with the entry object as the
    # associated value.
    if transaction_name not in mytransactions:
        mytransactions[transaction_name] = entryfour
        print('The entry has been added.')
    else:
        print('That name already exists.')
        
# The change function changes an existing
# entry in the specified dictionary.
def change_customer(mycustomers):
    # Get a name to look up.
    name = input('Enter a name: ')

    if name in mycustomers:
        # Get a new street.
        street = input('Enter the new street: ')

        # Get a new city.
        city = input('Enter the new city: ')
            
        #Get a new zip code
        zip_code = input('Enter the new zip code: ')

        # Create a contact object named entry.
        entry = Customer.Customer(name, street, city, zip_code)

        # Update the entry.
        mycustomers[name] = entry
        print('Information updated.')
    else:
        print('That name is not found.')
        
def change_department(mydepartments):
    # Get a name to look up.
    department_name = input('Enter a department name: ')

    if department_name in mydepartments:
        # Get a new department number.
        department_number = input('Enter the new department name: ')

        # Get a new description.
        description = input('Enter the new description: ')
            
        #Get a new department ID
        department_id = input('Enter the new department ID: ')

        # Create a contact object named entrytwo.
        entrytwo = Department.department(department_name, department_number, description, department_id)

        # Update the entry.
        mydepartments[department_name] = entrytwo
        print('Information updated.')
    else:
        print('That name is not found.')
        
def change_product(myproducts):
    # Get a name to look up.
    product_name = input('Enter a product name: ')

    if product_name in myproducts:
        # Get a new product brand.
        product_brand = input('Enter the new product brand name: ')

        # Get a new product id.
        product_id = input('Enter the new product ID: ')
            
        #Get a new product price
        product_price = input('Enter the new product price: ')
        
        #get a new product country
        product_country = input('Enter the new product country: ')

        # Create a product object named entrythree.
        entrythree = Product.Product(product_name, product_brand, product_id, product_price, product_country)

        # Update the entry.
        myproducts[product_name] = entrythree
        print('Information updated.')
    else:
        print('That name is not found.')
        
def change_transaction(mytransactions):
    # Get a name to look up.
    transaction_name = input('Enter a transaction name: ')

    if transaction_name in mytransactions:
        # Get a new total price.
        total_price = input('Enter the new total price: ')

        # Get a new payment info.
        payment_info = input('Enter the new payment information: ')
            
        #Get a new credit card number
        cc_number = input('Enter the new credit card number: ')
        
        #get a new credit card exipiration date
        cc_expdate = input('Enter the new credit card expiration date: ')

        # Create a transaction object named entryfour.
        entryfour = Transaction.Transaction(transaction_name, total_price, payment_info, cc_number, cc_expdate)

        # Update the entry.
        mytransactions[transaction_name] = entryfour
        print('Information updated.')
    else:
        print('That name is not found.')        

# The delete functions deletes an entry from the
# specified dictionary.
def delete_customer(mycustomers):
    # Get a name to look up.
    name = input('Enter a name: ')

    # If the name is found, delete the entry.
    if name in mycustomers:
        del mycustomers[name]
        print('Entry deleted.')
    else:
        print('That name is not found.')
        
def delete_department(mydepartments):
    # Get a department to look up.
    department_name = input('Enter a department name: ')

    # If the name is found, delete the entry.
    if department_name in mydepartments:
        del mydepartments[department_name]
        print('Entry deleted.')
    else:
        print('That name is not found.')
        
def delete_product(myproducts):
    # Get a product to look up.
    product_name = input('Enter a product name : ')

    # If the name is found, delete the entry.
    if product_name in myproducts:
        del myproducts[product_name]
        print('Entry deleted.')
    else:
        print('That name is not found.')

def delete_transaction(mytransactions):
    # Get a transaction to look up.
    transaction_name = input('Enter a transaction name: ')

    # If the name is found, delete the entry.
    if transaction_name in mytransactions:
        del mytransactions[transaction_name]
        print('Entry deleted.')
    else:
        print('That name is not found.')
        
# The save functions pickles the specified
# object and saves it to the contacts file.
def save_customers(mycustomers):
    # Open the file for writing.
    output_file = open(FILECUSTOMER, 'wb')

    # Pickle the dictionary and save it.
    pickle.dump(mycustomers, output_file)

    # Close the file.
    output_file.close()   
    
def save_departments(mydepartments):
    # Open the file for writing.
    output_file = open(FILEDEPARTMENT, 'wb')

    # Pickle the dictionary and save it.
    pickle.dump(mydepartments, output_file)

    # Close the file.
    output_file.close() 
    
def save_products(myproducts):
    # Open the file for writing.
    output_file = open(FILEPRODUCT, 'wb')

    # Pickle the dictionary and save it.
    pickle.dump(myproducts, output_file)

    # Close the file.
    output_file.close() 
    
def save_transactions(mytransactions):
    # Open the file for writing.
    output_file = open(FILETRANSACTION, 'wb')

    # Pickle the dictionary and save it.
    pickle.dump(mytransactions, output_file)

    # Close the file.
    output_file.close() 

main()     
               
