
import database, purchase
import menu
database.databaseCreate()
database.tablesCreate()
while True:
    purchase.clrscreen()
    print("****** INVENTORY MANAGEMENT SYSTEM ****** \n")
    print("+++++++++++++++++++++++++++++++++++++++++")
    print("1. Purchase")
    print("2. Sales")
    print("3. Inventory")
    print("4. Exit")
    
    choice = int(input("Make a choice between 1 and 4: "))
    if choice == 1:
        menu.menuPurchases()
    elif choice == 2:
        menu.menuSales()
    elif choice == 3:
        menu.menuInventory()
    elif choice == 4:
        break
    else:
        print("Wrong choice...try again")
        x = input("Press any key to continue: ")