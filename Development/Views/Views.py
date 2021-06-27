'''
@Author: Santanu Mohapatra
@Date: 25/06/2021
@Last Modified by: Santanu Mohapatra
@Last Modified Time: 17:45 PM
@Title: Python program to perform views in student's database.
'''

from StudentDetails import *
import logging

class View:

    def create_view():
        '''
        Description: Create a view in MySQL
        Parameter: None
        Return: None
        '''
        try:
            connect = Student() 
            cursor = connect._Student__db.cursor()
            viewName = input("Enter view name: ")

            cursor.execute("CREATE VIEW {} AS SELECT * FROM StudentDetails".format(viewName))
        
            connect._Student__db.commit()

            logging.info("View Created: {}".format(viewName))
        except:
            logging.error("Creating View Aborted")

    def show_view():
        '''
        Description: Show View
        Parameter: None
        Return: None
        '''
        try:
            connect = Student() 
            cursor = connect._Student__db.cursor()
            viewName = input("Enter view name: ")

            cursor.execute("SELECT * FROM {}".format(viewName))
        
            result = cursor.fetchall()

            for index in result:
                logging.info(index)
        except:
            logging.error("Show View Aborted")

    def drop_view():
        '''
        Description: Drop View
        Parameter: None
        Return: None
        '''
        try:
            connect = Student() 
            cursor = connect._Student__db.cursor()
            viewName = input("Enter view name: ")

            cursor.execute("DROP VIEW {}".format(viewName))
        
            connect._Student__db.commit()

            logging.info("View Dropped: {}".format(viewName))
        except:
            logging.error("Dropping View Aborted")

    def alter_view():
        '''
        Description: Alter View
        Parameter: None
        Return: None
        '''
        try:
            connect = Student() 
            cursor = connect._Student__db.cursor()
            viewName = input("Enter view name: ")

            cursor.execute("CREATE OR REPLACE VIEW {} AS SELECT name, marks FROM StudentDetails".format(viewName))
        
            connect._Student__db.commit()

            logging.info("View Altered: {}".format(viewName))
        except:
            logging.error("Altering View Aborted")