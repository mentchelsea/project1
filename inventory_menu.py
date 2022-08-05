
#++++++++++++++++++++++++++++++++++++
# Product inventory management system
# Mengistu
#++++++++++++++++++++++++++++++++++++
import mysql_config
import menu, database,sales
# database.databaseCreate()
# database.tablesCreate()
def adminLogin():
    
    while True:
    # purchase.clrscreen()
        print("****** INVENTORY MANAGEMENT SYSTEM ****** \n")
        print("+++++++++++++++++++++++++++++++++++++++++")
        print("1. Purchase")
        print("2. Sales")
        print("3. Inventory")
        print("4. Create new user")
        print("5. Exit")
        
        choice = int(input("Make a choice between 1 and 5: "))
        if choice == 1:
            menu.menuPurchases()
        elif choice == 2:
            menu.menuSales()
        elif choice == 3:
            menu.menuInventory()
        elif choice == 4:
            sales.addNewUser()
        elif choice == 5:
            break
        else:
            print("Wrong choice...try again")
            x = input("Press any key to continue: ")
            
def userLogin():
    
    while True:
    # purchase.clrscreen()
        print("****** INVENTORY MANAGEMENT SYSTEM ****** \n")
        print("+++++++++++++++++++++++++++++++++++++++++")
        print("1. Purchase")
        print("2. Sales")
        print("3. Exit")
        
        choice = int(input("Make a choice between 1 and 3: "))
        if choice == 1:
            menu.menuPurchases()
        elif choice == 2:
            menu.menuSales()
        elif choice == 3:
            break
        else:
            print("Wrong choice...try again")
            x = input("Press any key to continue: ")