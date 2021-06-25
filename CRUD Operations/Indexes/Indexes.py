'''
@Author: Santanu Mohapatra
@Date: 25/06/2021
@Last Modified by: Santanu Mohapatra
@Last Modified Time: 13:10 PM
@Title: Python program to perform indexing in student's database.
'''

from StudentDetails import *
import logging

def create_indexing():
    '''
    Description: To Create an Index in MySQL
    Parameter: None
    Return: None
    '''
    try:
        connect = Student() 
        cursor = connect._Student.__db.cursor()
        indexName = input("Enter index name: ")

        cursor.execute("CREATE INDEX {} ON StudentDetails(name, marks)".format(indexName))

        connect._Student.__db.commit()

        logging.info("Index Created: {}".format(indexName))
    except:
        logging.error("Creating Index Aborted")

def drop_indexing():
    '''
    Description: To Drop a Index in MySQL
    Parameter: None
    Return: None
    '''
    try:
        connect = Student() 
        cursor = connect._Student.__db.cursor()
        indexName = input("Enter index name: ")

        cursor.execute("DROP INDEX {} ON StudentDetails".format(indexName))

        connect._Student.__db.commit()

        logging.info("Index Dropped: {}".format(indexName))
    except:
        logging.error("Dropping Index Aborted")

def search_by_name():
    '''
    Description: To Search by name in MySQL
    Parameter: None
    Return: None
    '''
    try:
        connect = Student() 
        cursor = connect._Student.__db.cursor()

        name = input("Enter name of the student: ")

        cursor.execute("SELECT * FROM StudentDetails WHERE name = '{}'".format(name))

        result = cursor.fetchall()

        for index in result:
            logging.info(index)
    except:
        logging.error("Retrieve by data Aborted")