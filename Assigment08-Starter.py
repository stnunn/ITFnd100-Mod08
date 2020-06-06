# ------------------------------------------------------------------------ #
# Title: Assignment 08
# Description: Working with classes

# ChangeLog (Who,When,What):
# RRoot,1.1.2020,Created started script
# RRoot,1.1.2020,Added pseudo-code to start assignment 8
# SNunn,6.5.2020,Modified code to complete assignment 8
# ------------------------------------------------------------------------ #

# Import modules --------------------------------------------------------- #
import sys

# Data -------------------------------------------------------------------- #
STR_FILE_NAME = 'C:\\_PythonClass\\Assignment08\\products.txt'
lstOfProductObjects = []

class Product:
    """Stores data about a product:

    properties:
        product_name: (string) with the products's  name
        product_price: (float) with the products's standard price
    methods:
        # just the standard methods
    changelog: (When,Who,What)
        RRoot,1.1.2020,Created Class
        SNunn,6.5.2020,Modified code to complete assignment 8
    """
    # pass
    # TODO: Add Code to the Product class # DONE
    # --Fields --
    strProductName = ''
    fltProductPrice = 0.0
    strProductPrice = ''

    # --Constructor --
    def __init__(self, product_name = 'No Product', product_price = 0.0):
        # --Attributes--
        self.strProductName = product_name
        self.fltProductPrice = product_price
        self.strProductPrice = str(product_price)

    def __str__(self):
        return self.strProductName + ' | ' + self.strProductPrice

    # need __repr__ to display text of list, instead of memory address
    def __repr__(self):
        return self.__str__()

# Data -------------------------------------------------------------------- #

# Processing  ------------------------------------------------------------- #
class FileProcessor:
    """Processes data to and from a file and a list of product objects:

    methods:
        read_data_from_file(file_name): -> (a list of product objects)
        save_data_to_file(file_name, list_of_product_objects):
    changelog: (When,Who,What)
        RRoot,1.1.2020,Created Class
        SNunn,6.5.2020,Modified code to complete assignment 8
    """

    # TODO: Add Code to process data from a file # DONE
    n = ''
    p = 0.0

    @staticmethod
    def read_data_from_file(file_name):
        """  Read data from file.
        :return: list of objects
        """
        lstOfProductObjects.clear() # clear current data
        try:
            f = open(file_name, "r")
        except FileNotFoundError:
            input("*** " + file_name + " does not exist.  Please create it and rerun this program.  Press Enter key to exit.")
            sys.exit()
        except:
            input("*** Something is wrong with " + file_name + ". Please investigate and rerun this program.  Press Enter key to exit.")
            sys.exit()
        for line in f:
            n, p = line.split(',')
            npObj = Product(n.strip(), p.strip())
            lstOfProductObjects.append(npObj)
        f.close()
        return lstOfProductObjects

    # TODO: Add Code to process data to a file # DONE

    @staticmethod
    def save_data_to_file(file_name, list_of_product_objects):
        """  Saves data to file.
        :return: printed text
        """
        f = open(file_name, "w")
        for o in list_of_product_objects:
            f.write(str(o).replace(' | ', ',') + '\n')
        f.close()
        print('Data successfully saved to "' + STR_FILE_NAME + '".')

# Processing  ------------------------------------------------------------- #

# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    # TODO: Add docstring # DONE
    """Show Menu, Get User Choice, Show Data, Receive User Inputs:

        methods:
            show_menu(): -> (a string menu)
            user_choice(): -> (a string choice)
            reload_data(list_of_product_objects): -> (a list of objects)
            input_data(product_name, product_price): -> (an object)
            inwork_data(): -> (a printed list)
        changelog: (When,Who,What)
            SNunn,6.5.2020,Created Class to complete assignment 8
        """

    # TODO: Add code to show menu to user # DONE
    @staticmethod
    def show_menu():
        """  Display a menu of choices to the user.
        :return: nothing
        """
        print('''
        Menu of Options:
        1) Reload current Product and Price data from file
        2) Add new Product and Price data
        3) Save data to File
        4) Exit Program
        ''')
        print()  # Add an extra line for looks

    # TODO: Add code to get user's choice # DONE
    @staticmethod
    def user_choice():
        """ Gets the menu choice from a user
        :return: string
        """
        choice = str(input("Which option would you like to perform? [1 to 4] - ")).strip()
        print()  # Add an extra line for looks
        return choice

    # TODO: Add code to show the current data from the file to user # DONE
    @staticmethod
    def reload_data():
        """ Reload data from file
        :return: string
        """
        FileProcessor.read_data_from_file(STR_FILE_NAME)
        return 'Success'

    # TODO: Add code to get product data from user # DONE
    @staticmethod
    def input_data():
        """ Input Data
        :return: list
        """
        n = input('What is the product name? ')
        p = input('What is the product price? ')
        npObj = Product(n.strip(), p.strip())
        lstOfProductObjects.append(npObj)
        return lstOfProductObjects

    @staticmethod
    def in_work_data():
        """ Show in-work data
        :return: printed text
        """
        print('\n***** Product List *****')
        for o in lstOfProductObjects:
            print(o)
        print('************************')

    @staticmethod
    def input_yes_no_choice(message):
        """ Gets a yes or no choice from the user
        :return: string
        """
        return str(input(message)).strip().lower()

# Presentation (Input/Output)  -------------------------------------------- #

# Main Body of Script  ---------------------------------------------------- #
# TODO: Add Data Code to the Main body # DONE
# Load data from file into a list of product objects when script starts
FileProcessor.read_data_from_file(STR_FILE_NAME)

while True:
    # Show user current data in the list of product objects
    IO.in_work_data()
    # Show user a menu of options
    IO.show_menu()
    # Get user's menu option choice
    strChoice= IO.user_choice()
    if strChoice.strip() == '1': # Reload from file
        print('Warning: Unsaved Data Will Be Lost!')
        if IO.input_yes_no_choice('Are you sure you want to reload data from file? (y/n) -  ') == 'y':
            FileProcessor.read_data_from_file(STR_FILE_NAME)
            print('\n*** Data successfully reloaded from', STR_FILE_NAME, '***\n')
    # Let user add data to the list of product objects
    elif strChoice.strip() == '2': # Add new Product and Price data
        IO.input_data()
    # let user save current data to file and exit program
    elif strChoice.strip() == '3': # Save data to File
        FileProcessor.save_data_to_file(STR_FILE_NAME,lstOfProductObjects)
    elif strChoice == '4':  # Exit Program
        print("Goodbye!")
        break  # and Exit

# Main Body of Script  ---------------------------------------------------- #