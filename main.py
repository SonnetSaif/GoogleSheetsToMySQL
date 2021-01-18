# importing libraries
import webbrowser
import gspread
import MySQLCredentials as mc
import mysql.connector
from mysql.connector import Error
from oauth2client.service_account import ServiceAccountCredentials

# importing python files as modules
import WriteToMySQLTable
import ViewTableOnTerminal
import ViewTableOnHTML

# initialize variables for gspread
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('GoogleSheetsToMySQL.json', scope)
client = gspread.authorize(creds)


# define method to pull data from spreadsheet
def GetSpreadsheetData(sheetName, worksheetIndex):
    sheet = client.open(sheetName).get_worksheet(worksheetIndex)
    return sheet.get_all_values()[1:]


# data_temp = []
# for i in range(20):
#   data_temp[i] = GetSpreadsheetData('Copy of sample__AttendanceLog__2016', i)

# vertical dataset
# data_march16_1 = GetSpreadsheetData('Copy of sample__AttendanceLog__2016', 0)
# data_april16_1  = GetSpreadsheetData('Copy of sample__AttendanceLog__2016', 1)
# data_may16_1  = GetSpreadsheetData('Copy of sample__AttendanceLog__2016', 2)
# data_june16_1  = GetSpreadsheetData('Copy of sample__AttendanceLog__2016', 3)
# data_july16_1  = GetSpreadsheetData('Copy of sample__AttendanceLog__2016', 4)
# data_august16_1  = GetSpreadsheetData('Copy of sample__AttendanceLog__2016', 5)
# data_september16_1  = GetSpreadsheetData('Copy of sample__AttendanceLog__2016', 6)
# data_october16_1  = GetSpreadsheetData('Copy of sample__AttendanceLog__2016', 7)
data_november16_1 = GetSpreadsheetData('Copy of sample__AttendanceLog__2016', 8)
# data_december16_1  = GetSpreadsheetData('Copy of sample__AttendanceLog__2016', 9)

# horizontal dataset
# data_march16_2  = GetSpreadsheetData('Copy of sample__AttendanceLog__2016', 10)
# data_april16_2  = GetSpreadsheetData('Copy of sample__AttendanceLog__2016', 11)
# data_may16_2  = GetSpreadsheetData('Copy of sample__AttendanceLog__2016', 12)
# data_june16_2  = GetSpreadsheetData('Copy of sample__AttendanceLog__2016', 13)
# data_july16_2  = GetSpreadsheetData('Copy of sample__AttendanceLog__2016', 14)
# data_august16_2  = GetSpreadsheetData('Copy of sample__AttendanceLog__2016', 15)
# data_september16_2  = GetSpreadsheetData('Copy of sample__AttendanceLog__2016', 16)
# data_october16_2  = GetSpreadsheetData('Copy of sample__AttendanceLog__2016', 17)
# data_november16_2  = GetSpreadsheetData('Copy of sample__AttendanceLog__2016', 18)
# data_december16_2  = GetSpreadsheetData('Copy of sample__AttendanceLog__2016', 19)

# print(data_march16_1[7])
# print(len(data_march16_1))

# def WriteToMySQLTable(sql_data, tableName):
#     try:
#         connection = mysql.connector.connect(
#             user=mc.user,
#             password=mc.password,
#             host=mc.host,
#             database=mc.database,
#             auth_plugin=mc.auth_plugin
#         )
#
#         sql_drop = " DROP TABLE IF EXISTS {} ".format(tableName)
#
#         sql_create_table = """CREATE TABLE {}(
#             DayDate VARCHAR(30),
#             STATUS VARCHAR(11),
#             Tahsinur VARCHAR(20),
#             Niger VARCHAR(20),
#             Nishu VARCHAR(20),
#             Asifuzzaman VARCHAR(20),
#             Sanjoy VARCHAR(20)
#             )""".format(tableName)
#
#         sql_insert_statement = """INSERT INTO {}(
#             DayDate,
#             STATUS,
#             Tahsinur,
#             Niger,
#             Nishu,
#             Asifuzzaman,
#             Sanjoy )
#             VALUES ( %s,%s,%s,%s,%s,%s,%s )""".format(tableName)
#
#         cursor = connection.cursor()
#         cursor.execute(sql_drop)
#         print('Table {} has been dropped'.format(tableName))
#         cursor.execute(sql_create_table)
#         print('Table {} has been created'.format(tableName))
#
#         for i in sql_data:
#             cursor.execute(sql_insert_statement, i)
#
#         connection.commit()
#         print("Table {} successfully updated.".format(tableName))
#
#     except mysql.connector.Error as error:
#         connection.rollback()
#         print("Error: {}. Table {} not updated!".format(error, tableName))
#
#     finally:
#         cursor.execute('SELECT COUNT(*) FROM {}'.format(tableName))
#         rowCount = cursor.fetchone()[0]
#         print(tableName, 'row count:', rowCount)
#         if connection.is_connected():
#             cursor.close()
#             connection.close()
#             print("MySQL connection is closed.")

