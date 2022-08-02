
def menuPurchases():
    while True:
        purchases.clrscreen()
        print("****** PURCHASE MANAGEMENT SYSTEM ******\n")
        print("++++++++++++++++++++++++++++++++++++++++++")
        print("1. Add purchase")
        print("2. Search purchase")
        print("3. Delete purchase")
        print("4. Update purchase")
        print("5. Retun to main menu")
        print("++++++++++++++++++++++++++++++++++++++++++")
        
        choice = int(input("Make a choice between 1 and 5: "))
        if choice == 1:
            purchases.insertItem()
        elif choice == 2:
            purchases.searchItem()
        elif choice == 3:
            purchases.deleteItem()
        elif choice == 4:
            purchases.updateItem()
        elif choice == 5:
            return
        else:
           print("Wrong choice...try again")
           x = input("Press any key to continue: ")
           
def menuSales():
    while True:
        purchases.clrscrean()
        print("****** SALES MANAGEMENT SYSTEM ****** \n")
        print("+++++++++++++++++++++++++++++++++++++++++")
        print("1. Add sales ")
        print("2. Search sales")
        print("3. Delete sales")
        print("4. Update sales")
        print("5. Return to main menu")
        print("+++++++++++++++++++++++++++++++++++++++++")
        choice = int(input("Make a choice between 1 and 5: "))
        
        if choice == 1:
            sales.insertItem()
        elif choice == 2:
            sales.searchItem()
        elif choice == 3:
            sales.deleteItem()
        elif choice == 4:
            sales.updateItem()
        elif choice == 5:
            return
        else:
            print("Wrong choice...try again")
            x = input("Press any key to continue: ")
def menuInventory():
    while True:
        purchases.clrscrean()
        print("****** INVENTORY MANAGEMENT SYSTEM ****** \n")
        print("+++++++++++++++++++++++++++++++++++++++++")
        print("1. Search for inventory ")
        print("2. Return to main menu")
        print("+++++++++++++++++++++++++++++++++++++++++")
        choice = int(input("Make a choice between 1 and 2: "))
        if choice == 1:
            inventory.searchItem()
        elif choice == 2:
            return
        else:
            print("Wrong choice...try again")
            x = input("Press any key to continue: ")
        