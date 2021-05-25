#Quantity of coffee and juice at first
coffeeInventory=3
juiceInventory=2
while True:
#When there is no coffee and juice
    if coffeeInventory==0 and juiceInventory==0:
        print("#"*47)
        print("All sold out. Thank you for using \"Hello Cafe\".")
        print("#"*47)
        break
#When there are some coffee or juice left
    else:
        print("*"*20)
        print("{0:^20s}".format("Hello Cafe"))
        print("*"*20)
        print("1. Coffee")
        print("2. Juice \n")
        menuSelect=input("Please enter a menu 1 or 2:")
#When customer choose coffee(menu1) 
        if menuSelect=="1":
            if coffeeInventory==0:
                print("There is no coffee left.")
            else: 
                print("You choose coffee.")
                while True:
                    coffeeQuantity=int(input("Please give a quantity."))
                    if coffeeQuantity<=coffeeInventory:
                        print("Here it is.")
                        coffeeInventory -=coffeeQuantity
                        break
                    else: 
                        print("There is only {} left.".format(coffeeInventory))
                        continue
#When customer choose juice(menu2)
        elif menuSelect=="2":
            if juiceInventory==0:
                print("There is no juice left.")
            else:
                print("You choose juice.")
                while True:
                    juiceQuantity=int(input("Please give a quantity."))
                    if juiceQuantity<=juiceInventory:
                        print("Here it is.")
                        juiceInventory -=juiceQuantity
                        break
                    else: 
                        print("There is only {} left.".format(juiceInventory))
                        continue
    
        
  
            
    

    
