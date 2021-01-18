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

# vertical datasets
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

# horizontal datasets
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

WriteToMySQLTable.WriteToMySQLTable(data_november16_1, 'MyData_november16_1')

ViewTableOnTerminal.ViewTableOnTerminal('MyData_november16_1')

ViewTableOnHTML.ViewTableOnHTML('MyData_november16_1')
