import mysql.connector
from mysql.connector import Error
import pandas as pd
from datetime import datetime as dt

def create_db_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host = host_name,
            user = user_name,
            passwd = user_password,
            database = db_name
        )
        print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")

    return connection

connection = create_db_connection("localhost", "root", "sqledu", "discbot")

def sql_command(connection, query): #(binary, str) -> str
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
    except Error as err:
        print(f"Error: '{err}'")


#Relevant tables

user_info_table = """

CREATE TABLE user_info (
    username VARCHAR(40) PRIMARY KEY, 
    first_name VARCHAR(40) NOT NULL, 
    last_name VARCHAR(40), 
    course_1 VARCHAR(6),
    course_2 VARCHAR(6),
    course_3 VARCHAR(6),
    course_4 VARCHAR(6),
    course_5 VARCHAR(6),
    course_6 VARCHAR(6),
    );
    
"""

master_schedule = """

CREATE TABLE master_schedule ( 
    hour_num VARCHAR(3), 
    hour DATETIME, 
    day VARCHAR(9), 
    room VARCHAR(7), 
    class_type VARCHAR(3) 
);
    
"""

#HOW THE FUCK DO I DO THIS AHHHHHH

master_schedule_change_foreign_key_addition1 = """

ALTER TABLE master_schedule (
    
);
"""

user_courses = """

CREATE TABLE user_courses (
    username VARCHAR(40) PRIMARY KEY, 
    course_name VARCHAR(6)
    );
    
"""

update_master_schedule = """

    ALTER TABLE master_schedule
    ADD FOREIGN KEY ()
    REFERENCES 

"""

sql_command(connection, user_info_table)
sql_command(connection, master_schedule)

