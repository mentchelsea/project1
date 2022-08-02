#PURCHASES MODULE: 
import mysql.connector
from mysql.connector import errorcode
from datetime import date, datetime, timedelta
from mysql.connector import connection
import os
import platform


def clrscreen():
    if platform.system() == "Windows":
        print(os.system("cls"))


def insertData():
    try:
        cxn = mysql.connector.connect(user="root", password="*****", host='localhost', database='Inventory')
        cursor = cxn.cursor()
        ProductCode = input("Enter product code : ")
        ProductName = input("Enter product name : ")
        print("Enter Date of Purchase (Date/Month and Year seperately) DD, MM and YY : ")
        DD = int(input("Enter Date : "))
        MM = int(input("Enter Month : "))
        YY = int(input("Enter Year : "))
        PurchaseDate = date(YY,MM,DD)
        PurchasePrice = int(input("Enter product price : "))
        ProductStock = int(input("Enter quantity purchased : "))
        Query = ("INSERT INTO Purchases VALUES (%s, %s, %s, %s, %s)")
        data = (ProductCode, ProductName, PurchaseDate, PurchasePrice, ProductStock)
        cursor.execute(Query,data)
        Query1 = ("INSERT INTO inventory(ProductCode,ProductName,PurchaseDate,PurchasePrice) VALUES(%s, %s, %s, %s)")
        data1 = (ProductCode, ProductName, PurchaseDate, PurchasePrice)
        cursor.execute(Query1,data1)
        cxn.commit()
        cursor.close()
        cxn.close()
        print("Record Inserted.")
    except mysql.connector.Error as e:
        if e.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something went wrong with your user name or password")
        elif e.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(e)
    cxn.close()


def deleteData():
    try:
        cxn = mysql.connector.connect(user="root", password="***", host="localhost", database="Inventory")
        cursor = cxn.cursor()
        ProductCode = input("Enter product code to be deleted from the Purchases : ")
        Query = ("DELETE FROM Purchases WHERE ProductCode = %s")
        del_search = (ProductCode)
        cursor.execute(Query, del_search)
        cxn.commit()
        cursor.close()
        cxn.close()
        print(cursor.rowcount, "Record(s) Deleted Successfully.")
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
        cxn = mysql.connector.connect(user="root", password="123", host="localhost", database="Inventory")
        cursor = cxn.cursor()
        ProductCode = input("Enter Product Code to be searched from the Purchases : ")
        query = ("SELECT * FROM Purchases WHERE ProductCode = %s ")
        rec_search = (ProductCode)
        cursor.execute(query, rec_search)
        search_count = 0
        for(ProductCode, ProductName, PurchaseDate, PurchasePrice, ProductStock) in cursor:
            search_count += 1
            print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
            print("Product Code : ", ProductCode)
            print("Product Name : ", ProductName)
            print("Purchased on : ", PurchaseDate)
            print("Price of Product : ", PurchasePrice)
            print("Product in Stock : ", ProductStock)
            print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
            if search_count%2 == 0:
                input("Press any key continue")
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
        cxn = mysql.connector.connect(user='root', password='123', host='localhost', database='Inventory')
        cursor = cxn.cursor()
        ProductCode = input("Enter Product Code to be updated from the Purchases : ")
        query = ("SELECT * FROM Purchases WHERE ProductCode = %s ")
        rec_search = (ProductCode)
        print("Enter new data")
        ProductName = input("Enter Product Name : ")
        print("Enter Date of Purchase (Date/Month and Year seperately) as DD, MM and YY : ")
        DD = int(input("Enter Date : "))
        MM = int(input("Enter Month : "))
        YY = int(input("Enter Year : "))
        PurchaseDate = date(YY,MM,DD)
        PurchasePrice = int(input("Enter Product Price : "))
        ProductStock = int(input("Enter Quantity purchased : "))
        Qry = ("UPDATE Purchases SET ProductName=%s, PurchaseDate=%s, PurchasePrice=%s, ProductStock=%s  WHERE ProductCode=%s")
        data = (ProductName, PurchaseDate, PurchasePrice, ProductStock, ProductCode)
        cursor.execute(Qry,data)
        cxn.commit()
        cursor.close()
        cxn.close()
        print(cursor.rowcount, "Record(s) Updated Successfully.")
    except mysql.connector.Error as e:
        if e.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif e.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(e)
    cxn.close()
