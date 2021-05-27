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
    print(inventory)
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
                    print("There is only {} left.".format(inventory))
                    continue
            except ValueError:
                print("You have to enter a right quantity of menu in number")
           
            #     if coffeeInventory==0:
            #         print("There is no coffee left.")
            #     else: 
            #         while True:
            #             try:

            #                 coffeeQuantity=int(input("Please give a quantity."))
                        
            #                 if coffeeQuantity<=coffeeInventory:
            #                     print("Here it is.")
            #                     coffeeInventory -=coffeeQuantity
            #                     break
            #                 else:
            #                     print("There is only {} left.".format(coffeeInventory))
            #                     continue
            #             except:
            #                 print("You have to enter a right quantity of menu in number")
                        
                            

            # elif menuSelect==2:
            #     if juiceInventory==0:
            #         print("There is no juice left.")
            #     else:
                    
            #         while True:
            #             try:
            #                 juiceQuantity=int(input("Please give a quantity."))
            #                 if juiceQuantity<=juiceInventory:
            #                     print("Here it is.")
            #                     juiceInventory -=juiceQuantity
            #                     break
            #                 else: 
            #                     print("There is only {} left.".format(juiceInventory))
            #                     continue
            #             except:
            #                 print("You have to enter a right quantity of menu in number")
        
                # elif menuSelect=="2":
                #     if juiceInventory==0:
                #         print("There is no juice left.")
                #     else:
                #         print("You choose juice.")
                #         while True:
                #             juiceQuantity=int(input("Please give a quantity."))
                #             if juiceQuantity<=juiceInventory:
                #                 print("Here it is.")
                #                 juiceInventory -=juiceQuantity
                #                 break
                #             else: 
                #                 print("There is only {} left.".format(juiceInventory))
                #                 continue
        
            


main()



            # if menuSelect==1:
            #     if coffeeInventory==0:
            #         print("There is no coffee left.")
            #     else: 
            #         print("You choose coffee.")
            #         while True:
            #             coffeeQuantity=int(input("Please give a quantity."))
            #             if coffeeQuantity<=coffeeInventory:
            #                 print("Here it is.")
            #                 coffeeInventory -=coffeeQuantity
            #                 break
            #             else: 
            #                 print("There is only {} left.".format(coffeeInventory))
            #                 continue

        
        
        



    











# coffeeInventory=3
# juiceInventory=2
# while True:
#     if coffeeInventory==0 and juiceInventory==0:
#         print("#"*47)
#         print("All sold out. Thank you for using \"Hello Cafe\".")
#         print("#"*47)
#         break
#     else:
#         print("*"*20)
#         print("{0:^20s}".format("Hello Cafe"))
#         print("*"*20)
#         print("1. Coffee")
#         print("2. Juice \n")
#         menuSelect=input("Please enter a menu 1 or 2:")
        # if menuSelect=="1":
        #     if coffeeInventory==0:
        #         print("There is no coffee left.")
        #     else: 
        #         print("You choose coffee.")
        #         while True:
        #             coffeeQuantity=int(input("Please give a quantity."))
        #             if coffeeQuantity<=coffeeInventory:
        #                 print("Here it is.")
        #                 coffeeInventory -=coffeeQuantity
        #                 break
        #             else: 
        #                 print("There is only {} left.".format(coffeeInventory))
        #                 continue
        # elif menuSelect=="2":
        #     if juiceInventory==0:
        #         print("There is no juice left.")
        #     else:
        #         print("You choose juice.")
        #         while True:
        #             juiceQuantity=int(input("Please give a quantity."))
        #             if juiceQuantity<=juiceInventory:
        #                 print("Here it is.")
        #                 juiceInventory -=juiceQuantity
        #                 break
        #             else: 
        #                 print("There is only {} left.".format(juiceInventory))
        #                 continue
    
        
  
            
    

    
