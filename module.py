import psycopg2
from psycopg2 import Error

try:
    #connect to an existing database
    connection =psycopg2.connect(user="postgres",
                                 password="8790",
                                 host="127.0.0.1",
                                 port="5432",
                                 database="onlinefinance")
    
    #create a cursor to perform database operations
    cursor = connection.cursor()
    insert_query = """ INSERT INTO signup (email, password, confirmpassword,id_number) VALUES ('VERO@interweb.co.ke', 'vero003','vero003',003 )"""
    
    cursor.execute(insert_query)
    connection.commit()
    print("1 Record inserted successfully")
    
except (Exception, Error) as error:
    print("Error while connecting to PostgreSQL", error)
finally:
    if connection:
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")
     