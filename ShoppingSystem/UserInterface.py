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

LOOK_UP = 1
ADD = 2
CHANGE = 3
DELETE = 4
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
    choice = 0

    # Process menu selections until the user
    # wants to quit the program.
    while choice != QUIT:
        # Get the user's menu choice.
        choice = get_menu_choice()

        # Process the choice.
        if choice == LOOK_UP:
            look_up(mycustomers)
        elif choice == ADD:
            add(mycustomers)
        elif choice == CHANGE:
            change(mycustomers)
        elif choice == DELETE:
            delete(mycustomers)

    # Save the mycontacts dictionary to a file.
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
        input_file = open(FILEDEPARTMENT, 'dp')
            
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
        input_file = open(FILEPRODUCT, 'qr')
            
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
        input_file = open(FILETRANSACTION, 'ti')
            
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
    choice = int(input('Enter your choice: '))
    
    # Validate the choice.
    while choice < LOOK_UP or choice > QUIT:
        choice = int(input('Enter a valid choice: '))

    # return the user's choice.
    return choice

   # The look_up function looks up an item in the
   # specified dictionary.
def look_up(mycustomers):
    # Get a name to look up.
    name = input('Enter a name: ')

    # Look it up in the dictionary.
    print(mycustomers.get(name, 'That name is not found.'))

# The add function adds a new entry into the
# specified dictionary.
def add(mycustomers):
    # Get the customers info.
    name = input('Name: ')
    street = input('Street: ')
    city = input('City: ')
    zip_code = input('Zip Code: ')
    
    # Create a Customer object named entry.
    entry = Customer.customer(name, street, city, zip_code)

    # If the name does not exist in the dictionary,
    # add it as a key with the entry object as the
    # associated value.
    if name not in mycustomers:
        mycustomers[name] = entry
        print('The entry has been added.')
    else:
        print('That name already exists.')
        
# The change function changes an existing
# entry in the specified dictionary.
def change(mycustomers):
    # Get a name to look up.
    name = input('Enter a name: ')

    if name in mycustomers:
        # Get a new street.
        street = input('Enter the new phone number: ')

        # Get a new city.
        city = input('Enter the new email address: ')
            
        #Get a new zip code
        zip_code = input('Enter the new zip code: ')

        # Create a contact object named entry.
        entry = Customer.customer(name, street, city, zip_code)

        # Update the entry.
        mycustomers[name] = entry
        print('Information updated.')
    else:
        print('That name is not found.')

# The delete functions deletes an entry from the
# specified dictionary.
def delete(mycustomers):
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
    department_name = input('Enter a name: ')

    # If the name is found, delete the entry.
    if department_name in mydepartments:
        del mydepartments[department_name]
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
               
