'''
@Author: Santanu Mohapatra
@Date: 26/06/2021
@Last Modified by: Santanu Mohapatra
@Last Modified Time: 18:10 PM
@Title: Python program to call the student function class.
'''

from StoredProcedures import *
import logging

def Main():
    '''
    Description: Performs functions on Students Tables
    Parameter: None
    Return: None
    '''
    try:
        logging.info("Welcome to Student Database Management System")
        user_input = ""

        while user_input != 'q':
            print("Default table is considered. i.e. Students table")
            print("1 - Create Table")
            print("2 - Drop Table")
            print("3 - Insert record to StudentDetails")
            print("4 - Retrieve records from StudentDetails")
            print("5 - Update record from StudentDetails")
            print("6 - Delete record from StudentDetails")
            print("7 - Find maximum marks from StudentDetails")
            print("8 - Find minimum marks from StudentDetails")
            print("9 - Get Students using stored procedures")
            print("10 - Find maximum marks using stored procedures")
            print("11 - Display marks using stored procedures")
            print("q - Quit")
            user_input = input("Select Option: ")

            connect = Student()

            if (user_input == "1"):
                logging.info("Choosen to create a new table")
                connect.create_table()

            elif (user_input == "2"):
                logging.info("Choosen to drop the table")
                connect.drop_table()


            elif (user_input == "3"):
                logging.info("Choosen to insert record into table")
                connect.insert()

            elif (user_input == "4"):
                logging.info("Choosen to retrieve records from table")
                connect.retrieve()

            elif (user_input == "5"):
                logging.info("Choosen to update record from table")
                connect.update()

            elif (user_input == "6"):
                logging.info("Choosen to delete record from table")
                connect.retrieve()
                connect.delete()

            elif (user_input == "7"):
                logging.info("Choosen to find maximum marks from table")
                connect.maximum_marks()

            elif (user_input == "8"):
                logging.info("Choosen to find minimum marks from table")
                connect.minimum_marks()

            elif (user_input == "9"):
                logging.info("Choosen to get students using stored procedure")
                connect.get_student()

            elif (user_input == "10"):
                logging.info("Choosen to find maximum marks using stored procedure")
                connect.maximum_marks_sp()

            elif (user_input == "11"):
                logging.info("Choosen to display marks using stored procedure")
                connect.display_marks()

            elif user_input == "q":
                logging.info("Choosen to quit")
                break

            else:
                logging.info("Please Select Proper Option")

    except:
        raise Exception("Unexpected Error Occured!")

Main()
