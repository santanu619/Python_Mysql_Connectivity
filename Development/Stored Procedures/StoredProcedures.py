'''
@Author: Santanu Mohapatra
@Date: 27/06/2021
@Last Modified by: Santanu Mohapatra
@Last Modified Time: 10:10 AM
@Title: Python program to perform stored procedures in student class.
'''

import mysql.connector
from decouple import config
import logging

class Student:
    
    def __init__(self):
        self.__localhost = config('HOST')
        self.__username = config('USER')
        self.__password = config('PASSWD')
        self.__database_name = config('DATABASE_NAME')
        self.__table_name = config('DATAASE_TABLE')
        self.createConnection()

    def createConnection(self):
        '''
        Description: To Create Connection to the SQL Server
        Parameter: None
        Return: None
        '''
        try:
            db = mysql.connector.connect(host = self.__localhost, user = self.__username,
                passwd = self.__password, database = self.__database_name, table = self.__table_name)
            
            if (db):
                logging.info("Connection Successful!")
                
            self.__db = db
        except:
            logging.error("Connection Unsuccessful!")
            

    def insert(self):
        '''
        Description: To insert records
        Parameter: None
        Return: None
        '''
        try:
            name = input("Enter Student Name: ")
            marks = float(input("Enter Student Marks: "))

            logging.info("Entered: {}, {}".format(name, marks))
            
            cursor = self.__db.cursor()
            cursor.execute("INSERT INTO "+self.__table_name+" (name, marks) VALUES (%s,%s)", (name, marks))

            id = cursor.lastrowid

            cursor.execute("INSERT INTO student_details (name, marks)" +
                " VALUE ({},{},{})".format(id, name, marks))

            self.__db.commit()
            logging.info("{} record inserted".format(cursor.rowcount))

        except:
            logging.error("Insert aborted")
            

    def retrieve(self):
        '''
        Description: To retrieve records
        Parameter: None
        Return: None
        '''
        try:
            cursor = self.__db.cursor()
            cursor.execute("SELECT * FROM "+self.__table_name)

            result = cursor.fetchall()

            for index in result:
                logging.info(index)
        except:
            logging.error("Retrieve aborted")

    def update(self):
        '''
        Description: To Update Records
        Parameter: None
        Return: None
        '''
        try:
            id = int(input("Update by id: "))
            name = input("Enter Students Updated Name: ")
            marks = float(input("Enter Marks: "))

            logging.info("Entered: {}, {}, {}".format(id, name, marks))
            cursor = self.__db.cursor()

            cursor.execute("UPDATE "+self.__table_name+" SET name=%s, marks=%s WHERE id = %s", (name, marks, id))

            self.__db.commit()

            logging.info("{} record updated".format(cursor.rowcount))
        except:
            logging.error("Update aborted")        

    def delete(self):
        '''
        Description: To Delete Records
        Parameter: None
        Return: None
        '''
        try:
            id = int(input("Delete by id: "))

            logging.info("Entered: {}".format(id))
            cursor = self.__db.cursor()

            cursor.execute("DELETE FROM {} WHERE id = {}".format(self.__table_name, id))

            self.__db.commit()

            logging.info(cursor.rowcount, "record deleted")
        except:
            logging.error("Delete aborted")

    
    def drop_table(self):
        '''
        Description: To Drop a table
        Parameter: None
        Return: None
        '''
        try:
            cursor = self.__db.cursor()

            cursor.execute("SHOW TABLES")
            tables = cursor.fetchall()
            for index in tables:
                print(index)

            table_name = input("Enter table name to be deleted: ")

            logging.info("Table to be deleted: {}".format(table_name))

            cursor.execute("DROP TABLE "+table_name)

            self.__db.commit()
        except:
            logging.error("Drop table aborted")


    def create_table(self):
        '''
        Description: To Create a new table
        Parameter: None
        Return: None
        '''
        try:
            cursor = self.__db.cursor()

            cursor.execute("SHOW TABLES")
            tables = cursor.fetchall()
            for index in tables:
                print(index)

            table_name = input("Enter new table name: ")

            logging.info("Table to be created with id as a primary key: {}".format(table_name))

            cursor.execute("CREATE TABLE "+table_name+" (id INT unsigned NOT NULL AUTO_INCREMENT,PRIMARY  KEY (id))")

            self.__db.commit()
        except:
            logging.error("Create table aborted")

    def maximum_marks(self):
        '''
        Description: Function to find the maximum marks
        Parameter: None
        Return: None
        '''
        try:
            cursor = self.__db.cursor()
            cursor.execute("SELECT MAX(marks) FROM StudentDetails")
            tables = cursor.fetchall()
            for index in tables:
                print(index)
            logging.info(cursor.close())
        except Exception as ex:
            logging.error(ex)

    def minimum_marks(self):
        '''
        Description: Function to find the minimum marks
        Parameter: None
        Return: None
        '''
        try:
            cursor = self.__db.cursor()
            cursor.execute("SELECT MIN(marks) FROM StudentDetails")
            tables = cursor.fetchall()
            for index in tables:
                print(index)
            logging.info(cursor.close())
        except Exception as ex:
            logging.error(ex)

    def get_student(self):
        try: 
            cursor = self.connect._Student__db.cursor()

            cursor.callproc('get_qualified_students')

            for result in cursor.stored_results():
                for index in result.fetchall():
                    logging.info(index)

        except:
            logging.exception("Call Procedure Aborted")

    def maximum_marks_sp(self):
        try: 
            cursor = self.connect._Student__db.cursor()

            result = cursor.callproc('display_maximum_mark',[1])

            logging.info(result[0])

        except:
            logging.exception("Call Procedure Aborted")

    def display_marks(self):
        try: 
            cursor = self.connect._Student__db.cursor()

            result = cursor.callproc('display_marks',[3])

            logging.info(result[0])

        except:
            logging.exception("Call Procedure Aborted")