WriteToMySQLTable.WriteToMySQLTable(data_november16_1, 'MyData_november16_1')

# def ViewTableOnTerminal(tableName):
#     try:
#         connection = mysql.connector.connect(
#             user=mc.user,
#             password=mc.password,
#             host=mc.host,
#             database=mc.database,
#             auth_plugin=mc.auth_plugin
#         )
#         sql_select_Query = "SELECT * FROM {}".format(tableName)
#         cursor = connection.cursor()
#         cursor.execute(sql_select_Query)
#         records = cursor.fetchall()
#         # print("Total number of rows in Laptop is: ", cursor.rowcount)
#
#         print("\nPrinting each record\n")
#         for row in records:
#             print("Date : ", row[0])
#             print("Status : ", row[1])
#             print("Tahsinur  : ", row[2])
#             print("Niger  : ", row[3])
#             print("Nishu  : ", row[4])
#             print("Asifuzzaman  : ", row[5])
#             print("Sanjoy  : ", row[6], "\n")
#
#     except Error as e:
#         print("Error reading data from MySQL table", e)
#     finally:
#         if connection.is_connected():
#             cursor.close()
#             connection.close()
#             print("MySQL connection is closed")

ViewTableOnTerminal.ViewTableOnTerminal('MyData_november16_1')

# def ViewTableOnHTML(tableName):
#     connection = mysql.connector.connect(
#         user=mc.user,
#         password=mc.password,
#         host=mc.host,
#         database=mc.database,
#         auth_plugin=mc.auth_plugin
#     )
#
#     select_employee = """SELECT * FROM {}""".format(tableName)
#     cursor = connection.cursor()
#     cursor.execute(select_employee)
#     result = cursor.fetchall()
#
#     p = []
#
#     tbl = "<tr><td>ID</td><td>Name</td><td>Email</td><td>Phone</td></tr>"
#     p.append(tbl)
#
#     for row in result:
#         a = "%s" % row[0]
#         p.append(a)
#         b = "%s" % row[1]
#         p.append(b)
#         c = "%s" % row[2]
#         p.append(c)
#         d = "%s" % row[3]
#         p.append(d)
#         e = "%s" % row[4]
#         p.append(e)
#         f = "%s" % row[5]
#         p.append(f)
#         g = "%s" % row[6]
#         p.append(g)
#         h = "%s" % row[7]
#         p.append(h)
#
#     contents = '''<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
#     <html>
#     <head>
#     <meta
#     content="text/html; charset=ISO-8859-1"
#     http-equiv="content-type">
#     <title>Python Webbrowser</title>
#     </head>
#     <body>
#     <table>
#     %s
#     </table>
#     </body>
#     </html>
#     ''' % p
#
#     filename = 'web-browser.html'
#
#     # def main(contents, filename):
#     output = open(filename, "w")
#     output.write(contents)
#     output.close()
#
#     # main(contents, filename)
#     webbrowser.open(filename)
#
#     if connection.is_connected():
#         cursor.close()
#         connection.close()
#         print("MySQL connection is closed.")

ViewTableOnHTML.ViewTableOnHTML('MyData_november16_1')
