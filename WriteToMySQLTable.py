import MySQLCredentials as mc
import mysql.connector
from mysql.connector import Error


def WriteToMySQLTable(sql_data, tableName):
    try:
        connection = mysql.connector.connect(
            user=mc.user,
            password=mc.password,
            host=mc.host,
            database=mc.database,
            auth_plugin=mc.auth_plugin
        )

        sql_drop = " DROP TABLE IF EXISTS {} ".format(tableName)

        sql_create_table = """CREATE TABLE {}(
            DayDate VARCHAR(30),
            STATUS VARCHAR(11),
            Tahsinur VARCHAR(20),
            Niger VARCHAR(20),
            Nishu VARCHAR(20),
            Asifuzzaman VARCHAR(20),
            Sanjoy VARCHAR(20)
            )""".format(tableName)

        sql_insert_statement = """INSERT INTO {}(
            DayDate,
            STATUS,
            Tahsinur,
            Niger,
            Nishu,
            Asifuzzaman,
            Sanjoy )
            VALUES ( %s,%s,%s,%s,%s,%s,%s )""".format(tableName)

        cursor = connection.cursor()
        cursor.execute(sql_drop)
        print('Table {} has been dropped'.format(tableName))
        cursor.execute(sql_create_table)
        print('Table {} has been created'.format(tableName))

        for i in sql_data:
            cursor.execute(sql_insert_statement, i)

        connection.commit()
        print("Table {} successfully updated.".format(tableName))

    except mysql.connector.Error as error:
        connection.rollback()
        print("Error: {}. Table {} not updated!".format(error, tableName))

    finally:
        cursor.execute('SELECT COUNT(*) FROM {}'.format(tableName))
        rowCount = cursor.fetchone()[0]
        print(tableName, 'row count:', rowCount)
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed.")
