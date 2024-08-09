import mysql.connector

def db_connect():
    conn=mysql.connector.connect(
    host="localhost",      # This is to create a connection object and this method returns a connection object
    user="root",   
    password="root",  
    database="Library"
    )
    return conn

class LibManagement:
    def __init__(self,db_connect): # As soon as the object for the class is created the db_connect returns a connection object  
            self.conn_object=db_connect # we store that object in an instance variable
            self.cursor=db_connect.cursor()
    
    def add_book(ISBN,name,title,year,count):
         pass 