'''
@Author: Santanu Mohapatra
@Date: 26/06/2021
@Last Modified by: Santanu Mohapatra
@Last Modified Time: 13:10 PM
@Title: Python program to perform joins in student's database.
'''

from StudentDetails import *
import logging

class Join:

    def inner_join():
        '''
        Description: Inner Join
        Parameter: None
        Return: None
        '''
        try:
            connect = Student() 
            cursor = connect._Student__db.cursor()

            cursor.execute("SELECT * FROM StudentDetails ed INNER JOIN MarkDetails md ON sd.id = md.student_id")
        
            result = cursor.fetchall()

            for index in result:
                logging.info(index)

        except:
            logging.error("INNER JOIN Aborted")

    def outer_left_join():
        '''
        Description: Outer Left Join
        Parameter: None
        Return: None
        '''
        try:
            connect = Student() 
            cursor = connect._Student__db.cursor()

            cursor.execute("SELECT * FROM StudentDetails sd LEFT OUTER JOIN MarkDetails md ON sd.id = md.student_id")
        
            result = cursor.fetchall()

            for index in result:
                logging.info(index)

        except:
            logging.error("LEFT OUTER JOIN Aborted")

    def right_outer_join():
        '''
        Description: Outer Right Join
        Parameter: None
        Return: None
        '''
        try:
            connect = Student() 
            cursor = connect._Student__db.cursor()

            cursor.execute("SELECT * FROM StudentDetails sd RIGHT OUTER JOIN MarkDetails md ON sd.id = md.student_id")
        
            result = cursor.fetchall()

            for index in result:
                logging.info(index)

        except:
            logging.error("RIGHT OUTER JOIN Aborted")

    def cross_join():
        '''
        Description: Cross Join
        Parameter: None
        Return: None
        '''
        try:
            connect = Student() 
            cursor = connect._Student__db.cursor()

            cursor.execute("SELECT * FROM StudentDetails sd CROSS JOIN MarkDetails md")
        
            result = cursor.fetchall()

            for index in result:
                logging.info(index)

        except:
            logging.error("CROSS JOIN Aborted")

    def self_join():
        '''
        Description: Self Join
        Parameter: None
        Return: None
        '''
        try:
            connect = Student() 
            cursor = connect._Student__db.cursor()

            cursor.execute("SELECT * FROM StudentDetails sd1, StudentDetails sd2 WHERE sd1.marks = sd2.marks AND sd2.marks <90")
        
            result = cursor.fetchall()

            for index in result:
                logging.info(index)

        except:
            logging.error("SELF JOIN Aborted")