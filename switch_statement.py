helpline=int(input("Press one for balance inquiry \npress 2 for new packages\npress 3 for customer care services\npress 4 for quit\n"))
match helpline:
    case 1:
        print("your balance is 12000000")
        
    case 2:
        print("here's the detail about new packages")
        
    case 3:
        print("welcome to customer care services")
    case 4:
        print("terminated")
        
    case _:
        print("no such case exist")
    

