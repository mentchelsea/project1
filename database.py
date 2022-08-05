
import mysql.connector
import mysql_config as c
def databaseCreate():
    cxn = mysql.connector.connect(user=c.user, password=c.password, host=c.host)
    cursor = cxn.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS Inventory")
    cursor.execute()
    cursor.close()
    cxn.close()
    
def tablesCreate():
    cxn = mysql.connector.connect(user=c.user, password=c.password, host=c.host, database="Inventory")
    cursor = cxn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS purchases(ProductCode int Primary key, ProductName varchar(50), PurchaseDate Date, PurchasePrice int, ProductStock int )")
    cursor.execute("CREATE TABLE IF NOT EXISTS sales(ProductCode int Primary key, ProductName varchar(50), SalesDate Date, SalesPrice int)")
    cursor.execute("CREATE TABLE IF NOT EXISTS inventory(ProductCode int Primary key, ProductName varchar(50), PurchaseDate Date, PurchasePrice int, SalesPrice int)")
    cursor.execute("CREATE TABLE IF NOT EXISTS user(UserID int Primary key auto increament, UserName varchar(50)")
    cursor.execute("CREATE TABLE IF NOT EXISTS admin(UserID int Primary key auto increament, UserName varchar(50)")
    cursor.close()
    cxn.close()
    
    