
import mysql.connector

def databaseCreate():
    cxn = mysql.connector.connect(user="root", password="", host="localhost")
    cursor = cxn.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS Inventory")
    cursor.execute()
    cursor.close()
    cxn.close()
    
def tablesCreate():
    cxn = mysql.connector.connect(user="root", password="Mysql@57!", host="localhost", database="Inventory")
    cursor = cxn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS purchases(ProductCode int Primary key, ProductName varchar(50), PurchaseDate Date, PurchasePrice int, ProductStock int )")
    cursor.execute("CREATE TABLE IF NOT EXISTS sales(ProductCode int Primary key, ProductName varchar(50), SalesDate Date, SalesPrice int)")
    cursor.execute("CREATE TABLE IF NOT EXISTS inventory(ProductCode int Primary key, ProductName varchar(50), PurchaseDate Date, PurchasePrice int, SalesPrice int)")
    cursor.close()
    cxn.close()
    
    