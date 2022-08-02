#SALES MODULE
import mysql.connector
from mysql.connector import errorcode
from datetime import date, datetime, timedelta
from mysql.connector import connection
import os


def clrscreen():
    print('\n' * 5)


def insertData():
    try:
        cxn = mysql.connector.connect(user="root", password="123", host="localhost", database="Inventory")
        cursor = cxn.cursor()
        ProductCode = input("Enter Product Code : ")
        ProductName = input("Enter Product Name : ")
        print("Enter Date of Sales (Date/Month and Year) seperately) : ")
        DD = int(input("Enter Date : "))
        MM = int(input("Enter Month : "))
        YY = int(input("Enter Year : "))
        SalesDate = date(YY,MM,DD)
        SalesPrice = int(input("Enter Sales Price : "))
        Qry = ("INSERT INTO Sales VALUES(%s, %s, %s, %s)")
        data = (ProductCode, ProductName, SalesDate, SalesPrice)
        cursor.execute(Qry, data)
        cxn.commit()
        cursor.close()
        cxn.close()
        print("Item Inserted.")
    except mysql.connector.Error as e:
        if e.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif e.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(e)
        cxn.close()


def deleteData():
    try:
        cxn = mysql.connector.connect(user="root", password="*****", host="localhost", database="Inventory")
        cursor = cxn.cursor()
        ProductCode = input("Enter Product Code to be deleted from the Sales : ")
        Query =("""DELETE FROM Sales WHERE ProductCode = %s""")
        del_search = (ProductCode)
        cursor.execute(Query, del_search)
        cxn.commit()
        cursor.close()
        cxn.close()
        print(cursor.rowcount, "Item(s) Deleted Successfully.")
    except mysql.connector.Error as e:
        if e.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif e.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(e)
        cxn.close()


def searchData():
    try:
        cxn = mysql.connector.connect(user="root", password="*****", host="localhost", database="Inventory")
        cursor = cxn.cursor()
        ProductCode = input("Enter Product Code to be searched from the Sales : ")
        query = ("SELECT * FROM Sales where ProductCode = %s")
        rec_search = (ProductCode)
        cursor.execute(query, rec_search)
        search_count = 0
        for(ProductCode, ProductName, SalesDate, SalesPrice) in cursor:
            search_count += 1
            print("++++++++++++++++++++++++++++++++++++++++++++++++++++")
            print("Product code : ", ProductCode)
            print("Product name : ", ProductName)
            print("Date of sale : ", SalesDate)
            print("Sale price : ", SalesPrice)
            print("+++++++++++++++++++++++++++++++++++++++++++++++++++++")
            if search_count%2 == 0:
                input("Press any key to continue: ")
                clrscreen()
                print(search_count, "Record(s) found")
        cxn.commit()
        cursor.close()
        cxn.close()
    except mysql.connector.Error as e:
        if e.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif e.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(e)
        cxn.close()


def updateData():
    try:
        cxn = mysql.connector.connect(user="root", password="*****", host="localhost", database="Inventory")
        cursor = cxn.cursor()
        ProductCode = input("Enter Product Code to be updated from the Sales : ")
        query = ("SELECT * FROM Sales WHERE ProductCode = %s")
        rec_search = (ProductCode)
        print("Enter new item")
        ProductName = input("Enter Product Name : ")
        print("Enter Date of Sales (Date/Month and Year seperately) as DD, MM and YY: ")
        DD = int(input("Enter Date : "))
        MM = int(input("Enter Month : "))
        YY = int(input("Enter Year : "))
        SalesDate = date(YY,MM,DD)
        SalesPrice = input("Enter Sales Price : ")
        Qry = ("UPDATE Sales SET ProductName=%s, SalesDate=%s, SalesPrice=%s WHERE ProductCode=%s")
        data = (ProductName, SalesDate, SalesPrice, ProductCode)
        cursor.execute(Qry,data)
        cxn.commit()
        cursor.close()
        cxn.close()
        print(cursor.rowcount, "Item(s) Updated Successfully.")
    except mysql.connector.Error as e:
        if e.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif e.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(e)
    cxn.close()