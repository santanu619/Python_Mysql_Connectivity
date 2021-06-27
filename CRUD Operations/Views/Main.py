'''
@Author: Santanu Mohapatra
@Date: 25/06/2021
@Last Modified by: Santanu Mohapatra
@Last Modified Time: 18:50 PM
@Title: Python program to call the views class in the main function.
'''

from Views.Views import View
import logging

def Main():
    views = View()
    '''
    Description: Performs features on views in MySQL student's database
    Parameter: None
    Return: None
    '''
    try:
        logging.info("Program start")
        user_input = ""

        while user_input != 'q':
            print("1 - Create View")
            print("2 - Show View")
            print("3 - Drop View")
            print("4 - Alter View")
            print("q - Quit")
            user_input = input("Select Option: ")

            if (user_input == "1"):
                logging.info("Choosen to create view")
                views.create_view()

            elif (user_input == "2"):
                logging.info("Choosen to show view")
                views.show_view()
            
            elif (user_input == "3"):
                logging.info("Choosen to drop view")
                views.drop_view()

            elif (user_input == "4"):
                logging.info("Choosen to alter view")
                views.alter_view()
                
            elif user_input == "q":
                logging.info("Quit from the Database")
                break

            else:
                print("Please Select Proper Option")

    except:
        raise Exception("Unexpected Error Occured")

Main()