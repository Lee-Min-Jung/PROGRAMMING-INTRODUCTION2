menu1="coffee"
menu2="juice"
coffeeInventory=3
juiceInventory=2
def main():    
    menulist={1:"Coffee",2:"Juice"}
    while True:
        global coffeeInventory
        global juiceInventory
        try:
            if (coffeeInventory==0 and juiceInventory==0):
                print("#"*47)
                print("All sold out. Thank you for using \"Hello Cafe\".")
                print("#"*47)
                break
            else:
                print("*"*20)
                print("{0:^20s}".format("Hello Cafe"))
                print("*"*20)
                print("1. Coffee")
                print("2. Juice \n")
                menuSelect=int(input("Please enter a menu 1 or 2:"))
                print("You chose " + menulist[menuSelect])
        except KeyError:
            print("You have to enter right number of menu amoung 1 or 2.")
            continue
        except ValueError:
            print("You have to enter a number amoung 1 or 2.")
            continue
        else:
            if menuSelect==1:
                coffeeInventory=check(menu1,coffeeInventory)  
            elif menuSelect==2:
                juiceInventory=check(menu2,juiceInventory)                
def check(menu,inventory):
    global coffeeInventory
    global juiceInventory
    if inventory==0:
        print("There is no " +menu+ " left.")
        return inventory
    else: 
        while True:
            try:
                quantity=int(input("Please give a quantity."))
                if quantity<=inventory:
                    print("Here it is.")
                    inventory -=quantity
                    return inventory
                else:
                    continue
            except ValueError:
                print("You have to enter a right quantity of menu in number")
            finally:
                print(str(inventory) + " "+ menu+" is(are) left.")
main()
    
        
  
            
    

    
