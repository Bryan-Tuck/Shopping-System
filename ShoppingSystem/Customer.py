# -*- coding: utf-8 -*-
"""
Created on Thu May  6 16:40:08 2021

@author: Bryan
"""
# import pickle

class Customer:
    
    #Constructor
    def __init__(self, name, street, city, zip_code):
        self.__name = name       
        self.__street = street
        self.__city = city
        self.__zip_code = zip_code
        
        
        
        
    ##Setters and Getters Begin    
    def set_name(self, name):
        self.__name = name        
        
    def set_street(self, street):
        self.__street = street
        
    def set_city(self, city):
        self.__city = city
    
    def set_zip_code(self, zip_code):
        self.__zip_code = zip_code
        
    def get_name(self):
        return self.__name     
        
    def get_street(self):
        return self.__street 
        
    def get_city(self):
        return self.__city 
    
    def get_zip_code(self):
        return self.__zip_code     
    ##Setters and Getters End   

    ##__str__ method returns object's state as a string
    def __str__(self):        
        return "Name: " + self.__name + \
               "\nStreet: " + self.__street + \
               "\nCity: " + self.__city + \
               "\nZip Code: " + self.__zip_code
               
# class CustomerManagement(Customer):
    
    
#     def __init__(self, FILENAME, customer_dct, LOOK_UP, ADD, CHANGE, DELETE, QUIT, load_customers ):
#         self.FILENAME = "Contacts.dat"
#         self.__customer_dct = customer_dct
#         self.__LOOK_UP = LOOK_UP
#         self.__ADD = ADD
#         self.__CHANGE = CHANGE
#         self.__DELETE = DELETE
#         self.__QUIT = QUIT
#         self.mycustomers = load_customers()

    
#     def load_customers(self, FILENAME):
        
#         try:
#             # Open the Customers.dat file.
#             input_file = open(FILENAME, 'rb')
            
#             # Unpickle the dictionary.
#             customer_dct = pickle.load(input_file)
            
#             # Close the phone_inventory.dat file.
#             input_file.close()
#         except IOError:
#                 # Could not open the file, so create
#                 # an empty dictionary.
#                 customer_dct = {}
                
#                 # Return the dictionary.
#         return customer_dct

#     # The get_menu_choice function displays the menu
#     # and gets a validated choice from the user.
#     def get_menu_choice(self, LOOK_UP, ADD, CHANGE, DELETE, QUIT):
#         print()
#         print('Menu')
#         print('---------------------------')
#         print('1. Look up a customer')
#         print('2. Add a new customer')
#         print('3. Change an existing customer')
#         print('4. Delete a customer')
#         print('5. Quit the program')
#         print()

#         # Get the user's choice.
#         choice = int(input('Enter your choice: '))

#         # Validate the choice.
#         while choice < LOOK_UP or choice > QUIT:
#             choice = int(input('Enter a valid choice: '))

#         # return the user's choice.
#         return choice

#     # The look_up function looks up an item in the
#     # specified dictionary.
#     def look_up(mycustomers,name):
#         # Get a name to look up.
#         name = input('Enter a name: ')

#         # Look it up in the dictionary.
#         print(mycustomers.get(name, 'That name is not found.'))

#     # The add function adds a new entry into the
#     # specified dictionary.
#     def add(mycustomers):
#         # Get the customers info.
#         name = input('Name: ')
#         street = input('Street: ')
#         city = input('City: ')
#         zip_code = input('Zip Code: ')

#         # Create a Customer object named entry.
#         entry = Customer.Customer(name, street, city, zip_code)

#         # If the name does not exist in the dictionary,
#         # add it as a key with the entry object as the
#         # associated value.
#         if name not in mycustomers:
#             mycustomers[name] = entry
#             print('The entry has been added.')
#         else:
#             print('That name already exists.')

#     # The change function changes an existing
#     # entry in the specified dictionary.
#     def change(mycustomers):
#         # Get a name to look up.
#         name = input('Enter a name: ')

#         if name in mycustomers:
#             # Get a new street.
#             street = input('Enter the new phone number: ')

#             # Get a new city.
#             city = input('Enter the new email address: ')
            
#             #Get a new zip code
#             zip_code = input('Enter the new zip code: ')

#             # Create a contact object named entry.
#             entry = Customer.Customer(name, street, city, zip_code)

#             # Update the entry.
#             mycustomers[name] = entry
#             print('Information updated.')
#         else:
#             print('That name is not found.')

#     # The delete function deletes an entry from the
#     # specified dictionary.
#     def delete(mycustomers):
#         # Get a name to look up.
#         name = input('Enter a name: ')

#         # If the name is found, delete the entry.
#         if name in mycustomers:
#               del mycustomers[name]
#               print('Entry deleted.')
#         else:
#             print('That name is not found.')

#     # The save_customers funtion pickles the specified
#     # object and saves it to the contacts file.
#     def save_customers(mycustomers, FILENAME):
#         # Open the file for writing.
#         output_file = open(FILENAME, 'wb')

#         # Pickle the dictionary and save it.
#         pickle.dump(mycustomers, output_file)

#         # Close the file.
#         output_file.close()    

               
               
               

                
    





