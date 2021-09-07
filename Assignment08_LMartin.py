# ------------------------------------------------------------------------ #
# Title: Assignment 08
# Description: Working with classes

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 8
# LMartin, 8.28.2021, Modified code for class and process data from file, added pseudocode for tasks - TODO 1-2
# LMartin, 8.29.2021, Modified code to process data to a file - TODO 3
# LMartin, 8.31.2021, Modified code by starting Presentation code - TODO 4-8
# LMartin, 9.1.2021, Modified code by finishing Presentation code - TODO 4-8
# LMartin, 9.3.2021, Modified code by completing Main Body code - TODO 9
# LMartin, 9.4.2021, Modified code by finishing Main Body code - TODO 9
# LMartin, 9.5.2021, Tested script and fixed errors with script - TODO 1-9
# ------------------------------------------------------------------------ #

import os

# ------------------------------------------------------------------------- #
# Data -------------------------------------------------------------------- #
# ------------------------------------------------------------------------- #

strFileName = 'products.txt'
lstOfProductObjects = []

class Product:
    """Stores data about a product:

    properties:
        product_name: (string) with the products's  name
        product_price: (float) with the products's standard price
    methods:
    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        LMartin, 8.28.2021, Modified Class code
    """
    pass
    # TODO: Add Code to the Product class - 1 DONE

# -- Fields --
    # Already defined above.

# -- Constructors --
    def __init__(self, product_name = "", product_price = ""):
        # -- Attributes --
        self.__product_name = product_name
        self.__product_price = product_price

# -- Properties --
    # Product Name
    @property
    def product_name(self):
        return str(self.__product_name).title()

    @product_name.setter
    def product_name(self, value: str):
        if value.isnumeric():
            raise Exception ("ERROR - Product Name must not contain numbers. Try again.")
        else:
            self.__product_name = value

    # Product Price
    @property
    def product_price(self):
        return float(self.__product_price)

    @product_price.setter
    def product_price(self, value: float):
        try:
            self.__product_price = float(value)
        except ValueError:
            raise Exception("ERROR - Product Price must contain numbers. Try again.")

# -- Methods --
    def __str__(self):
        return self.product_name + "," + str(self.product_price)

# ------------------------------------------------------------------------- #
# Processing  ------------------------------------------------------------- #
# ------------------------------------------------------------------------- #

class FileProcessor:
    """Processes data to and from a file and a list of product objects:

    methods:
        save_data_to_file(file_name, list_of_product_objects):

        read_data_from_file(file_name): -> (a list of product objects)

    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        LMartin, 8.28.2021, Modified code to process data from a file.
        LMartin, 8.29.2021, Modified code to process data to a file.
    """
    pass
    # TODO: Add Code to process data from a file - 2 DONE

# Read Data From File
    @staticmethod
    def read_data_from_file(file_name):
        """ Reads data from text file and places it into dictionary rows.

        :param file_name: (string) of file name.
        :return: (list) of dictionary rows with product information.
        """
        list_of_product_objects = []
        try:
            if os.path.exists(file_name):
                objFile = open(file_name, "r")
                for line in objFile:
                    data = line.split(",")
                    row = Product(data[0], data [1])
                    list_of_product_objects.append(row)
                objFile.close()
        except FileNotFoundError as e:
            print("ERROR - Cannot locate file.")
            input("Press ENTER key to return to the main menu.")
        else:
            print("Data successfully loaded.")
        return list_of_product_objects

    # TODO: Add Code to process data to a file - 3 DONE
# Save Data To File
    @staticmethod
    def save_data_to_file(file_name, list_of_product_objects):
        """ Saves data to text file.

        :param file_name: (string) of file name.
        :param list_of_product_objects: (list) of product data inputted.
        :return: (list) of dictionary rows with product information.
        """
        try:
            objFile = open(file_name, "w")
            for product in list_of_product_objects:
                objFile.write(product.__str__() + "\n")
            objFile.close()
        except Exception as e:
            print("ERROR - Data was not saved to file correctly.")

# ------------------------------------------------------------------------- #
# Presentation (Input/Output)  -------------------------------------------- #
# ------------------------------------------------------------------------- #

class IO:
    # TODO: Add docstring - 4 DONE
    """ Performs Input and Output tasks for script."""

    pass
    # TODO: Add code to show menu to user - 5 DONE
    @staticmethod
    def print_menu_list():
        """ Displays Choice Menu to user."""
        print('''
        ~~~ Products Menu Options ~~~
        1) Display Current Products
        2) Add New Product
        3) Save Data to File
        4) Exit Program
        ''')

    # TODO: Add code to get user's choice - 6 DONE
    @staticmethod
    def input_menu_choice():
        """ Obtains user's menu selection.

        :return: (string) of menu input value.
        """
        menu_choice = str(input("Which option would you like to do? [1-4] - "))
        return menu_choice

    # TODO: Add code to show the current data from the file to user - 7 DONE
    @staticmethod
    def display_current_products(list_of_rows):
        """ Shows user the current products.

        :param list_of_rows: (list) of rows displayed.
        :return: N/A
        """
        print("~~~ Current Products ~~~")
        for row in list_of_rows:
            print(row.product_name + "," + str(row.product_price))

    @staticmethod
    def input_press_to_continue(optional_message=""):
        """ Have user press enter to get the script to continue.

        :param optional_message: (string) An optional message displayed.
        :return: N/A
        """
        print(optional_message)
        input("Press [Enter] to continue.")

    # TODO: Add code to get product data from user - 8 DONE
    @staticmethod
    def add_new_products():
        """ Adds new products and prices to the list.

        :return: (list) of product information.
        """

        try:
            prod_name = str(input("Enter a new product name [using letters only] : ")).strip()
            prod_price = float(input("Enter the project price [using numbers only]: ").strip())
            prod_1 = Product(product_name=prod_name, product_price=prod_price)
            return prod_1
        except Exception as e:
            print(e)
        return prod_1

# ------------------------------------------------------------------------- #
# Main Body of Script  ---------------------------------------------------- #
# ------------------------------------------------------------------------- #

# TODO: Add Data Code to the Main body - 9 DONE
    # Load data from file into a list of product objects when script starts
    # Show user a menu of options
    # Get user's menu option choice
    # Show user current data in the list of product objects
    # Let user add data to the list of product objects
    # let user save current data to file and exit program

lstofProductObjects = FileProcessor.read_data_from_file(strFileName)
print("Opening database...")
# IO.print_menu_list()

try:
    while (True):
        IO.print_menu_list()
        strChoice = IO.input_menu_choice()

        if strChoice.strip() == "1":
            IO.display_current_products(lstofProductObjects)
            IO.input_press_to_continue()

        elif strChoice.strip() == "2":
            lstofProductObjects.append(IO.add_new_products())
            continue

        elif strChoice.strip() == "3":
            FileProcessor.save_data_to_file(strFileName, lstofProductObjects)
            print("SUCCESS - Data was saved to text file.")
            IO.input_press_to_continue()
            continue

        elif strChoice.strip() == "4":
            print("Exiting Program.")
            break

        else:
            print("Please select options 1-4 only.")

except Exception as e:
    print("ERROR - Program did not run correctly.")
    print(e)