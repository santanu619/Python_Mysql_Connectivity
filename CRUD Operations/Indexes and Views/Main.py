'''
@Author: Santanu Mohapatra
@Date: 25/06/2021
@Last Modified by: Santanu Mohapatra
@Last Modified Time: 13:50 PM
@Title: Python program to call the indexes class in the main function.
'''

from Indexes import *
import logging

def Main():
    indexes = Indexes()
    '''
    Description: Performs features on indexing in MySQL student's database
    Parameter: None
    Return: None
    '''
    try:
        logging.info("Program start")
        user_input = ""

        while user_input != 'q':
            print("1 - Create Indexing")
            print("2 - Drop Indexing")
            print("3 - Search By Name")
            print("q - Quit")
            user_input = input("Select Option: ")

            if (user_input == "1"):
                logging.info("Choosen to create index")
                indexes.create_indexing()

            elif (user_input == "2"):
                logging.info("Choosen to drop index")
                indexes.drop_indexing()
            
            elif (user_input == "3"):
                logging.info("Choosen to Search By Name")
                indexes.search_by_name()

            elif user_input == "q":
                logging.info("Quit from the Database")
                break

            else:
                print("Please Select Proper Option")

    except:
        raise Exception("Unexpected Error Occured")

Main()