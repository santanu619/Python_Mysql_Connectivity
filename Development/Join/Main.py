'''
@Author: Santanu Mohapatra
@Date: 26/06/2021
@Last Modified by: Santanu Mohapatra
@Last Modified Time: 14:10 PM
@Title: Python program to call join class.
'''

from Join.Joins import Join
import logging

def Main():
    '''
    Description: Performs features on types of JOINS in MySQL
    Parameter: None
    Return: None
    '''
    join = Join()
    try:
        logging.info("Program start")
        user_input = ""

        while user_input != 'q':
            print("1 - Inner Join")
            print("2 - Left Outer Join")
            print("3 - Right Outer Join")
            print("4 - Cross Join")
            print("5 - Self Join")
            print("q - Quit")
            user_input = input("Select Option: ")

            if (user_input == "1"):
                logging.info("Choosen Inner Join")
                join.inner_join()

            elif (user_input == "2"):
                logging.info("Choosen Left Outer Join")
                join.outer_left_join()
            
            elif (user_input == "3"):
                logging.info("Choosen Right Outer Join")
                join.right_outer_join()

            elif (user_input == "4"):
                logging.info("Choosen Cross Join")
                join.cross_join()

            elif (user_input == "5"):
                logging.info("Choosen Self Join")
                join.self_join()

            elif user_input == "q":
                logging.info("Choosen to quit")
                break

            else:
                print("Please Select Proper Option")

    except:
        raise Exception("Unexpected Error Occured")

Main()