import MySQLCredentials as mc
import mysql.connector
from mysql.connector import Error


def ViewTableOnTerminal(tableName):
    try:
        connection = mysql.connector.connect(
            user=mc.user,
            password=mc.password,
            host=mc.host,
            database=mc.database,
            auth_plugin=mc.auth_plugin
        )
        sql_select_statement = "SELECT * FROM {}".format(tableName)
        cursor = connection.cursor()
        cursor.execute(sql_select_statement)
        records = cursor.fetchall()
        # print("Total number of rows in Laptop is: ", cursor.rowcount)

        print("\nPrinting each record\n")
        for row in records:
            print("Date : ", row[0])
            print("Status : ", row[1])
            print("Tahsinur  : ", row[2])
            print("Niger  : ", row[3])
            print("Nishu  : ", row[4])
            print("Asifuzzaman  : ", row[5])
            print("Sanjoy  : ", row[6], "\n")

    except Error as e:
        print("Error reading data from MySQL table", e)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")
