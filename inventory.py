#INVENTORY MODULE: 
import mysql.connector
from mysql.connector import errorcode
from datetime import date
from mysql.connector import connection
import os

def clrscrean():
    print("\n" * 5)

def searchItem():
    try:
        os.system("cls")
        cxn = mysql.connector.connect(user="root", password="*****", host="localhost", database="Inventory")
        cursor = cxn.cursor()
        ProductCode = input("Enter product code to search an item from the inventory")
        query = ("SELECT * FROM inventory WHERE ProductCode =%s")
        search = (ProductCode)
        cursor.execute(query, search)
        search_count = 0
        
        for (ProductCode, ProductName, PurchaseDate, SalesDate, PurchasePrice, SalesPrice) in cursor:
            search_count += 1
            print("+++++++++++++++++++++++++++++++++++++++++++++++")
            print("1. Product code : ", ProductCode)
            print("2. Product name : ", ProductName)
            print("3. Purchase date : ", PurchaseDate)
            print("4. Sales date : ", SalesDate)
            print("5. Purchase price : ", PurchasePrice)
            print("6. Sales price : ", SalesPrice)
            print("+++++++++++++++++++++++++++++++++++++++++++++++")
            if search_count%2 == 0:
                input("Press any key to continue")
                clrscrean()
                print(search_count, "Item(s) found")
        cursor.close()
        cxn.close()
    except mysql.connector.Error as e:
        if e.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something went wrong with your user name or password")
        elif e.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(e)
    else:
        cxn.close()