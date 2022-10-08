for zmienna in range(3):
    pin=input("Enter your PIN code: ")
    
    if pin=='0805':
        print("Access Granted!")
        break
    else:
        print("Incorrect...")
else:
    print("Sorry, your payment card has been blocked.")

