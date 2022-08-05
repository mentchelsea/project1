from inventory_menu import adminLogin, userLogin
import mysql.connector
from mysql.connector import errorcode
from datetime import date, datetime, timedelta
from mysql.connector import connection
import os
import mysql_config as c

while True:
   # purchase.clrscreen()
    print("****** LOGING SYSTEM ****** \n")
    print("+++++++++++++++++++++++++++++++++++++++++")
    print("1. Admin")
    print("2. User")
    print("3. Exit")
    
    choice = int(input("Make a choice between 1 and 3: "))
    if choice == 1:
        userID = input("Enter admin ID: ")
        UserName = input("Enter user name: ")
        cxn = mysql.connector.connect(user=c.user, password=c.password, host=c.host, database="Inventory")
        cursor = cxn.cursor()
        # ProductCode = int(input("Enter Product Code to be deleted from the Sales : "))
        Query =(f"SELECT * FROM admin WHERE UserName = '{UserName}'")
        cursor.execute(Query)
        for record in cursor:
            if UserName == record[1]:
                print("Admin Login successful")
                adminLogin()
            else:
                print("Wrong information try again...")
                break
        #menu.menuPurchases()
    elif choice == 2:
        userID = input("Enter admin ID: ")
        UserName = input("Enter user name: ")
        cxn = mysql.connector.connect(user=c.user, password=c.password, host=c.host, database="Inventory")
        cursor = cxn.cursor()
        # ProductCode = int(input("Enter Product Code to be deleted from the Sales : "))
        Query =(f"SELECT * FROM user WHERE UserName = '{UserName}'")
        cursor.execute(Query)
        for record in cursor:
            if UserName == record[1]:
                print("User Login successful! ")
                userLogin()
            else:
                print("Wrong information try again...")
                break
        pass
       # menu.menuSales()
    elif choice == 3:
        break
    else:
        print("Wrong choice...try again")
        x = input("Press any key to continue: ")