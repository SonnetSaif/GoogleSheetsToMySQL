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

        # print("\tDate\t\t\tStatus\tTahsinur\tNiger\tNishu\tAsifuzzaman\tSanjoy")
        print("\n")
        for row in records:
            print(row[0] + " " + row[1] + "\t" + row[2] + "\t" + row[3] + "\t" + row[4] + "\t" + row[5] + "\t" + row[
                6])
            print("\n")

    except Error as e:
        print("Error reading data from MySQL table", e)

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")
