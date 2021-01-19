import webbrowser
import MySQLCredentials as mc
import mysql.connector
from mysql.connector import Error


def ViewTableOnHTML(tableName):
    connection = mysql.connector.connect(
        user=mc.user,
        password=mc.password,
        host=mc.host,
        database=mc.database,
        auth_plugin=mc.auth_plugin
    )

    select_employee = """SELECT * FROM {}""".format(tableName)
    cursor = connection.cursor()
    cursor.execute(select_employee)
    result = cursor.fetchall()

    temp = []

    # tbl = "<tr><td>NBR DC/DR Attendance Register</td></tr>" \
    #       "<tr><td>Date</td><td>Status</td><td>Tahsinur Refat Emon</td>" \
    #       "<td>Niger</td><td>Nishu</td><td>Asifuzzaman</td><td>Sanjoy</td></tr> "
    #
    # temp.append(tbl)

    for row in result:
        a = "<tr><td>%s</td>" % row[0]
        temp.append(a)
        b = "<td>%s</td>" % row[1]
        temp.append(b)
        c = "<td>%s</td>" % row[2]
        temp.append(c)
        d = "<td>%s</td>" % row[3]
        temp.append(d)
        e = "<td>%s</td>" % row[4]
        temp.append(e)
        f = "<td>%s</td>" % row[5]
        temp.append(f)
        g = "<td>%s</td>" % row[6]
        temp.append(g)
        print("\n")

    contents = """<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
    <html>
    <head>
    <meta content="text/html; charset=ISO-8859-1"
    http-equiv="content-type">
    <title>Python Webbrowser</title>
    </head>
    <body>
    <table>
    %s
    </table>
    </body>
    </html>
    """ % temp

    filename = 'web-browser.html'

    output = open(filename, "w")
    output.write(contents)
    output.close()

    webbrowser.open(filename)

    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed.")
