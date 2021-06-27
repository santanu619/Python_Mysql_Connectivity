'''
@Author: Santanu Mohapatra
@Date: 27/06/2021
@Last Modified by: Santanu Mohapatra
@Last Modified Time: 12:40 PM
@Title: Python program to perform Import-Export
'''

from StudentDetails import Student
from decouple import config
import logging
import pandas as pd

class ImportExport():
    
    def __init__(self):
        self.connect = Student()

    def import_csv(self):
        '''
        Descriptions: This function is used to import from the csv file
        Parameter: None
        Return: None
        '''
        try:
            data = pd.read_csv('Students.csv')   
            df = pd.DataFrame(data, columns= ['Name','Marks'])
            logging.info("DataFrame: \n{}".format(df))

            cursor = self.connect._Student__db.cursor()

            
            
            for row in df.itertuples():
                cursor.execute("INSERT INTO student_details (Name, Marks)VALUES ('{}','{}')".format(row.Name,row.Marks))
            
            self.connect._Student__db.commit()

        except:
            logging.exception("Import Aborted")

    def export_csv(self):
        '''
        Descriptions: This function is used to export to the csv file
        Parameter: None
        Return: None
        '''
        try:            
            df = pd.read_sql('SELECT * FROM student_details', self.connect._Student__db)
            df.to_csv('Results.csv', index=False)

        except:
            logging.exception("Export Aborted")