'''
@Author: Santanu Mohapatra
@Date: 27/06/2021
@Last Modified by: Santanu Mohapatra
@Last Modified Time: 13:40 PM
@Title: Python program to call main function to perform Import-Export
'''

from ImportExport import ImportExport 
import logging

def Main():
    
    try:
        logging.info("Program start")
        user_input = ""

        while user_input != 'q':
            print("1 - Import CSV")
            print("2 - Export CSV")
            print("q - Quit")
            user_input = input("Select Option: ")

            importexport = ImportExport()

            if (user_input == "1"):
                logging.info("Choosen to import poeple.csv file")
                importexport.import_csv()

            elif (user_input == "2"):
                logging.info("Choosen to export to output.csv file")
                importexport.export_csv()

            elif user_input == "q":
                logging.info("Choosen to quit")
                break

            else:
                print("Please Select Proper Option")

    except:
        raise Exception("Program Stopped")

Main()